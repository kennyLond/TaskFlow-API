from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.db.database import Base

class  User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)