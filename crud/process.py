from sqlalchemy.orm import Session

from models.process import Process
from schemas.process import ProcessCreate 

from crud.activity import create_activity

def getProcess(db: Session):
    process =  db.query(Process).all()
    serialized_process = []
    for p in process:
        if not p.is_done:
            process_dict = p.as_dict()
            activities_dict = [a.as_dict() for a in p.activities]
            process_dict['activities'] = activities_dict
            serialized_process.append(process_dict)
    return serialized_process

def create_process(db: Session, process: ProcessCreate):
    list_activities = []
    create = {
        'nombre' : process.name,
        'descripcion' : process.description,
        'is_done' : process.id_done
    }
    activities = process.activities

    process = Process(**create)
    db.add(process)
    db.commit()
    db.refresh(process)

    print(
        process.id
    )

    for activity in activities:
        getactivity = create_activity(db, activity, process.id)
        final_activity = {
            'id' : getactivity.id,
            'nombre' : getactivity.nombre,
            'ciclos' : getactivity.ciclos,
            'idproceso' : getactivity.idproceso
        }

        list_activities.append(final_activity)

    response = {
        'id' : process.id,
        'nombre' : process.nombre,
        'descripcion' : process.descripcion,
        'actividades' : list_activities
    }

    return response