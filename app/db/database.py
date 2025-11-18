from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

meta_data = MetaData()
Base = declarative_base()


try:
    with engine.connect() as connection:
        print("successful connecton to database")
except Exception as e:
    print("not connected to database")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()