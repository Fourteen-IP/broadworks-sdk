# this will be resposnsible for sending and receiving data from the API
import httpx
import asyncio


class Requester:
    def __init__(self):
        self.sync = SyncRequester()
        self.async_ = AsyncRequester()


class SyncRequester:
    def __init__(self):
        pass

    def send_command_soap(self):
        pass

    def send_command_tcp(self):
        pass


class AsyncRequester:
    def __init__(self):
        pass

    def send_command_soap(self):
        pass

    def send_command_tcp(self):
        pass
