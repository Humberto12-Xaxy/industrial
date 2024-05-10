from sqlalchemy import Column, Integer, String, ForeignKey
from db.connection import Base


class Activity(Base):
    __tablename__ = "actividades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    ciclos = Column(Integer)
    idProceso = Column(Integer, ForeignKey("procesos.id"))


    def __str__(self):
        return f'id: {self.id}, nombre: {self.nombre}, ciclos: {self.ciclos}, idProceso: {self.idProceso}'