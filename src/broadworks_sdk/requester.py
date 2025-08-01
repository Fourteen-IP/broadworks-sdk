import asyncio
import socket
import requests
import ssl
import select
import logging
from abc import ABC, abstractmethod
from typing import Union, Tuple

from broadworks_sdk.exceptions import (
    THErrorSocketInitialisation,
    THErrorSendRequestFailed,
    THErrorSocketTimeout,
    THErrorClientInitialisation,
)
from broadworks_sdk.commands.base_command import OCICommand as BroadworksCommand

from lxml import etree, builder
from zeep import Client, Settings, Transport
from zeep import AsyncClient as AsyncClientZeep
from zeep.transports import AsyncTransport
from httpx import AsyncClient as AsyncClientHttpx
from httpx import Client as ClientHttpx


class BaseRequester(ABC):
    """Base class for all requesters.

    Args:
        logger (logging.Logger): The logger instance for logging messages.
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect to on the server.
        timeout (int): The timeout duration (in seconds) for operations.
        session_id (str): The session ID used for the connection.
    """

    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int,
        timeout: int,
        session_id: str,
    ):
        self.logger = logger
        self.host = host
        self.port = port
        self.timeout = timeout
        self.session_id = session_id

    @abstractmethod
    def send_request(
        self, command: BroadworksCommand
    ) -> Union[str, Tuple[Exception, Exception]]:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Union[str, Tuple[Exception, Exception]]: The server's response as a string,
            or a tuple containing exceptions if an error occurs.
        """
        pass

    @abstractmethod
    def connect(self):
        """Connects to the server."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnects from the server."""
        pass

    def build_oci_xml(self, command: BroadworksCommand) -> bytes:
        """Builds an OCI XML request from the given BroadworksCommand.

        Constructs an XML document with a session ID and the encoded command,
        wrapped in a BroadsoftDocument element with the OCI protocol.

        Args:
            command (BroadworksCommand): The command to be encoded into the XML.

        Returns:
            bytes: The serialized XML document as bytes, encoded with ISO-8859-1.
        """

        self.logger.debug(
            f"Building OCI XML for command: {command} with session ID: {self.session_id}"
        )

        ElementMaker = builder.ElementMaker(
            namespace="C",
            nsmap={None: "C", "xsi": "http://www.w3.org/2001/XMLSchema-instance"},
        )

        session_id = etree.Element("sessionId")
        session_id.text = self.session_id
        session_id.set("xmlns", "")

        command = etree.fromstring(command.encode("ISO-8859-1"))

        broadsoft_doc = ElementMaker.BroadsoftDocument(
            session_id, command, protocol="OCI"
        )

        return etree.tostring(
            broadsoft_doc, xml_declaration=True, encoding="ISO-8859-1"
        )

    def __del__(self):
        self.disconnect()


class SyncTCPRequester(BaseRequester):
    """A synchronous TCP requester for BroadWorks OCI-P.

    This class manages a synchronous connection to a BroadWorks Application
    Server. It opens a TCP socket connection, optionally wrapped with SSL for
    encrypted traffic, and sends OCI-P commands over the connection.

    Args:
        logger (logging.Logger): An instance of `logging.Logger` for logging messages.
        host (str): The hostname or IP address of the BroadWorks server.
        port (int): The port for the OCI-P interface, defaults to 2209.
        timeout (int): The timeout for socket operations in seconds, defaults to 30.
        session_id (str): The session ID for an established OCI-P session.
        tls (bool): Whether to use TLS for the connection, defaults to True.
    """

    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int = 2209,
        timeout: int = 30,
        session_id: str = None,
        tls: bool = True,
    ):
        self.sock = None
        self.tls = tls
        super().__init__(
            logger=logger,
            host=host,
            port=port,
            timeout=timeout,
            session_id=session_id,
        )
        self.connect()

    def connect(self):
        """
        Opens a TCP socket connection to the server.

        If TLS is enabled, the socket is wrapped with SSL for encrypted communication.

        Returns:
            Union[None, Tuple[Exception, Exception]]: None if the connection is successful,
            or a tuple containing exceptions if an error occurs.
        """
        if self.sock is None:
            try:
                if self.tls:
                    raw_sock = socket.create_connection(
                        (self.host, self.port), timeout=self.timeout
                    )
                    context = ssl.create_default_context()
                    self.sock = context.wrap_socket(raw_sock, server_hostname=self.host)
                else:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.settimeout(self.timeout)
                    self.sock.connect((self.host, self.port))
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate socket on {self.__class__.__name__}: {e}"
                )
                return (THErrorSocketInitialisation, e)
            finally:
                self.logger.info(
                    f"Initiated socket on {self.__class__.__name__}: {self.host}:{self.port}"
                )

    def disconnect(self):
        """Disconnects from the server.

        Closes the TCP socket connection if it is open. Logs a warning if an
        exception occurs during the disconnection process.
        """
        if self.sock:
            try:
                self.sock.close()
            except Exception as e:
                self.logger.warning(
                    f"Exception: {e} was raised when attemping to close {self.__class__.__name__}, but was ignored."
                )
                pass  # Pass as this is expected behaviour, but better to put a warning.
            finally:
                self.sock = None

    def send_request(
        self, command: BroadworksCommand
    ) -> Union[str, Tuple[Exception, Exception]]:
        """Sends a request to the server.

        Encodes the given command into an OCI XML document and sends it over
        the TCP connection. Waits for and returns the server's response.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Union[str, Tuple[Exception, Exception]]: The server's response as a string,
            or a tuple containing exceptions if an error occurs.
        """
        try:
            if self.sock is None and isinstance(
                (connection := self.connect()), tuple
            ):  # If it returns the exception tuple, we return it again
                return connection

            command_bytes = self.build_oci_xml(command)

            self.logger.debug(
                f"Sending command over {self.__class__.__name__}: {command_bytes.decode('ISO-8859-1')}"
            )

            self.sock.sendall(command_bytes + b"\n")

            content = b""
            while True:
                readable, _, _ = select.select([self.sock], [], [], self.timeout)
                if not readable:
                    self.logger.error(f"Select timed out: {self.__class__.__name__}")
                    return (THErrorSocketTimeout, TimeoutError("Socket read timed out"))

                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                content += chunk

                if b"</BroadsoftDocument>" in content:
                    break

            return content.rstrip(b"\0").decode("ISO-8859-1")
        except Exception as e:
            return (THErrorSendRequestFailed, e)

    def __del__(self):
        self.disconnect()


