from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    
    login: str
    password: str   