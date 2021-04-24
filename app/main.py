from fastapi import FastAPI
from app.models import Pokemon

app = FastAPI()


@app.get("/")
async def root():
    return {"mensaje": "hola mundo"}


@app.get("/items/{item_id}")
async def get_item_id(item_id: int):
    return {"item_id": item_id}


@app.get("/models/")
async def get_models(model_name: str, model_id: int):
    return {model_id: model_name}


@app.post("/pokemon/")
async def post_pokemon(pokemon: Pokemon):
    return pokemon
