from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://industrial:ovunLm6NysKIy1ukEnXZxm3V8RDLm4WC@dpg-cp2pg821hbls7382dokg-a.oregon-postgres.render.com/estudio_tiempos"
SQLALCHEMY_DATABASE_URL2 = "mysql://user.javafx:Suriano0726@localhost:3307/industrial"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessinLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()