from datetime import datetime
from model.InventoryItem import InventoryCreate, Inventory, InventoryDB, InventoryUpdate
from fastapi.encoders import jsonable_encoder
from database import Inventory_collection
from model.user import UserPayload
from seralizer import Inventory_serailzer, Inventory_serializer_list
from bson import ObjectId
from fastapi import HTTPException,status


class InventoryCrud:
    @staticmethod
    def create_inventory(data: InventoryCreate, current_user: UserPayload) -> InventoryDB:
        data = data.model_dump()
        data["User_name"] = current_user.username
        data["createdAt"] = datetime.utcnow()
        data["updateAt"] = datetime.utcnow()

        result = Inventory_collection.insert_one(jsonable_encoder(data))
        new_item = Inventory_collection.find_one({"_id": result.inserted_id})
        return Inventory_serailzer(new_item)

    
    @staticmethod
    def get_inventory_with_id(id: str):
        item = Inventory_collection.find_one({"_id": ObjectId(id)})

        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not Found")
        return Inventory_serailzer(item)
    

    @staticmethod
    
    def List_of_Inventory():
        items = Inventory_collection.find()
        return Inventory_serializer_list(items)

    
    @staticmethod
    def update_all_inventory(id: str, data: InventoryUpdate):
        data = jsonable_encoder(data)  
        Inventory_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        updated_item = Inventory_collection.find_one({"_id": ObjectId(id)})
        return Inventory_serailzer(updated_item)




    @staticmethod
    def delete_inventory(inventory_id: str):
        inventory = Inventory_collection.find_one({"id": ObjectId(inventory_id)})
        if inventory:

            remove = Inventory_collection.delete_one({"_id": ObjectId(inventory_id)})
            return {"message": "Inventory Deleted Successfully", "data": remove}
        
        else:
           if not inventory:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory not found")
            

inventory_crud = InventoryCrud()