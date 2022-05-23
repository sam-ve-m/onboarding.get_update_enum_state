
# main tests

main_service_response_dummy = '{"result": [{"code": 1, "value": "BRASILEIRO NATO"}, {"code": 2, "value": "BRASILEIRO NATURALIZADO"}, {"code": 3, "value": "ESTRANGEIRO"}], "message": null, "success": true, "code": 0}'
main_response_dummy = main_service_response_dummy.encode()

# src.service.enum.service tests

enum_service_get_enums_response_ok = [(1, 'BRASILEIRO NATO'), (2, 'BRASILEIRO NATURALIZADO'), (3, 'ESTRANGEIRO')]
enum_service_response_ok = '{"result": [{"code": 1, "value": "BRASILEIRO NATO"}, {"code": 2, "value": "BRASILEIRO NATURALIZADO"}, {"code": 3, "value": "ESTRANGEIRO"}], "message": null, "success": true, "code": 0}'
enum_service_get_enums_response_none = None
enum_service_response_none = '{"result": [], "message": "Data not found or inconsistent.", "success": false, "code": 99}'
enum_service_get_enums_response_invalid = [(1)]
enum_service_response_invalid = '{"result": [], "message": "Error trying to get the enum.", "success": false, "code": 99}'


