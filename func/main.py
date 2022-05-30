from http import HTTPStatus
from pathlib import Path

from etria_logger import Gladsheim
from flask import request, Response, Request

from src.domain.response.status_code.enums import StatusCode
from src.domain.validators.state.validator import StateParams
from src.infrastructure.env_config import Configuration

Configuration.get_config(
    env_path=Path(__file__).parent.absolute()
)  # This line is important to load the environment variables needed by the project!

from src.domain.response.model import ResponseModel
from src.service.state_enum.service import StateEnumService


def get_enums(request_: Request = request) -> Response:
    parameters = request_.args.to_dict()

    try:
        parameters_validated = StateParams(**parameters)
        service_response = StateEnumService.get_response(parameters_validated)
        response = ResponseModel.build_http_response(
            response_model=service_response, status=HTTPStatus.OK
        )
        return response

    except TypeError:
        Gladsheim.error(error=TypeError(), message="Data not found or inconsistent.")
        response = ResponseModel.build_http_response(
            response_model=ResponseModel.build_response(
                success=False,
                code=StatusCode.DATA_NOT_FOUND,
                message="Data not found or inconsistent.",
                result=[],
            ),
            status=HTTPStatus.NOT_FOUND,
        )
        return response

    except Exception as error:
        Gladsheim.error(error=error, message="Error trying to get the enum.")
        response = ResponseModel.build_http_response(
            response_model=ResponseModel.build_response(
                success=False,
                code=StatusCode.DATA_NOT_FOUND,
                message="Error trying to get the enum.",
                result=[],
            ),
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
        return response
