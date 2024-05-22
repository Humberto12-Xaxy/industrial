from sqlalchemy import Column, Integer, String, ForeignKey
from db.connection import Base


class Activity(Base):
    __tablename__ = "actividades"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    ciclos = Column(Integer)
    idproceso = Column(Integer, ForeignKey("procesos.id"))


    def __str__(self):
        return f'id: {self.id}, nombre: {self.nombre}, ciclos: {self.ciclos}, idProceso: {self.idProceso}'
    
    def as_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}
