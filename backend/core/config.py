import secrets
from typing import List, Optional, Dict, Any

from pydantic import BaseSettings, MongoDsn, AnyHttpUrl, validator


# export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

class Setttigns(BaseSettings):
    API_V1_STR: str = "/api"
    SECRET_KEY: str = secrets.token_urlsafe(23)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List
    PROJECT_NAME: str

    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str
    MONGO_PORT: str
    MONGO_HOST: str
    MONGO_QUERY: str
    MONGO_DATABASE_URI: Optional[MongoDsn] = None

    @validator("MONGO_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict) -> Any:
        if isinstance(v, str):
            return v
        return MongoDsn.build(
            scheme="mongodb",
            user=values.get("MONGO_USERNAME"),
            password=values.get("MONGO_PASSWORD"),
            host=values.get("MONGO_HOST"),
            port=values.get("MONGO_PORT"),
            path=values.get("MONGO_DATABASE"),
            query=values.get("MONGO_QUERY")
        )

    class Config:
        case_sensitive = True


settings = Setttigns(
    SERVER_HOST="http://127.0.0.1",
    SERVER_NAME="Karate Jion App",
    PROJECT_NAME="Karate Jion App",
    MONGO_USERNAME="karate",
    MONGO_PASSWORD="karate",
    MONGO_DATABASE="/karate",
    MONGO_PORT="27017",
    MONGO_HOST="127.0.0.1",
    MONGO_QUERY="authSource=admin",
    BACKEND_CORS_ORIGINS=["*"]
)
