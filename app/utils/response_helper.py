from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def response_helper(
    status_code: int,
    message: str,
    error: str = None,
    description: str = None,
    data: dict = None,
):
    if data is None:
        data = {}

    result = {"status_code": status_code, "message": message, "data": data}

    if error:
        result["error"] = error
    if description:
        result["description"] = description
    return JSONResponse(jsonable_encoder(result), status_code)
