"""Main FastAPI File."""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Sample of a Request Model."""

    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
async def read_root():
    """Read from api root."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, _q: Optional[str] = None):
    """Read Item from query string."""
    return {"item_id": item_id, "q": _q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Update Item from query string."""
    return {"item_name": item.name, "item_id": item_id}
