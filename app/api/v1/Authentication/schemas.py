from pydantic import BaseModel, model_validator
from fastapi import status
from app.utils.exception_helper import ExceptionHelper
from typing import Optional
from enum import Enum


class AuthType(str, Enum):
    GOOGLE = "google"
    APPLE = "apple"
    EMAIL = "email"


class Authenticate(BaseModel):
    auth_type: AuthType
    email: Optional[str] = "user@example.com"
    password: Optional[str] = "Strong_pass_007"

    @model_validator(mode="after")
    def validate_email_and_password(self):
        if self.auth_type == AuthType.EMAIL:
            if not self.email:
                raise ExceptionHelper(
                    status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                    error="Needed a valid Email",
                    message="Please provide a valid email"
                )
            password = self.password  # need to provide proper validation
            if not password:
                raise ExceptionHelper(
                    status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                    error="Needed a valid Password",
                    message="Please provide a strong password"
                )
        return self
