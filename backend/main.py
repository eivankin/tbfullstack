from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import DB_URL

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


register_tortoise(
    app=app,
    db_url=DB_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
)
