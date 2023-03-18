from datetime import datetime, date

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class TorneoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nombre: str = Field(...)
    fecha_creacion: datetime = Field(...)
    inicio_evento: date = Field(...)
    final_evento: date = Field(...)
    dojo_id: PyObjectId = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
