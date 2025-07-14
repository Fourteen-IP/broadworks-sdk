import sys
import logging
import hashlib
import uuid
from typing import Dict, Type
from abc import ABC, abstractmethod

from .commands.base_command import BroadworksCommand as BWKSCommand
from .requester import create_requester 
from .exceptions import THError

import attr
'''
TODO: 
- Dispatch table
- command classes I think can be condensed with the use of command classes and dist table
- BWKSCommand may be BWKSType
'''

@attr.s(slots=True, kw_only=True)
class BaseClient(ABC):
    """Base class for all clients
    - Host: The host of the server
    - Username: The username of the user
    - Password: The password of the user
    - Conn_type: The type of connection to the server
    - User_agent: The user agent of the client
    - Timeout: The timeout of the client
    - Logger: The logger of the client
    - Authenticated: Whether the client is authenticated
    - Session_id: The session id of the client
    - Dispatch_table: The dispatch table of the client
    """
    
    host: str = attr.ib()
    username: str = attr.ib()
    password: str = attr.ib()
    conn_type: str = attr.ib(default="TCP", validator=attr.validators.in_(["TCP", "SOAP"]))
    user_agent: str = attr.ib(default="Thor\'s Hammer")
    timeout: int = attr.ib(default=30)
    logger: logging.Logger = attr.ib(default=None)
    authenticated: bool = attr.id(default=False)
    session_id: str = attr.ib(default=None)

    _dispatch_table: Dict[str, Type[BWKSCommand]] = attr.ib(default=None)

    def __attrs_post_init__(self):
        try: 
            self.authenticate()
            self._dispatch_table = self._set_up_dispatch_table()
            self.logger = self.logger or self._set_up_logging()
            self.session_id or str(uuid.uuid4())
            self.requester = create_requester(
                conn_type=self.conn_type,
                async_mode=self.async_mode,
                host=self.host,
                timeout=self.timeout,
                logger=self.logger,
                session_id=self.session_id
            )
        except Exception as e:
            print(f"Failed to authenticate {e}")
            raise Exception #TODO: Handle better
    
    @property
    @abstractmethod
    def async_mode(self) -> bool:
        """Whether the client is in async mode"""
        pass

    @abstractmethod
    def command(self, command: BWKSCommand) -> BWKSCommand:
        """Executes command class from .commands lib"""
        pass
    
    @abstractmethod
    def raw_command(self, command: str, **kwargs) -> BWKSCommand:
        """Executes raw command specified by end user - instantiates class command"""
        pass

    @abstractmethod
    def authenticate(self) -> BWKSCommand:
        """Authenticates client with username and password in client"""
        pass

    @abstractmethod
    def _receive_response(self, response: str) -> BWKSCommand:
        """Receives response from requester and returns BWKSCommand"""
        pass
    
    def _set_up_dispatch_table(self):
        """Set up the dispatch table for the client"""
        # TODO: Set up dispatch table
        self._dispatch_table = {}

    def _set_up_logging(self):
        """Common logging setup for all APIs"""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.WARNING)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.WARNING)
        logger.addHandler(console_handler)
        
        return logger