class SyncSOAPRequester(BaseRequester):
    """A synchronous SOAP requester for BroadWorks OCI-P.

    This class manages a synchronous connection to a BroadWorks Application
    Server, handling the wrapping of OCI commands into SOAP envelopes and
    returning the response.

    Args:
        logger (logging.Logger): An instance of `logging.Logger` for logging messages.
        host (str): The hostname or IP address of the BroadWorks server.
        port (int): The port for the OCI-P interface, defaults to 2209.
        timeout (int): The timeout for HTTP requests in seconds, defaults to 10.
        session_id (str): The session ID for an established OCI-P session.
    """

    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int = 2209,
        timeout: int = 10,
        session_id: str = None,
    ):
        self.zclient = None
        super().__init__(
            logger=logger,
            host=host,
            port=port,
            timeout=timeout,
            session_id=session_id,
        )
        self.connect()

    def connect(self):
        """
        Opens a HTTP Client connection to the Server.

        Returns:
            THErrorClientInitialisation if the client fails to open.
        """
        if self.zclient is None:
            try:
                self.client = requests.sessions.Session()
                settings = Settings(strict=False, xml_huge_tree=True)
                transport = Transport(session=self.client, timeout=self.timeout)
                self.zclient = Client(
                    wsdl=f"{self.host}?wsdl", transport=transport, settings=settings
                )
                self.logger.info(
                    f"Initiated socket on {self.__class__.__name__}: {self.host}:{self.port}"
                )
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate client on {self.__class__.__name__}: {e}"
                )
                return (THErrorClientInitialisation, e)

    def disconnect(self):
        """Disconnects from the server.

        Closes the HTTP client connection if it is open. Logs a warning if an
        exception occurs during the disconnection process.
        """
        if self.zclient:
            try:
                self.client.close()
            except Exception as e:
                self.logger.warning(
                    f"Exception: {e} was raised when attempting to close {self.__class__.__name__}, but was ignored."
                )
                pass
            finally:
                self.zclient = None

    def send_request(
        self, command: BroadworksCommand
    ) -> Union[str, Tuple[Exception, Exception]]:
        """Sends a request to the server.

        Encodes the given command into an OCI XML document, wraps it in a SOAP
        envelope, and sends it to the server. Waits for and returns the server's
        response.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Union[str, Tuple[Exception, Exception]]: The server's response as a string,
            or a tuple containing exceptions if an error occurs.
        """
        try:
            command = self.build_oci_xml(command)

            self.logger.debug(
                f"Sending command over {self.__class__.__name__}: {command.decode('ISO-8859-1')}"
            )

            response = self.zclient.service.processOCIMessage(command)

            return response
        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return (THErrorSendRequestFailed, e)

    def __del__(self):
        self.disconnect()


