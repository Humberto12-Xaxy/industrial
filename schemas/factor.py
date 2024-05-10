from pydantic import BaseModel

class FactorBase(BaseModel):
    habilidad : float
    esfuerzo : float
    condiciones : float
    consistencia : float

class CreateFactor(FactorBase):
    idProceso : int


class Factor(FactorBase):
    id : int
    idProceso : int

    class Config:
        from_attributes = True