from pydantic import BaseModel
from typing import List, Optional

from schemas.activity import CreateActivity


class ProcessBase(BaseModel):
    name : str
    description : str
    id_done : Optional[bool] = False

class ProcessCreate(ProcessBase):
    activities : List[CreateActivity]

class Process(ProcessBase):
    id : int
    activities : List[str]

    class Config:
        from_attributes = True


