from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas_user import UserCreate,UserResponse
from app.services.user_service import register_user_service, login_user_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(data:UserCreate, db:Session = Depends(get_db)):
    return register_user_service(data, db)

@router.post("/login")
def login_user(data: UserCreate, db:Session = Depends(get_db)):
    return login_user_service(data, db )