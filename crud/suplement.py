from sqlalchemy.orm import Session

from models.suplement import Suplement
from schemas.suplement import CreateSuplement

def get_suplements(db: Session):
    return db.query(Suplement).all()

def create_suplement(db: Session, suplement: CreateSuplement):
    db_suplement = Suplement(**suplement.dict())
    db.add(db_suplement)
    db.commit()
    db.refresh(db_suplement)
    return db_suplement