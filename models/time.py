from sqlalchemy import Column, ForeignKey, Integer, String, Float
from db.connection import Base

class Time(Base):
    __tablename__ = "tiempos"

    id = Column(Integer, primary_key=True, index=True)
    duracion = Column(Float)
    mano = Column(String)
    idActividad = Column(Integer, ForeignKey("actividades.id"))