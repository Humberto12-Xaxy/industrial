from pydantic import BaseModel

class SuplementBase(BaseModel):
    necesidades : float
    fatiga : float
    dePie : float
    postura : float
    fuerza : float

class CreateSuplement(SuplementBase):
    idProceso : int


class Suplement(SuplementBase):
    id : int
    idProceso : int

    class Config:
        from_attributes = True