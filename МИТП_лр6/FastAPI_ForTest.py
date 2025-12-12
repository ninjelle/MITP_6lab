from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items_db = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def list_items():
    return {"items": items_db}

@app.post("/items/")
def create_item(item: Item):
    items_db.append(item.dict())
    return {"message": "Item created", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < len(items_db):
        items_db[item_id] = item.dict()
        return {"message": "Item updated"}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items_db):
        deleted = items_db.pop(item_id)
        return {"message": "Item deleted", "deleted": deleted}
    return {"error": "Item not found"}
