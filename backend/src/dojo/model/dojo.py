from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class DojoModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nombre: str = Field(...)
    nombre_sensei: str = Field(...)
    apellido_sensei: str = Field(...)
    ruta_logo: str = Field(...)
    token_url: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
