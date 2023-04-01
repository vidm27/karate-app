from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class CategoriaCinturonModel(BaseModel):
    cinturon_id: PyObjectId
    nombre: str


class Puntaje(BaseModel):
    valor: float
    arbitro: str


class CategoriaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    age_min: int
    age_max: int
    cinturones: list[CategoriaCinturonModel] = []
    competicion_id: PyObjectId
    torneo_id: PyObjectId

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateCategoriaModel(BaseModel):
    name: Optional[str]
    age_min: Optional[int]
    age_max: Optional[int]
    cinturones: Optional[list[CategoriaCinturonModel]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CategoriaCompetidorModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    categoria_id: PyObjectId
    competidor_id: PyObjectId
    puntajes: Optional[list[Puntaje]]
    ronda: int = 1
    posicion: Optional[int]


class UpdateCategoriaCompetidorModel(BaseModel):
    categoria_id: PyObjectId
    puntajes: Optional[list[Puntaje]]
    ronda: int = 1
    posicion: Optional[int]
