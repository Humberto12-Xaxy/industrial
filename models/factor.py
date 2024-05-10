from sqlalchemy import Column, Integer, Float, ForeignKey
from db.connection import Base



class Factor(Base):
    __tablename__ = "factorcalificacion"

    id = Column(Integer, primary_key=True, index=True)
    habilidad = Column(Float)
    esfuerzo = Column(Float)
    condiciones = Column(Float)
    consistencia = Column(Float)
    idProceso = Column(Integer, ForeignKey("procesos.id"))