class AsyncTCPRequester(BaseRequester):
    """An asynchronous TCP requester for BroadWorks OCI-P.

    This class manages an asynchronous connection to a BroadWorks Application
    Server. It will open a TCP Socket connection, using 2209 for an SSL wrapped
    socket for encrypted traffic.

    Args:
        session_id (str): The session ID passed to keep the session alive.
        logger (logging.Logger): An instance of `logging.Logger` for logging messages.
        host (str): The hostname or IP address of the BroadWorks server.
        port (int): The port for the OCI-P interface, defaults to 2209.
        timeout (int): The timeout for HTTP requests in seconds, defaults to 10.
    """

    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int = 2209,
        timeout: int = 10,
        session_id: str = None,
        tls: bool = True,
    ):
        self.reader = None
        self.writer = None
        self.tls = tls
        super().__init__(
            logger=logger,
            host=host,
            port=port,
            timeout=timeout,
            session_id=session_id,
        )
        self.connect()

    async def connect(self):
        """Connects to the server.

        Initializes the asynchronous HTTP client and SOAP client for sending
        OCI commands. Fetches the WSDL file and prepares the SOAP client for
        communication.

        Returns:
            Union[None, Tuple[Exception, Exception]]: None if the connection is successful,
            or a tuple containing exceptions if an error occurs.
        """
        if self.reader is None and self.writer is None:
            try:
                if self.tls:
                    context = ssl.create_default_context()
                    self.reader, self.writer = await asyncio.wait_for(
                        asyncio.open_connection(
                            host=self.host, port=self.port, ssl=context
                        ),
                        timeout=self.timeout,
                    )
                    self.logger.info(
                        f"Initiated socket on {self.__class__.__name__}: {self.host}:{self.port}"
                    )
                else:
                    self.reader, self.writer = await asyncio.wait_for(
                        asyncio.open_connection(self.host, self.port),
                        timeout=self.timeout,
                    )
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate socket on {self.__class__.__name__}: {e}"
                )
                return (THErrorSocketInitialisation, e)

    async def disconnect(self):
        """Disconnects from the server.

        Closes the asynchronous HTTP client if it is open. Logs a warning if an
        exception occurs during the disconnection process.
        """
        if self.reader and self.writer:
            try:
                self.writer.close()
                await self.writer.wait_closed()
            except Exception as e:
                self.logger.warning(
                    f"Exception: {e} was raised when attemping to close {self.__class__.__name__}, but was ignored."
                )
                pass
            finally:
                self.writer = None
                self.reader = None

    async def send_request(
        self, command: BroadworksCommand
    ) -> Union[str, Tuple[Exception, Exception]]:
        """Sends a request to the server.

        Encodes the given command into an OCI XML document and sends it over
        the TCP connection. Waits for and returns the server's response.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Union[str, Tuple[Exception, Exception]]: The server's response as a string,
            or a tuple containing exceptions if an error occurs.
        """
        try:
            if self.reader or self.writer is None:
                result = await self.connect()
                if isinstance(result, tuple):  # Error returned
                    return result

            command = await command

            command_bytes = await self.build_oci_xml(command)

            self.logger.debug(
                f"Sending command over {self.__class__.__name__}: {command_bytes.decode('ISO-8859-1')}"
            )

            self.writer.write(command_bytes + b"\0")
            await self.writer.drain()

            content = b""
            while True:
                try:
                    chunk = await asyncio.wait_for(
                        self.reader.read(4096), timeout=self.timeout
                    )
                except asyncio.TimeoutError as e:
                    self.logger.error(
                        f"Socket read timed out in {self.__class__.__name__}: {e}"
                    )
                    return (THErrorSocketTimeout, e)

                if not chunk:
                    break

                content += chunk
                if b"</BroadsoftDocument>" in content:
                    break
            return content.rstrip(b"\0").decode("ISO-8859-1")

        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return (THErrorSendRequestFailed, e)

    async def build_oci_xml(self, command: BroadworksCommand) -> bytes:
        """Builds an OCI XML request from the given BroadworksCommand asynchronously.

        Uses a thread pool executor to offload the XML building process to a
        separate thread, ensuring non-blocking behavior.

        Args:
            command (BroadworksCommand): The command to be encoded into the XML.

        Returns:
            bytes: The serialized XML document as bytes, encoded with ISO-8859-1.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, super().build_oci_xml, command)

    def __del__(self):
        self.disconnect()


class AsyncSOAPRequester(BaseRequester):
    """An asynchronous SOAP requester for BroadWorks OCI-P.

    This class manages an asynchronous connection to a BroadWorks Application
    Server, handling the wrapping of OCI commands into SOAP envelopes and
    returning the response.

    Args:
        logger (logging.Logger): An instance of `logging.Logger` for logging messages.
        host (str): The hostname or IP address of the BroadWorks server.
        port (int): The port for the OCI-P interface, defaults to 2209.
        timeout (int): The timeout for HTTP requests in seconds, defaults to 10.
        session_id (str): The session ID for an established OCI-P session.
    """

    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int = 2209,
        timeout: int = 10,
        session_id: str = None,
    ):
        self.async_client = None
        self.wsdl_client = None
        self.zeep_client = None
        super().__init__(
            logger=logger,
            host=host,
            port=port,
            timeout=timeout,
            session_id=session_id,
        )
        self.connect()

    async def connect(self):
        """Connects to the server.

        Initializes the asynchronous HTTP client and SOAP client for sending
        OCI commands. Fetches the WSDL file and prepares the SOAP client for
        communication.

        Returns:
            Union[None, Tuple[Exception, Exception]]: None if the connection is successful,
            or a tuple containing exceptions if an error occurs.
        """
        if None not in (self.async_client, self.wsdl_client, self.zeep_client):
            pass
        try:
            self.async_client = AsyncClientHttpx()
            self.wsdl_client = ClientHttpx()
            # Zeep fetches the WSDL synchronously, but actual requests are asynchronous, so we must have a Sync and Async Httpx Client.

            settings = Settings(strict=False, xml_huge_tree=True)
            transport = AsyncTransport(
                client=self.async_client,
                wsdl_client=self.wsdl_client,
                timeout=self.timeout,
            )

            self.zeep_client = AsyncClientZeep(
                wsdl=f"{self.host}?wsdl", transport=transport, settings=settings
            )

        except Exception as e:
            self.logger.error(
                f"Failed to initiate client on {self.__class__.__name__}: {e}"
            )
            return (THErrorClientInitialisation, e)

    async def disconnect(self):
        """Disconnects from the server.

        Closes the asynchronous HTTP client if it is open. Logs a warning if an
        exception occurs during the disconnection process.
        """
        if self.client:
            try:
                self.client.close()
            except Exception as e:
                self.logger.warning(
                    f"Exception: {e} was raised when attemping to close {self.__class__.__name__}, but was ignored."
                )
                pass
            finally:
                self.client = None

    async def send_request(
        self, command: BroadworksCommand
    ) -> Union[str, Tuple[Exception, Exception]]:
        """Sends a request to the server.

        Encodes the given command into an OCI XML document, wraps it in a SOAP
        envelope, and sends it to the server. Waits for and returns the server's
        response.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Union[str, Tuple[Exception, Exception]]: The server's response as a string,
            or a tuple containing exceptions if an error occurs.
        """
        if None in (self.async_client, self.wsdl_client, self.zeep_client):
            connection = await self.connect()
            if isinstance(connection, tuple):
                return connection

        command = await command

        try:
            command = await self.build_oci_xml(command)

            self.logger.debug(
                f"Sending command over {self.__class__.__name__}: {command.decode('ISO-8859-1')}"
            )

            response = await self.zeep_client.service.processOCIMessage(command)

            return response
        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return (THErrorSendRequestFailed, e)

    async def build_oci_xml(self, command: BroadworksCommand) -> bytes:
        """Builds an OCI XML request from the given BroadworksCommand asynchronously.

        Uses a thread pool executor to offload the XML building process to a
        separate thread, ensuring non-blocking behavior.

        Args:
            command (BroadworksCommand): The command to be encoded into the XML.

        Returns:
            bytes: The serialized XML document as bytes, encoded with ISO-8859-1.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, super().build_oci_xml, command)

    def __del__(self):
        self.disconnect()


