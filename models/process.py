from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base
from .activity import Activity
from .factor import Factor

class Process(Base):
    __tablename__ = "procesos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    activities = relationship(lambda: Activity)
    factors = relationship(lambda: Factor)

    def as_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}
