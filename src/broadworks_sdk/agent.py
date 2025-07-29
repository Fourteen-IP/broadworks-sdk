# Overlap but different from bulker this is resposonible for scripts and reporting.
# Where bulker and agent differ is bulker only tackles bulk builing bwks entities, agent pulls info and upates them.

from broadworks_sdk.client import BaseClient


class Agent:
    __instance = None

    @staticmethod
    def get_instance(Client: BaseClient = None) -> "Agent":
        """
        Singleton implementation for Agent object.

        Args:
            Client (Client): Client object to be used in the scripts.
        """
        if Agent.__instance is None:
            Agent.__instance = Agent(Client)
        return Agent.__instance

    def __init__(
        self,
        Client: BaseClient,
    ) -> None:
        if Agent.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.Client = Client