def create_requester(
    logger: logging.Logger,
    session_id: str,
    host: str,
    port: int,
    conn_type: str = "SOAP",
    async_: bool = True,
    timeout: int = 10,
    tls: bool = True,
) -> BaseRequester:
    """Factory function to create a requester.

    Creates and returns an instance of a requester class based on the specified
    connection type and whether asynchronous behavior is required.

    Args:
        logger (logging.Logger): The logger to use for the requester.
        session_id (str): The session ID to use for the connection.
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect to on the server.
        conn_type (str): The connection type to use ("SOAP" or "TCP").
        async_ (bool): Whether to use an asynchronous requester.
        timeout (int): The timeout duration (in seconds) for operations.
        tls (bool): Whether to use TLS for the connection (only applicable for TCP).

    Returns:
        BaseRequester: An instance of the appropriate requester class.
    """
    if conn_type == "SOAP":
        if async_:
            return AsyncSOAPRequester(
                host=host,
                port=port,
                timeout=timeout,
                logger=logger,
                session_id=session_id,
            )
        else:
            return SyncSOAPRequester(
                host=host,
                port=port,
                timeout=timeout,
                logger=logger,
                session_id=session_id,
            )
    elif conn_type == "TCP":
        if async_:
            return AsyncTCPRequester(
                host=host,
                port=port,
                timeout=timeout,
                logger=logger,
                session_id=session_id,
                tls=tls,
            )
        else:
            return SyncTCPRequester(
                host=host,
                port=port,
                timeout=timeout,
                logger=logger,
                session_id=session_id,
                tls=tls,
            )
