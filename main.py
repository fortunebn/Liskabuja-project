from fastapi import FastAPI
from router.user import user_router
from router.InventoryItem import Inventory_router


app = FastAPI()
app.include_router(user_router, tags=["User"])
app.include_router(Inventory_router, tags=["Inventory Item"])

@app.get("/")
def Home_page():
    return {"message": "welcome To my lisk abuja assessment api"}