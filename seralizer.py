from model.user import UserDB
from model.InventoryItem import InventoryDB

def User_serailzer(user)-> UserDB:
    userDict = {
        "id": str(user.get("_id")),
        "username": user.get("username"),
        "email": user.get("email"),
        "createdAt": user.get("createdAt"),
        "updatedAt": user.get("updatedAt")
    }
    return UserDB(**userDict)


def Inventory_serailzer(inventory)-> InventoryDB:
    inventory_dict = {
        "id": str(inventory.get("_id")),
        "name": inventory.get("name"),
        "description": inventory.get("description"),
        "quantity": inventory.get("quantity"),
        "price": inventory.get("price"),
        "createdAt": inventory.get("createdAt"),
        "updateAt": inventory.get("updateAt")
    }
    return InventoryDB(**inventory_dict)

def Inventory_serializer_list(Inventory_documents) -> list:
    return [Inventory_serailzer(Inventory_document) for Inventory_document in Inventory_documents]