class Client(BaseClient):
    """Connection to a BroadWorks server

    Args:
        host (str): URL or IP address of server. Depends on connection type.
        username (str): The username of the user
        password (str): The password of the user
        conn_type (str): Either 'TCP' or 'SOAP'. TCP is the default.
        user_agent (str): The user agent of the client, used for logging. Default is 'Thor\'s Hammer'. 
        timeout (int): The timeout of the client. Default is 30 seconds.
        logger (logging.Logger): The logger of the client. Default is None.

    Attributes:
        authenticated (bool): Whether the client is authenticated
        session_id (str): The session id of the client
        dispatch_table (dict): The dispatch table of the client

    Raises:
        Exception: If the client fails to authenticate
    """

    @property
    def async_mode(self) -> bool:
        return False

    def command(self, command: BWKSCommand) -> BWKSCommand:
        """
        Executes all requests to the server.
        If the client is not authenticated, it will authenticate first.

        Args:
            command (BWKSCommand): The command class to execute

        Returns:
            BWKSCommand: The response from the server
        """
        if not self.authenticated:
            self.authenticate()
        self.logger.info(f"Executing command: {command.__class__.__name__}")
        self.logger.debug(f"Command: {command.to_dict()}")
        response = self.requester.send_request(command.to_xml())
        return self._receive_response(response)

    def raw_command(self, command: str, **kwargs) -> BWKSCommand:
        """
        Executes raw command specified by end user - instantiates class command.

        Args:
            command (str): The command to execute
            **kwargs: The arguments to pass to the command

        Returns:
            BWKSCommand: The response from the server

        Raises:
            ValueError: If the command is not found in the dispatch table
        """
        command_class = self.dispatch_table.get(command)
        if not command_class:
            self.logger.error(f"Command {command} not found in dispatch table")
            raise ValueError(f"Command {command} not found in dispatch table")
        return self.command(command_class(**kwargs))

    def authenticate(self) -> BWKSCommand:
        """
        Authenticates client with username and password in client.

        Returns:
            BWKSCommand: The response from the server

        Raises:
            ValueError: If the command is not found in the dispatch table
        """
        if self.authenticated:
            return
        try: 
            auth_command = self.dispatch_table.get("AuthenticationRequest")
            auth_resp = self.command(auth_command(user_id=self.username))

            authhash = hashlib.sha1(self.password.encode()).hexdigest().lower()
            signed_password = (
                hashlib.md5(":".join([auth_resp.nonce, authhash]).encode())
                .hexdigest()
                .lower()
            )

            login_command = self.dispatch_table.get("LoginResponse22V5")
            login_resp = self.command(
                login_command(user_id=self.username, signed_password=signed_password)
            )
        except Exception as e:
            self.logger.error(f"Failed to authenticate: {e}")
            raise THError(f"Failed to authenticate: {e}")
        self.logger.info("Authenticated with server")
        self.authenticated = True
        return login_resp

    def _receive_response(self, response: str) -> BWKSCommand:
        """Receives response from requester and returns BWKSCommand"""
        return BWKSCommand.from_xml(response)

class AsyncClient(BaseClient):
    """Asycn version of Client.

    Note: Performs the same functions as Client, but in an asynchronous manner.

    Args:
        host (str): URL or IP address of server. Depends on connection type.
        username (str): The username of the user
        password (str): The password of the user
        conn_type (str): Either 'TCP' or 'SOAP'. TCP is the default.
        user_agent (str): The user agent of the client, used for logging. Default is 'Thor\'s Hammer'. 
        timeout (int): The timeout of the client. Default is 30 seconds.
        logger (logging.Logger): The logger of the client. Default is None.

    Attributes:
        authenticated (bool): Whether the client is authenticated
        session_id (str): The session id of the client
        dispatch_table (dict): The dispatch table of the client

    Raises:
        Exception: If the client fails to authenticate
    """

    @property
    def async_mode(self) -> bool:
        return True
    
    async def command(self, command: BWKSCommand) -> BWKSCommand:
        if not self.authenticated:
            await self.authenticate()
        self.logger.info(f"Executing command: {command.__class__.__name__}")
        self.logger.debug(f"Command: {command.to_dict()}")
        response = await self.requester.send_request(command.to_xml())
        return self._receive_response(response)

    async def raw_command(self, command: str, **kwargs) -> BWKSCommand:
        command_class = self.dispatch_table.get(command)
        if not command_class:
            self.logger.error(f"Command {command} not found in dispatch table")
            raise ValueError(f"Command {command} not found in dispatch table")
        response = await self.command(command_class(**kwargs))
        return response

    async def authenticate(self) -> BWKSCommand:
        if self.authenticated:
            return
        try:        
            auth_command = self.dispatch_table.get("AuthenticationRequest")
            auth_resp = await self.command(auth_command(user_id=self.username))

            authhash = hashlib.sha1(self.password.encode()).hexdigest().lower()
            signed_password = (
                hashlib.md5(":".join([auth_resp.nonce, authhash]).encode())
                .hexdigest()
                .lower()
            )

            login_command = self.dispatch_table.get("LoginResponse22V5")
            login_resp = await self.command(
                login_command(user_id=self.username, signed_password=signed_password)
            )
        except Exception as e:
            self.logger.error(f"Failed to authenticate: {e}")
            raise THError(f"Failed to authenticate: {e}")
        self.logger.info("Authenticated with server")
        self.authenticated = True
        return login_resp
    
    def _receive_response(self, response: str) -> BWKSCommand: #TODO: this needs flushing out
        """Receives response from requester and returns BWKSCommand"""
        return BWKSCommand.from_xml(response)