"""
test client
"""
import pytest
from unittest.mock import patch, MagicMock

from src.thors_hammer.client import Client, AsyncClient

@pytest.fixture
def mock_auth():
    with patch("src.thors_hammer.client.BaseClient.authenticate") as mock:
        yield mock

@pytest.fixture
def mock_dispatch_table():
    class AuthenticationRequest(): 
        def __init__(self, user_id):
            self.user_id = user_id
    class LoginResponse22V5(): 
        def __init__(self, user_id, signed_password):
            self.user_id = user_id
            self.signed_password = signed_password
    return {"AuthenticationRequest": AuthenticationRequest, "LoginResponse22V5": LoginResponse22V5}

@pytest.fixture
def mock_dispatch(mock_dispatch_table):
    with patch("src.thors_hammer.client.BaseClient._set_up_dispatch_table", return_value=mock_dispatch_table) as mock:
        yield mock

@pytest.fixture
def mock_logging():
    with patch("src.thors_hammer.client.BaseClient._set_up_logging") as mock:
        yield mock

class TestClientSetup:
    def test_client_initialises_with_defaults(self, mock_auth, mock_dispatch, mock_logging):
        client = Client(host="localhost", username="user", password="pass")
        client._dispatch_table = mock_dispatch
        
        assert client.host == "localhost"
        assert client.username == "user"
        assert client.password == "pass"
        assert client.conn_type == "TCP"
        assert client.user_agent == "Thor's Hammer"
        assert client.timeout == 30
        assert not client.authenticated
        assert client.session_id is None