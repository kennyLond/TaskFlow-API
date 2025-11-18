from pydantic import BaseModel, Field, field_validator
import re

class UserBase(BaseModel):
    user_name : str = Field(...,description='User name')

class UserCreate(UserBase):
    password: str = Field(...,min_length=4, description='secure password')

    @field_validator("password")
    def validate_password(cls,password):
        if len(password) < 3:
            raise ValueError("te password must be at least 4 characters long.")
        if not re.search(r"[A-Z]", password):
            raise ValueError("the password must include at least one uppercase letter")
        
        if len(re.findall(r"\d", password)) < 1:
            raise ValueError ( "The password must contain at least one number.")
        
        return password

class UserLogin(BaseModel):
    user_name: str
    password : str

class UserResponse(BaseModel):
    id: int
    user_name: str

    class Config:
        orm_mode = True