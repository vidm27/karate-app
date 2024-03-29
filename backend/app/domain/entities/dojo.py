from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class DojoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    sensei_name: str
    sensei_lastname: str
    path_logo: str
    token_url: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateDojoModel(BaseModel):
    name: Optional[str]
    sensei_name: Optional[str]
    sensei_lastname: Optional[str]
    path_logo: Optional[str]
    token_url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
