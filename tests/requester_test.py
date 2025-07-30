import pytest
from unittest.mock import Mock, patch, AsyncMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from broadworks_sdk.requester import (
    SyncTCPRequester,
    SyncSOAPRequester,
    AsyncSOAPRequester,
    AsyncTCPRequester,
)
from broadworks_sdk.exceptions import (
    THErrorSocketInitialisation,
    THErrorSocketTimeout,
    THErrorClientInitialisation,
    THErrorSendRequestFailed,
)
from broadworks_sdk.commands import base_command as BroadworksCommand


@pytest.fixture
def mock_logger():
    return Mock()


@pytest.fixture
def mock_command():
    cmd = Mock()
    cmd.encode.return_value = b"""
<BroadsoftDocument xmlns:xsi="http://www.w3.org/2001/XMLSchema-requester">
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
                b"<BroadsoftDocument xmlns:xsi='http://www.w3.org/2001/XMLSchema-requester'>",
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


class TestSyncSOAPRequester:
    @patch("broadworks_sdk.requester.requests.sessions.Session")
    @patch("broadworks_sdk.requester.Settings")
    @patch("broadworks_sdk.requester.Transport")
    @patch("broadworks_sdk.requester.Client")
    def test_connect_success(
        self, mock_client_class, mock_transport, mock_settings, mock_session
    ):
        mock_logger = Mock()
        requester = SyncSOAPRequester(logger=mock_logger, host="localhost", port=2209)

        assert requester.client is not None
        assert requester.zclient is not None
        mock_logger.info.assert_called_once_with(
            "Initiated socket on SyncSOAPRequester: localhost:2209"
        )

    @patch(
        "broadworks_sdk.requester.requests.sessions.Session",
        side_effect=Exception("Session error"),
    )
    def test_connect_fail(self, mock_session):
        mock_logger = Mock()
        requester = SyncSOAPRequester.__new__(SyncSOAPRequester)
        requester.logger = mock_logger
        requester.host = "localhost"
        requester.port = 2209
        requester.timeout = 10
        requester.client = None

        result = requester.connect()

        assert isinstance(result, tuple)
        assert result[0] == THErrorClientInitialisation
        assert isinstance(result[1], Exception)
        mock_logger.error.assert_called_once()
        mock_logger.info.assert_not_called()

    def test_disconnect_closes_session(self):
        mock_logger = Mock()
        mock_client = Mock()

        requester = SyncSOAPRequester.__new__(SyncSOAPRequester)
        requester.logger = mock_logger
        requester.client = mock_client

        requester.disconnect()

        mock_client.close.assert_called_once()
        assert requester.client is None

    def test_disconnect_handles_exception(self):
        mock_logger = Mock()
        bad_client = Mock()
        bad_client.close.side_effect = Exception("close failed")

        requester = SyncSOAPRequester.__new__(SyncSOAPRequester)
        requester.logger = mock_logger
        requester.client = bad_client

        requester.disconnect()

        mock_logger.warning.assert_called_once()
        assert requester.client is None

    @patch.object(SyncSOAPRequester, "build_oci_xml", return_value="<xml>request</xml>")
    def test_send_request_success(self, mock_build_xml):
        mock_logger = Mock()
        mock_zclient = Mock()
        mock_service = Mock()
        mock_service.processOCIMessage.return_value = "response"
        mock_zclient.service = mock_service

        requester = SyncSOAPRequester.__new__(SyncSOAPRequester)
        requester.logger = mock_logger
        requester.zclient = mock_zclient

        mock_command = Mock(spec=BroadworksCommand)

        response = requester.send_request(mock_command)

        mock_build_xml.assert_called_once_with(mock_command)
        mock_service.processOCIMessage.assert_called_once()
        assert response == "response"

    @patch.object(
        SyncSOAPRequester, "build_oci_xml", side_effect=Exception("build failed")
    )
    def test_send_request_fail(self, mock_build_xml):
        mock_logger = Mock()
        requester = SyncSOAPRequester.__new__(SyncSOAPRequester)
        requester.logger = mock_logger
        requester.zclient = Mock()

        mock_command = Mock(spec=BroadworksCommand)

        result = requester.send_request(mock_command)

        assert isinstance(result, tuple)
        assert result[0] == THErrorSendRequestFailed
        assert isinstance(result[1], Exception)
        mock_logger.error.assert_called_once()


@pytest.mark.asyncio
class TestAsyncTCPRequester:
    async def test_send_request_success(self):
        mock_logger = Mock()

        async def fake_command():
            return "mocked_command"

        mock_command = fake_command()

        requester = AsyncTCPRequester.__new__(AsyncTCPRequester)
        requester.logger = mock_logger
        requester.host = "localhost"
        requester.port = 2209
        requester.timeout = 10
        requester.session_id = None

        requester.reader = AsyncMock()
        requester.writer = AsyncMock()
        requester.writer.drain = AsyncMock()
        requester.reader.read = AsyncMock(
            side_effect=[b"<data></BroadsoftDocument>", b""]
        )

        with patch.object(requester, "build_oci_xml", return_value=b"<mocked-xml>"):
            result = await requester.send_request(mock_command)

            assert isinstance(result, str)
            assert "data" in result
            requester.writer.write.assert_called_once()
            requester.writer.drain.assert_called_once()


@pytest.mark.asyncio
class TestAsyncSOAPRequester:
    async def test_send_request_success(self):
        mock_logger = Mock()

        async def fake_command():
            return "mocked_command"

        mock_command = fake_command()

        requester = AsyncSOAPRequester.__new__(AsyncSOAPRequester)
        requester.logger = mock_logger
        requester.host = "localhost"
        requester.port = 2209
        requester.timeout = 10
        requester.session_id = None

        requester.async_client = Mock()
        requester.wsdl_client = Mock()
        requester.zeep_client = Mock()
        requester.zeep_client.service.processOCIMessage = AsyncMock(
            return_value="soap response"
        )

        with patch.object(requester, "build_oci_xml", return_value=b"<mocked-xml>"):
            result = await requester.send_request(mock_command)

            assert result == "soap response"
            requester.zeep_client.service.processOCIMessage.assert_called_once()
