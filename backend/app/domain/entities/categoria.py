from enum import Enum
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from backend.db.py_object import PyObjectId


class Cinturon(str, Enum):
    BLANCO = "blanco"
    AMARILLO = "amarillo"
    ANARANJADO = "anaranjado"
    VERDE = "verde"
    MORADO = "morado"
    CHOCOLATE = "chocolate"
    NEGRO = "negro"


class CategoriaCinturonModel(BaseModel):
    name: Cinturon


class Puntaje(BaseModel):
    valor: float
    arbitro: str


class CategoriaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    age_min: int
    age_max: int
    cinturones: list[Cinturon] = []
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
