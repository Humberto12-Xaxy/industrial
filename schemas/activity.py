from pydantic import BaseModel


class ActivityBase(BaseModel):
    nombre : str
    ciclos : int

class CreateActivity(ActivityBase):
    pass

class Activity(ActivityBase):
    id : int
    idProceso : int

    class Config:
        from_attributes = True
