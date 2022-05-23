from etria_logger import Gladsheim
from flask import Request

from src.core.interfaces.service.enum.interface import IEnumService
from src.repository.enum.repository import EnumRepository
from src.core.response_model.response_model import ResponseModel
from src.core.status_codes.code_enums import StatusCode


class EnumService(IEnumService):
    @classmethod
    def get_response(cls, request: Request):
        service_response = []

        country = request.args.get("country")
        there_are_parameters = bool(country)
        if not there_are_parameters:
            service_response = ResponseModel.build_response(
                success=False,
                code=StatusCode.INVALID_PARAMS,
                message="Bad request. Incorrect or invalid parameters.",
                result=service_response
            )
            return service_response

        enums = EnumRepository.get_enums(country)

        try:
            for code, value in enums:
                service_response.append(
                    {
                        "code": code,
                        "value": value
                    }
                )
        except TypeError:
            Gladsheim.error(error=TypeError(), message='Data not found or inconsistent.')
            service_response = ResponseModel.build_response(
                success=False,
                code=StatusCode.DATA_NOT_FOUND,
                message='Data not found or inconsistent.',
                result=[]
            )
            return service_response

        except Exception as error:
            Gladsheim.error(error=error, message='Error trying to get the enum.')
            service_response = ResponseModel.build_response(
                success=False,
                code=StatusCode.DATA_NOT_FOUND,
                message='Error trying to get the enum.',
                result=[]
            )
            return service_response

        service_response = ResponseModel.build_response(
            success=True,
            code=StatusCode.SUCCESS,
            message=None,
            result=service_response
        )
        return service_response
