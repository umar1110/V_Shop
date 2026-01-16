from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Voice Shop Service", version="1.0.0")

from .api.v1.router import api_router

app.include_router(api_router, prefix="/api/v1")



@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    quantity: Union[int, None] = None

class MoreItem(BaseModel):
    description: Union[str, None] = None
    tax: Union[float, None] = None

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, r: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "r": r}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item , moreItem : MoreItem):
    return {"item_name": item.name, "item_id": item_id}