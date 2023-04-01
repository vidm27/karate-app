from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class CompeticiaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    dt_created: Optional[datetime]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateCompeticiaModel(BaseModel):
    name: str
    dt_created: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
