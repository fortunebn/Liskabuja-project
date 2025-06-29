from model.user import UserCreate, User
from fastapi.encoders import jsonable_encoder
from database import Users_collection
from seralizer import User_serailzer
from bson import ObjectId
from auth import get_password_hash


class UserCrud:
    @staticmethod
    def create_account(user: UserCreate)-> User:
        user = user.model_dump()
        user["password"] = get_password_hash(user["password"])
        user_payload = User(**user)
        user_id = Users_collection.insert_one(jsonable_encoder(user_payload)).inserted_id
        user_data = Users_collection.find_one({"_id": user_id})
        return User_serailzer(user_data)
    
    @staticmethod
    def get_user_with_username(username: str):
        user = Users_collection.find_one({"username": username})
        return user
    

user_crud = UserCrud()