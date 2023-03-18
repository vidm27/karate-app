from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class CinturonModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nombre: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
