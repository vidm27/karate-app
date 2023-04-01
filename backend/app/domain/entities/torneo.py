from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class TorneoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    dt_created: Optional[datetime]
    dt_schedule: Optional[datetime]
    dojo_id: Optional[PyObjectId]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateTorenoModel(BaseModel):
    name: str
    dt_created: Optional[datetime]
    dt_schedule: Optional[datetime]
    dojo_id: Optional[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
