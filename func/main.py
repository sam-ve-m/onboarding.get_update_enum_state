from http import HTTPStatus
from pathlib import Path

from flask import request, Response, Request

from src.core.status_codes.code_enums import StatusCode
from src.core.validator.validator import StateParams
from src.infrastructure.env_config import Configuration

Configuration.get_config(
    env_path=Path(__file__).parent.absolute()
)  # This line is important to load the environment variables needed by the project!

from src.core.response_model.response_model import ResponseModel
from src.service.enum.service import EnumService


def get_enums(request_: Request = request) -> Response:
    parameters = request_.args.to_dict()

    try:
        parameters_validated = StateParams(**parameters)
        service_response = EnumService.get_response(parameters_validated)

    except ValueError:
        service_response = ResponseModel.build_response(
            success=False,
            code=StatusCode.INVALID_PARAMS,
            message="Bad request. Incorrect or invalid parameters.",
            result=[],
        )

    response = ResponseModel.build_http_response(
        response_model=service_response, status=HTTPStatus.OK
    )
    return response
