from fastapi import APIRouter, HTTPException, status, Depends
from crud.InventoryItem import inventory_crud
from model.InventoryItem import InventoryCreate, InventoryUpdate
from middware import get_current_user
from router.user import login_for_access_token
from typing import Annotated

Inventory_router = APIRouter()


@Inventory_router.post("/api/v1/inventories", status_code=status.HTTP_201_CREATED)
def create_Inventory_item(
    data: InventoryCreate, current_user=Depends(get_current_user)
):
    payload = inventory_crud.create_inventory(data, current_user)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request"
        )

    return {"Message": "Inventory Created Successfully", "data": payload}


@Inventory_router.get("/api/v1/inventories", status_code=status.HTTP_200_OK)
def List_of_Inventory(current_user=Depends(get_current_user)):
    list_inventory = inventory_crud.List_of_Inventory()
    return list_inventory


@Inventory_router.get("/api/v1/inventories/{id}", status_code=status.HTTP_200_OK)
def Get_inventory_with_id(id: str, current_user=Depends(get_current_user)):
    payload = inventory_crud.get_inventory_with_id(id)
    print("=====Payload:", payload)
    return payload

@Inventory_router.put("/api/v1/inventories/{id}", status_code=status.HTTP_202_ACCEPTED)
def Update_all_(id:str, data: InventoryUpdate, current_user=Depends(get_current_user)):
    inventory = inventory_crud.update_all_inventory(id, data)
    return {"message": "Inventory Updated Successfully", "data": inventory}




@Inventory_router.delete("/api/v1/inventories/{id}", status_code=status.HTTP_202_ACCEPTED)
def Delete_Inventory(id: str, current_user=Depends(get_current_user)):
    Deleted_inventory =  inventory_crud.delete_inventory(id)
    return {"Message": "Inventory Deleted Successfully", "data": Deleted_inventory}
