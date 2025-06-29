from pydantic import BaseModel, EmailStr, Field, condecimal
from datetime import datetime
from decimal import Decimal
from typing import Optional
from bson.decimal128 import Decimal128


class InventoryitemBase(BaseModel):
    name: str
    description: str
    quantity: int
    price: Decimal = condecimal(gt=0, max_digits=10, decimal_places=2)

class InventoryCreate(InventoryitemBase):
    pass

class Inventory(InventoryitemBase):
    createdAt: datetime = datetime.now()
    updateAt: datetime = datetime.now()

class InventoryUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    updateAt: datetime = Field(default_factory=datetime.now)


class InventoryDB(InventoryCreate):
    id: str
    createdAt: Optional[datetime]
    updateAt: Optional[datetime]
    

