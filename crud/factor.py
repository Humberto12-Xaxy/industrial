from sqlalchemy.orm import Session

from models.factor import Factor
from schemas.factor import CreateFactor


def get_factors(db: Session):
    return db.query(Factor).all()
def create_factor(db: Session, factor: CreateFactor):
    db_factor = Factor(**factor.model_dump())
    print(db_factor)
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor