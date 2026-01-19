from fastapi import APIRouter

from .schemas import Authenticate

router = APIRouter(prefix="/auth",tags=["Authentication"])

OAUTH = "/oauth"
SIGN_OUT = "/sign-out"

SIGN_UP = "/sign-up"

@router.post(OAUTH)
async def sign_in(Auth:Authenticate):
    pass

