from fastapi import APIRouter
from .v1.v1_api import router_v1

router = APIRouter(prefix="/app")

router.include_router(router_v1)