import logging
import attr
from abc import ABC, abstractmethod

from .commands.base_command import BroadworksCommand as BWKSCommand
from .requester import create_requester 

'''
TODO: 
- command()
- raw_command()
- authenticate()
- re_auth()
- SOAP or TCP
- Set up logging
- Set up requester
- Consider attributes and how they are passed in?
- async and sync
- Dispatch table
- create_client()
- command classes I think can be condensed with the use of command classes and dist table
'''

@attr.s(slots=True, kw_only=True)
class BaseClient(ABC):
    host: str = attr.ib()
    username: str = attr.ib()
    password: str = attr.ib()
    conn_type: str = attr.ib(default="TCP", validator=attr.validators.in_(["TCP", "SOAP"]))
    user_agent: str = attr.ib(default="Thor\'s Hammer")
    timeout: int = attr.ib(default=30)
    logger: logging.Logger = attr.ib(default=None)
    authenticated: bool = attr.id(default=False)

    def __attrs_post_init__(self):
        try: 
            self.authenticate()
            self._set_up_dispatch_table()
            self.logger = self.logger or self._set_up_logging()
            self.requester = create_requester(
                conn_type=self.conn_type,
                async_mode=self.async_mode,
                host=self.host,
                timeout=self.timeout,
                logger=self.logger
            )
        except Exception as e:
            print(f"Failed to authenticate {e}")
            raise Exception #TODO: Handle better
    
    @property
    @abstractmethod
    def async_mode(self) -> bool:
        pass

    @abstractmethod
    def authenticate(self):
        """Authenticates client with username and password in client"""
        pass

    @abstractmethod
    def command(self, command: BWKSCommand) -> BWKSCommand:
        """Executes command class from .commands lib"""
        pass
    
    @abstractmethod
    def raw_command(self, command: str, **kwargs) -> BWKSCommand:
        """Executes raw command specified by end user - instantiates class command"""
        pass
    
    def _set_up_dispatch_table(self):
        """Set up the dispatch table for the client"""
        self.dispatch_table = {}

    def _set_up_logging(self):
        """Common logging setup for all APIs"""
        logger = logging.getLogger(f"{self.__name__}")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
             "timestamp: %(asctime)s, level: %(levelname)s, module: %(module)s, function: %(funcName)s,  message: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger

class Client(BaseClient):

    @property
    @abstractmethod
    def async_mode(self) -> bool:
        return False
    
    def authenticate(self):
        # instan a authcommand
        # call slef.r with to_xml
        pass

    def command(self):
        # call class to_xml
        # pass to requester.send_request()
        pass

    def raw_command(self):
        # get raw command
        # init command class
        # call command()
        pass


class AsyncClient(BaseClient):

    @property
    @abstractmethod
    def async_mode(self) -> bool:
        return True
    
    async def authenticate(self):
        pass

    async def command(self):
        pass

    async def raw_command(self):
        pass
