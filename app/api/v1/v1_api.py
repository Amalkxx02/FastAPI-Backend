from fastapi import APIRouter
from .Authentication.api import router as Authentication_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(Authentication_router)