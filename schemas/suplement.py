from pydantic import BaseModel

class SuplementBase(BaseModel):
    necesidades : float
    fatiga : float
    depie : float
    postura : float
    fuerza : float

class CreateSuplement(SuplementBase):
    idproceso : int


class Suplement(SuplementBase):
    id : int
    idproceso : int

    class Config:
        from_attributes = True