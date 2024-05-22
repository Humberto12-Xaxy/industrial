from pydantic import BaseModel

class FactorBase(BaseModel):
    habilidad : float
    esfuerzo : float
    condiciones : float
    consistencia : float

class CreateFactor(FactorBase):
    idproceso : int


class Factor(FactorBase):
    id : int
    idproceso : int

    class Config:
        from_attributes = True