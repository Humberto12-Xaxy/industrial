from sqlalchemy.orm import Session

from sqlalchemy.orm.state import InstanceState

import json

from models.process import Process
from schemas.process import ProcessCreate 

from crud.activity import create_activity

def serialize_instance(obj):
    if isinstance(obj, InstanceState):
        return None
    return obj

def getProcess(db: Session):
    process =  db.query(Process).all()
    serialized_process = [p.as_dict() for p in process]
    return serialized_process

def create_process(db: Session, process: ProcessCreate):
    list_activities = []
    create = {
        'nombre' : process.name,
        'descripcion' : process.description
    }
    activities = process.activities

    process = Process(**create)
    db.add(process)
    db.commit()
    db.refresh(process)

    for activity in activities:
        getactivity = create_activity(db, activity, process.id)
        final_activity = {
            'id' : getactivity.id,
            'nombre' : getactivity.nombre,
            'ciclos' : getactivity.ciclos,
            'idProceso' : getactivity.idProceso
        }

        list_activities.append(final_activity)

    response = {
        'id' : process.id,
        'nombre' : process.nombre,
        'descripcion' : process.descripcion,
        'actividades' : list_activities
    }

    return response