from http import HTTPStatus
from flask import request, Response, Request
from pathlib import Path

from src.infrastructure.env_config import Configuration

Configuration.get_config(
    env_path=Path(__file__).parent.absolute()
)  # This line is important to load the environment variables needed by the project!

from src.core.response_model.response_model import ResponseModel
from src.service.enum.service import EnumService


def get_enums(request_: Request = request) -> Response:
    service_response = EnumService.get_response(request_)
    response = ResponseModel.build_http_response(
        response_model=service_response, status=HTTPStatus.OK
    )
    return response
