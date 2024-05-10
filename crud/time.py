from sqlalchemy.orm import Session

from models.time import Time
from schemas.time import CreateTime

def create_time(db: Session, time: CreateTime):
    db_time = Time(**time.model_dump())
    db.add(db_time)
    db.commit()
    db.refresh(db_time)
    return db_time