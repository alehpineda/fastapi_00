from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mensaje": "hola mundo"}


@app.get("/items/{item_id}")
async def get_item_id(item_id: int):
    return {"item_id": item_id}
