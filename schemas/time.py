from pydantic import BaseModel
from typing import List

class TimeBase(BaseModel):
    duracion : float
    mano : str

class CreateTime(TimeBase):
    idActividad : int

class CreateVeryTime(BaseModel):
    tiempos : List[CreateTime]

class Time(TimeBase):
    id : int
    idActividad : int

    class Config:
        from_attributes = True