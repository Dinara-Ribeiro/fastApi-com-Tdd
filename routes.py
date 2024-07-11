from fastapi import APIRouter, HTTPException
from .database import get_database
from .models import Item

router = APIRouter()

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    db = get_database()
    item_dict = item.dict()
    await db["items"].insert_one(item_dict)
    return item

@router.get("/items/")
async def read_items():
    db = get_database()
    items = await db["items"].find().to_list(100)
    return items
