from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user_models import User
from app.schemas.schemas_user import UserCreate
from app.auth.jwt_handler import create_access_token
import bcrypt

def register_user_service(data: UserCreate, db:Session):
    existing_user = db.execute(select(User).where(User.user_name == data.user_name)).scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user name is already registered"
        )
    
    hashed_password = bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    new_user = User(user_name=data.user_name, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user_service(data, db:Session):
    user = db.execute(select(User).where(User.user_name == data.user_name)).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User name not registered"
        )
    
    if not bcrypt.checkpw(data.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrct password"
        )
    access_token = create_access_token(data={"sub":str(user.id)})

    return {
        "message":"Login successful",
        "access_token": access_token,
        "totken_type":"bearer"
    }