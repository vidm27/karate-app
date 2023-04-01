from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class CompetidorModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    lastname: str
    age: int
    gender: str
    cinturon_id: PyObjectId

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateCompetidorModel(BaseModel):
    name: Optional[str]
    lastname: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    cinturon_id: Optional[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
