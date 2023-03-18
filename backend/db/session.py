import motor.motor_asyncio

from backend.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_DATABASE_URI)
db = client.karate
