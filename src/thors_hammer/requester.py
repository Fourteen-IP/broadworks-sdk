# this will be resposnsible for sending and receiving data from the API
import httpx
import asyncio
import socket
import ssl
import select
import logging
from typing import Any
from commands.base_command import OCICommand as BroadworksCommand
from abc import ABC, abstractmethod


class BaseRequester(ABC):
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
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    def __del__(self):
        self.disconnect()


class SyncTCPRequester(BaseRequester):
    def __init__(
        self,
        logger: logging.Logger,
        host: str,
        port: int = 2209,
        timeout: int = 30,
        session_id: str = None,
    ):
        super().__init__(
            logger=logger, host=host, port=port, timeout=timeout, session_id=session_id
        )
        self.sock = None

    def connect(self):
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

    def disconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except Exception as e:
                self.logger.warning(
                    f"Exception: {e} was raised when attemping to close {self.__class__.__name__}, but was ignored."
                )
                pass
            finally:
                self.sock = None

    def send_request(self, command: str) -> Any:
        try:
            if self.sock is None:
                self.connect()

            command_bytes = command.encode("utf-8") + b"\0"

            self.sock.sendall(command_bytes + b"\0")

            content = b""
            while True:
                readable, _, _ = select.select([self.sock], [], [], self.timeout)
                if not readable:
                    self.logger.warning("Socket read timed out")
                    break

                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                content += chunk

                if b"</BroadsoftDocument>" in content:
                    break

            return content.rstrip(b"\0").decode("utf-8")
        except Exception as e:
            self.logger.error(
                f"Failed to send command over {self.__class__.__name__}: {e}"
            )
            return None

    def __del__(self):
        self.disconnect()


class SyncSOAPRequester(BaseRequester):
    def __init__(
        self, logger: logging.Logger, host: str, port: int = 2208, timeout: int = 10
    ):
        super().__init__(logger=logger, host=host, port=port, timeout=timeout)
        self.client = None

    def connect(self):
        if self.client is None:
            try:
                self.client = httpx.Client(timeout=self.timeout)
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate client on {self.__class__.__name__}: {e}"
                )

    def disconnect(self):
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
        try:
            #             headers = {
            #                 "Content-Type": "text/xml; charset=utf-8",
            #                 "SOAPAction": "processOCIMessage",
            #             }

            #             oci_xml = f"""<BroadsoftDocument protocol="OCI" xmlns="C">
            #   <sessionId>{self.session_id}</sessionId>
            #   {command}
            # </BroadsoftDocument>"""

            #             soap_envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
            # <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
            #   <soapenv:Header/>
            #   <soapenv:Body>
            #     {oci_xml}
            #   </soapenv:Body>
            # </soapenv:Envelope>"""

            #             headers = {
            #                 "Content-Type": "text/xml; charset=utf-8",
            #                 "SOAPAction": "processOCIMessage",
            #             }

            # TODO, this class does not work as intended.

            response = self.client.post(
                self.host, headers="headers", data="soap_envelope"
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            self.logger.error(f"Failed to send command over {self.__name__}: {e}")
            return None

    def __del__(self):
        self.disconnect()


class AsyncTCPRequester(BaseRequester):
    def __init__(
        self, logger: logging.Logger, host: str, port: int = 2208, timeout: int = 10
    ):
        super().__init__(logger=logger, host=host, port=port, timeout=timeout)
        self.reader = None
        self.writer = None

    async def connect(self):
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
    def __init__(
        self, logger: logging.Logger, host: str, port: int = 2208, timeout: int = 10
    ):
        super().__init__(logger=logger, host=host, port=port, timeout=timeout)
        self.client = None

    def connect(self):
        if self.client is None:
            try:
                self.client = httpx.Client(timeout=self.timeout)
            except Exception as e:
                self.logger.error(
                    f"Failed to initiate client on {self.__class__.__name__}: {e}"
                )

    def disconnect(self):
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
