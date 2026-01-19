from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.mongodb.mongodb import client, connect_to_mongodb


@asynccontextmanager
async def server_life(app: FastAPI):
    connect_to_mongodb()
    yield
    if client:
        client.close()
