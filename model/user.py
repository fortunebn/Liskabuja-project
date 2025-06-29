from pydantic import BaseModel, EmailStr, Field
from datetime import datetime



class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserCreate):

    createdAt: datetime  = datetime.now()
    updatedAt: datetime = datetime.now()

class UserPayload(UserBase):
    id: str 
    createdAt: datetime
    updatedAt: datetime 

class UserDB(UserBase):
    id: str
    createdAt: datetime
    updatedAt: datetime


# class Config:
#         allow_population_by_field_name = True
