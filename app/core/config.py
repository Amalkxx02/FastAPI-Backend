from pydantic_settings import BaseSettings

class Secrets(BaseSettings):
    #JWT_ALGORITHM:str
    #JWT_ACCESS_KEY:str
    #JWT_REFRESH_KEY:str
    FIREBASE_CRED:str
    MONGODB_URI:str

    model_config = {
        "env_file": ".env",
        "case_sensitive":True
    }

secrets = Secrets()