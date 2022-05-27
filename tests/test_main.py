from unittest.mock import patch

from flask import Flask

from main import get_enums
from src.service.enum.service import EnumService
from tests.test_doubles.doubles import (
    main_service_response_dummy,
    main_response_dummy,
    main_service_response_when_invalid_params_dummy,
    main_response_when_invalid_params_dummy,
)


@patch.object(EnumService, "get_response")
def test_get_enums_when_params_are_ok(get_response_mock):
    get_response_mock.return_value = main_service_response_dummy
    app = Flask(__name__)
    with app.test_request_context("?country=USA").request as request:
        response = get_enums(request_=request)
        expected_response = main_response_dummy
        assert response.data == expected_response


@patch.object(EnumService, "get_response")
def test_get_enums_when_params_are_invalid(get_response_mock):
    get_response_mock.return_value = main_service_response_when_invalid_params_dummy
    app = Flask(__name__)
    with app.test_request_context("?country=").request as request:
        response = get_enums(request_=request)
        expected_response = main_response_when_invalid_params_dummy
        assert response.data == expected_response
