from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://user.javafx:Suriano0726@localhost:3307/industrial"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessinLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()