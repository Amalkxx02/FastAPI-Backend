
from fastapi import Request,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

class ExceptionHelper(Exception):
    def __init__(
        self,
        status_code: int,
        error: str,
        message: str,
        data: dict | None = None,
        **kwargs,
    ):
        self.status_code = status_code
        self.error = error
        self.message = message
        self.data = data or {}
        self.extra = kwargs

async def custom_exception_handler(request: Request, exc: ExceptionHelper):
    content = {
        "status_code": exc.status_code,
        "error": exc.error,
        "message": exc.message,
        "data": exc.data,
        **exc.extra,
    }
    return JSONResponse(status_code=exc.status_code, content=content)


async def custom_validation_error_handler(
    request: Request, exc: RequestValidationError
):
    response_status = status.HTTP_422_UNPROCESSABLE_CONTENT
    content = {
        "status_code": response_status,
        "error": "Validation Error",
        "message": "The data provided is invalid or missing.",
        "data": exc.errors(),
    }
    return JSONResponse(status_code=response_status, content=content)

def setup_exception_handlers(app):
    app.add_exception_handler(ExceptionHelper,custom_exception_handler)
    app.add_exception_handler(RequestValidationError,custom_validation_error_handler)