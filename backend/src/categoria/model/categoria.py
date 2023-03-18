from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class CategoriaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descripcion: str = Field(...)
    edad_minima: int = Field(...)
    edad_maxima: int = Field(...)
    competicion_id: PyObjectId = Field(...)
    torneo_id: PyObjectId = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
