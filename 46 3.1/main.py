from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

items = {
    "1": {"name": "Item 1"},
    "2": {"name": "Item 2"},
    "3": {"name": "Item 3"},
}

@app.get("/items/{item_id}")
def read_item(item_id: str):
    try:
        return items[item_id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")