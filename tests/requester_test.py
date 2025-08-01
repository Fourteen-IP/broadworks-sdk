import pytest
from unittest.mock import Mock, patch

from broadworks_sdk.requester.SyncTCPRequester import SyncTCPRequester


@pytest.fixture
def mock_logger():
    return Mock()


@pytest.fixture
def mock_command():
    cmd = Mock()
    cmd.encode.return_value = (
        b'<command xmlns="" xsi:type="LoginRequest22V4"></command>"'
    )
    return cmd


@patch("thors_hammer.requester.SyncTCPRequester.socket.create_connection")
@patch("thors_hammer.requester.SyncTCPRequester.ssl.create_default_context")
def test_init_and_connect_ssl_success(self, mock_ssl_context, mock_create_connection):
    mock_logger = Mock()
    requester = SyncTCPRequester("localhost", 2209, ssl=True, logger=mock_logger)

    mock_socket = Mock()
    mock_create_connection.return_value = mock_socket

    mock_ssl = Mock()
    mock_ssl.wrap_socket.return_value = "wrapped_socket"
    mock_ssl_context.return_value = mock_ssl

    result = requester.connect()

    assert requester.sock == "wrapped_socket"
    mock_create_connection.assert_called_once_with(("localhost", 2209), timeout=10)
    mock_ssl.wrap_socket.assert_called_once_with(
        mock_socket, server_hostname="localhost"
    )
    mock_logger.info.assert_called()
    assert result is None


@patch("select.select")
def test_send_request_success(self, mock_select, mock_logger, mock_command):
    with patch("socket.create_connection"), patch("ssl.create_default_context"):
        pass


def test_send_request_timeout(self, mock_logger, mock_command):
    with patch("socket.create_connection"), patch("ssl.create_default_context"):
        pass
