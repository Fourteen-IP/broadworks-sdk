# this will be resposnsible for sending and receiving data from the API

class Requester:
    pass

def create_requester(
    conn_type,
    async_mode,
    host,
    timeout,
    logger,
    session_id
):
    return 