# this will be resposnsible for sending and receiving data from the API
import httpx
import asyncio
import socket
from typing import Any
from .commands.base_command import BroadworksCommand
from abc import ABC, abstractmethod


class BaseRequester(ABC):
    def __init__(self, host: str, port: int, timeout: int):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.session_id = ""

    @abstractmethod
    def send_command(self, command: BroadworksCommand) -> Any:
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
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        super().__init__(host, port, timeout)
        self.sock = None

    def connect(self):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(self.timeout)
            self.sock.connect((self.host, self.port))

    def disconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except Exception:
                pass
            finally:
                self.sock = None

    def send_command(self, command: BroadworksCommand) -> Any:
        try:
            if self.sock is None:
                self.connect()

            self.sock.sendall(command)

            response = b""
            while True:
                data = self.sock.recv(1024)
                if not data:
                    break
                response += data

            return response.decode("utf-8")
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __del__(self):
        self.disconnect()


class SyncSOAPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        super().__init__(host, port, timeout)
        self.client = None

    def connect(self):
        if self.client is None:
            self.client = httpx.Client(timeout=self.timeout)

    def disconnect(self):
        if self.client:
            try:
                self.client.close()
            except Exception:
                pass
            finally:
                self.client = None

    def send_command(self, command: BroadworksCommand) -> Any:
        try:
            headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": ""}

            response = self.client.post(self.url, headers=headers, data=command)

            self.client.close()
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __del__(self):
        self.disconnect()


class AsyncTCPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        super().__init__(host, port, timeout)
        self.reader = None
        self.writer = None

    async def connect(self):
        if self.reader and self.writer is None:
            self.reader, self.writer = await asyncio.open_connection(
                host=self.host, port=self.port
            )

    async def disconnect(self):
        if self.reader and self.writer:
            try:
                self.writer.close()
                await self.writer.wait_closed()
            except Exception:
                pass
            finally:
                self.writer = None
                self.reader = None

    async def send_command(self, command: BroadworksCommand) -> Any:
        try:
            self.writer.write(command)
            await self.writer.drain()

            response = await self.reader.readuntil(b"</BroadsoftDocument>")

            return response.decode()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __del__(self):
        self.disconnect()


class AsyncSOAPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        super().__init__(host, port, timeout)
        self.client = None

    def connect(self):
        if self.client is None:
            self.client = httpx.Client(timeout=self.timeout)

    def disconnect(self):
        if self.client:
            try:
                self.client.close()
            except Exception:
                pass
            finally:
                self.client = None

    async def send_command(self, command: BroadworksCommand) -> Any:
        try:
            headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": ""}

            response_cor = await self.client.post(
                self.url, headers=headers, data=command
            )

            response = await asyncio.gather(response_cor)

            await self.client.aclose()

            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __del__(self):
        self.disconnect()


def create_requester(
    host: str, port: int, connection_type: str = "SOAP", async_: bool = True
) -> BaseRequester:
    if connection_type == "SOAP":
        if async_:
            return AsyncSOAPRequester(host, port)
        else:
            return SyncSOAPRequester(host, port)
    elif connection_type == "TCP":
        if async_:
            return AsyncTCPRequester(host, port)
        else:
            return SyncTCPRequester(host, port)
