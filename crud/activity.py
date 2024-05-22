from sqlalchemy.orm import Session

from models.activity import Activity
from schemas.activity import CreateActivity

def get_activities(db: Session):
    return db.query(Activity).all()

def create_activity(db: Session, activity: CreateActivity, id_process: int):
    get_activity = Activity(**activity.model_dump(), idproceso=id_process)
    db.add(get_activity)
    db.commit()
    db.refresh(get_activity)
    return get_activity