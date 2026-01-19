from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.core_api import router
from app.utils.exception_helper import setup_exception_handlers
from app.utils.main_utils import server_life

app = FastAPI(
    title="sample project",
    version="v1",
    lifespan=server_life
)

setup_exception_handlers(app)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)


@app.get("/")
def root():
    return {"message": "HELLO FROM SERVER!!!"}
