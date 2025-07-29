import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from thors_hammer.requester import SyncTCPRequester
from thors_hammer.exceptions import THErrorSocketInitialisation, THErrorSocketTimeout


@pytest.fixture
def mock_logger():
    return Mock()


@pytest.fixture
def mock_command():
    cmd = Mock()
    cmd.encode.return_value = b"""
<BroadsoftDocument xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <command xmlns="" xsi:type="LoginRequest22V5"></command>
</BroadsoftDocument>
"""
    return cmd


class TestSyncTCPRequester:
    @patch("socket.create_connection")
    @patch("ssl.create_default_context")
    def test_init_and_connect_ssl_success(
        self, mock_ssl_context, mock_create_connection, mock_logger
    ):
        mock_socket = Mock()
        mock_create_connection.return_value = mock_socket

        mock_ssl = Mock()
        mock_ssl.wrap_socket.return_value = "wrapped_socket"
        mock_ssl_context.return_value = mock_ssl

        requester = SyncTCPRequester(
            logger=mock_logger, host="localhost", port=2209, tls=True
        )
        result = requester.connect()

        assert requester.sock == "wrapped_socket"
        mock_create_connection.assert_called_once_with(("localhost", 2209), timeout=30)
        mock_ssl.wrap_socket.assert_called_once_with(
            mock_socket, server_hostname="localhost"
        )
        mock_logger.info.assert_called()
        assert result is None

    @patch("socket.create_connection")
    @patch("ssl.create_default_context")
    def test_connect_ssl_failure(
        self, mock_ssl_context, mock_create_connection, mock_logger
    ):
        mock_create_connection.side_effect = Exception("Failed to connect")

        requester = SyncTCPRequester(
            logger=mock_logger, host="localhost", port=2209, tls=True
        )
        result = requester.connect()

        assert requester.sock is None
        assert isinstance(result, tuple)
        assert result[0] == THErrorSocketInitialisation
        mock_logger.error.assert_called()

    @patch("select.select")
    def test_send_request_success(self, mock_select, mock_logger, mock_command):
        with patch("socket.create_connection"), patch("ssl.create_default_context"):
            mock_socket = Mock()
            mock_socket.recv.side_effect = mock_socket.recv.side_effect = [
                b"<BroadsoftDocument xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>",
                b"<command xmlns='' xsi:type='LoginRequest22V5'></command>",
                b"</BroadsoftDocument>",
            ]
            mock_select.return_value = ([mock_socket], [], [])

            requester = SyncTCPRequester(
                logger=mock_logger, host="localhost", port=2209, tls=True
            )
            requester.sock = mock_socket

            result = requester.send_request(mock_command)

            assert isinstance(result, str)
            assert "</BroadsoftDocument>" in result
            mock_socket.sendall.assert_called()
            mock_select.assert_called_with([mock_socket], [], [], 30)
            mock_socket.recv.assert_called()

    @patch("select.select")
    def test_send_request_timeout(self, mock_select, mock_logger, mock_command):
        with patch("socket.create_connection"), patch("ssl.create_default_context"):
            mock_select.return_value = ([], [], [])  # simulate timeout

            requester = SyncTCPRequester(
                logger=mock_logger, host="localhost", port=2209, tls=True
            )
            requester.sock = Mock()

            result = requester.send_request(mock_command)

            assert isinstance(result, tuple)
            assert result[0] == THErrorSocketTimeout
