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

    @abstractmethod
    def send_command(self, command: BroadworksCommand) -> Any:
        pass


class SyncTCPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        self.host = host
        self.port = port
        self.timeout = timeout

    def send_command(self, command: BroadworksCommand) -> Any:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                sock.connect((self.host, self.port))

                sock.sendall(command)

                response = b""
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    response += data

            return response.decode("utf-8")
        except Exception as e:
            print(f"Error: {e}")
            return None

    def send_raw_command(self):
        pass


class SyncSOAPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.client = httpx.Client(timeout=timeout)

    def send_command(self, command: BroadworksCommand) -> Any:
        try:
            headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": ""}

            response = self.client.post(self.url, headers=headers, data=command)

            self.client.close()
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def send_raw_command(self):
        pass


class AsyncTCPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None

    async def send_command(self, command: BroadworksCommand) -> Any:
        try:
            reader, writer = await asyncio.open_connection(
                host=self.host, port=self.port
            )

            writer.write(command)
            await writer.drain()

            response = await reader.read()  # "If n is not provided or set to -1, read until EOF, then return all read bytes"

            writer.close()
            await writer.wait_closed()

            return response.decode()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def send_raw_command(self):
        pass


class AsyncSOAPRequester(BaseRequester):
    def __init__(self, host: str, port: int = 2208, timeout: int = 10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)

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

    def send_raw_command(self):
        pass


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
