from pymongo import AsyncMongoClient
from app.core.config import secrets

client: AsyncMongoClient = None

def connect_to_mongodb():
    global client
    client = AsyncMongoClient(secrets.MONGODB_URI)

def mongodb_client()->AsyncMongoClient:
    return client