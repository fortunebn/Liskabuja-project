import os
from pymongo import mongo_client
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
client = mongo_client.MongoClient(MONGO_DB_URL)

Users_collection = client["Lisk_Abuja"]["User"]
Inventory_collection = client["Lisk_Abuja"]["Inventory"]
