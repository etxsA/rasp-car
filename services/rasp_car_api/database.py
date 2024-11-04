# Database Connection and Setup with SQLAlchemy
# rasp_car_api/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:toor@localhost:3306/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Return a database dependecy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()