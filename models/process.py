from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.connection import Base
from .activity import Activity
from .factor import Factor

class Process(Base):
    __tablename__ = "procesos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)
    is_done = Column(Boolean, default=False)
    activities = relationship(lambda: Activity)
    factors = relationship(lambda: Factor)

    def as_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}
