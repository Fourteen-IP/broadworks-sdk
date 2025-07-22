# this will be resposnsible for sending and receiving data from the API
import httpx
import asyncio
import socket
import ssl
import select
import logging
import xml.etree.ElementTree as ET
from html import unescape
from exceptions import (
    THErrorSocketInitialisation,
    THErrorSendRequestFailed,
    THErrorSocketTimeout,
    THErrorClientInitialisation,
)
from typing import Any
from commands.base_command import OCICommand as BroadworksCommand
from abc import ABC, abstractmethod


class BaseRequester(ABC):
    """Base class for all requesters.

    Args:
        logger (logging.Logger): The logger of the requester.
        host (str): The host of the server.
        port (int): The port of the server.
        timeout (int): The timeout of the requester.
        session_id (str): The session id of the requester.
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
    def send_request(self, command: BroadworksCommand) -> Any:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.
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

    def __del__(self):
        self.disconnect()


class SyncTCPRequester(BaseRequester):
    """A synchronous TCP requester for BroadWorks OCI-P.

    This class manages a synchronous connection to a BroadWorks Application
    Server. It will open a TCP Socket connection, using 2209 for an SSL wrapped
    socket for encrypted traffic.

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
        timeout: int = 30,
        session_id: str = None,
    ):
        self.sock = None
        super().__init__(
            logger=logger, host=host, port=port, timeout=timeout, session_id=session_id
        )
        self.connect()

    def connect(self):
        """
        Opens a TCP Socket connection to the Server

        Returns:
            THErrorSocketInitialisation if the Socket fails to open
        """
        if self.sock is None:
            try:
                if self.port == 2209:  # SSL
                    raw_sock = socket.create_connection(
                        (self.host, self.port), timeout=self.timeout
                    )
                    context = ssl.create_default_context()
                    self.sock = context.wrap_socket(raw_sock, server_hostname=self.host)
                elif self.port == 2208:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.settimeout(self.timeout)
                    self.sock.connect((self.host, self.port))
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate socket on {self.__class__.__name__}: {e}"
                )
                return (THErrorSocketInitialisation, e)

    def disconnect(self):
        """Disconnects from the server."""
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

    def send_request(self, command: BroadworksCommand) -> Any:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Any: The response from the server.
        """
        try:
            if self.sock is None:
                self.connect()

            command_bytes = (
                "<?xml version='1.0' encoding='ISO-8859-1'?>"
                '<BroadsoftDocument xmlns="C" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" protocol="OCI">'
                f'<sessionId xmlns="">{self.session_id}</sessionId>'
                f"{command}"
                "</BroadsoftDocument>"
            )

            command_bytes = command_bytes.encode("utf-8")

            self.sock.sendall(command_bytes + b"\0")

            content = b""
            while True:
                readable, _, _ = select.select([self.sock], [], [], self.timeout)
                if not readable:
                    break

                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                content += chunk

                if b"</BroadsoftDocument>" in content:
                    break

            return content.rstrip(b"\0").decode("utf-8")
        except socket.timeout as e:
            self.logger.error(f"Socket timed out: {self.__class__.__name__}: {e}")
            return (THErrorSocketTimeout, e)
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
        self.client = None
        super().__init__(
            logger=logger, host=host, port=port, timeout=timeout, session_id=session_id
        )
        self.connect()

    def connect(self):
        """
        Opens a HTTP Client connection to the Server.

        Returns:
            THErrorClientInitialisation if the client fails to open.
        """
        if self.client is None:
            try:
                self.client = httpx.Client(timeout=self.timeout)
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate client on {self.__class__.__name__}: {e}"
                )
                return (THErrorClientInitialisation, e)

    def disconnect(self):
        """Disconnects from the server."""
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

    def send_request(self, command: BroadworksCommand) -> Any:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Any: The response from the server.
        """
        try:
            oci_payload = f"""<?xml version="1.0" encoding="ISO-8859-1"?>
                            <BroadsoftDocument xmlns="C" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" protocol="OCI">
                                <sessionId xmlns="">{self.session_id}</sessionId>
                                {command}
                            </BroadsoftDocument>"""

            soap_envelope = f"""<?xml version="1.0" encoding="ISO-8859-1"?>
                                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                                                  xmlns:web="urn:com:broadsoft:webservice">
                                  <soapenv:Header/>
                                  <soapenv:Body>
                                    <web:processOCIMessage>
                                      <in0><![CDATA[
                                {oci_payload}
                                      ]]></in0>
                                    </web:processOCIMessage>
                                  </soapenv:Body>
                                </soapenv:Envelope>"""  # The WSDL for provisioning expects a processOCIMessage action to be wraped in '<in0>'

            headers = {
                "Content-Type": "text/xml; charset=ISO-8859-1",
                "SOAPAction": "",
            }

            response = self.client.post(
                self.host, headers=headers, data=soap_envelope.encode("ISO-8859-1")
            )
            response.raise_for_status()

            root = ET.fromstring(response.text)

            encoded_inner = root.find(
                ".//{urn:com:broadsoft:webservice}processOCIMessageReturn"
            ).text

            decoded_inner = unescape(
                encoded_inner.strip()
            )  # We need to decode some XML Entity Values from the center, this ensures the response remains a proper string, and keeps the XML header as per the spec.

            return ET.fromstring(decoded_inner)
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
        logger (logging.Logger): An instance of `logging.Logger` for logging messages.
        host (str): The hostname or IP address of the BroadWorks server.
        port (int): The port for the OCI-P interface, defaults to 2209.
        timeout (int): The timeout for HTTP requests in seconds, defaults to 10.
    """

    def __init__(
        self, logger: logging.Logger, host: str, port: int = 2209, timeout: int = 10
    ):
        super().__init__(logger=logger, host=host, port=port, timeout=timeout)
        self.reader = None
        self.writer = None

    async def connect(self):
        """Connects to the server."""
        if self.reader and self.writer is None:
            try:
                self.reader, self.writer = await asyncio.open_connection(
                    host=self.host, port=self.port
                )
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate socket on {self.__class__.__name__}: {e}"
                )

    async def disconnect(self):
        """Disconnects from the server."""
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

    async def send_request(self, command: BroadworksCommand) -> Any:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Any: The response from the server.
        """
        try:
            self.writer.write(command)
            await self.writer.drain()

            response = await self.reader.readuntil(b"</BroadsoftDocument>")

            return response.decode()
        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return None

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
    """

    def __init__(
        self, logger: logging.Logger, host: str, port: int = 2209, timeout: int = 10
    ):
        super().__init__(logger=logger, host=host, port=port, timeout=timeout)
        self.client = None

    def connect(self):
        """Connects to the server."""
        if self.client is None:
            try:
                self.client = httpx.Client(timeout=self.timeout)
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate client on {self.__class__.__name__}: {e}"
                )

    def disconnect(self):
        """Disconnects from the server."""
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

    async def send_request(self, command: BroadworksCommand) -> Any:
        """Sends a request to the server.

        Args:
            command (BroadworksCommand): The command to send to the server.

        Returns:
            Any: The response from the server.
        """
        try:
            headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": ""}

            response_cor = await self.client.post(
                self.url, headers=headers, data=command
            )

            response = await asyncio.gather(response_cor)

            await self.client.aclose()

            return response.text
        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return None

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
) -> BaseRequester:
    """Factory function to create a requester.

    Args:
        logger (logging.Logger): The logger to use.
        session_id (str): The session ID to use.
        host (str): The host to connect to.
        port (int): The port to connect to.
        conn_type (str): The connection type to use.
        async_ (bool): Whether to use an asynchronous requester.
        timeout (int): The timeout to use.

    Returns:
        BaseRequester: The created requester.
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
            )
        else:
            return SyncTCPRequester(
                host=host,
                port=port,
                timeout=timeout,
                logger=logger,
                session_id=session_id,
            )
