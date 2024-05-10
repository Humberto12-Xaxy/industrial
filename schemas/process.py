from pydantic import BaseModel
from typing import List

from schemas.activity import CreateActivity


class ProcessBase(BaseModel):
    name : str
    description : str

class ProcessCreate(ProcessBase):
    activities : List[CreateActivity]

class Process(ProcessBase):
    id : int
    activities : List[str]

    class Config:
        from_attributes = True


