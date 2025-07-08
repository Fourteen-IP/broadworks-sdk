# Overlap but different from bulker this is resposonible for scripts and reporting. 
# Where bulker and agent differ is bulker only tackles bulk builing bwks entities, agent pulls info and upates them.


from .api import API


class Agent:

    __instance = None

    @staticmethod
    def get_instance(api: API = None) -> "Agent":
        """
        Singleton implementation for Agent object.

        Args:
            api (API): API object to be used in the scripts.
        """
        if Agent.__instance is None:
            Agent.__instance = Agent(api)
        return Agent.__instance

    def __init__(
        self,
        api: API,
    ) -> None:
        if Agent.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.api = api

    