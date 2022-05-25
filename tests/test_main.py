from unittest.mock import patch

from main import get_enums
from src.service.enum.service import EnumService
from tests.test_doubles.doubles import main_service_response_dummy, main_response_dummy

service_response_dummy = main_service_response_dummy


@patch.object(EnumService, "get_response")
def test_when_response_return_response(get_response_mock):
    get_response_mock.return_value = service_response_dummy
    response = get_enums()
    expected_response = main_response_dummy
    assert response.data == expected_response
