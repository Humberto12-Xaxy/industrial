from sqlalchemy.orm import Session

from models.activity import Activity
from schemas.activity import CreateActivity

def get_activities(db: Session):
    return db.query(Activity).all()

def create_activity(db: Session, activity: CreateActivity, id_process: int):
    activity = Activity(**activity.model_dump(), idProceso=id_process)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity