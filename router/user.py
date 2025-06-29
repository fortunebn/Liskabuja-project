import os
from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, verify_password
from model.token import Token, TokenData
from model.user import UserCreate, User, UserPayload
from crud.user import user_crud
from dotenv import load_dotenv
from jose import jwt, JWTError


load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")  # Change this in production
ALGORITHM = os.environ.get("ALOGRITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 60))


user_router = APIRouter()


@user_router.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_user = user_crud.create_account(user)
    return {"Message": "User Created Successfully", "data": new_user}



@user_router.post("/token", status_code=status.HTTP_202_ACCEPTED)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user: UserPayload = user_crud.get_user_with_username(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"message": "Invaild credentials"},
        )
    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail={"message": "Invaild credentials"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    print("User data=======:", user)

    data_to_encode = TokenData(
    id=str(user["_id"]),
    username=user["username"]
).model_dump()
    access_token = create_access_token(
        data=data_to_encode, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
