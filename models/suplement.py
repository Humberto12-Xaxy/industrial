from sqlalchemy import Column, Integer, ForeignKey, Float
from db.connection import Base


class Suplement(Base):
    __tablename__ = "suplementos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    necesidades = Column(Float)
    fatiga = Column(Float)
    depie = Column(Float)
    postura = Column(Float)
    fuerza = Column(Float)
    idproceso = Column(Integer, ForeignKey("procesos.id"))