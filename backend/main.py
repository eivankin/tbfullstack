from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import DB_URL, LOAD_DATA
from load_data import load
from models import (
    SportObject_Pydantic,
    FederationEntity_Pydantic,
    District_Pydantic,
    Locality_Pydantic,
    SportType_Pydantic,
    SportObjectType_Pydantic,
    SportObject,
    FederationEntity,
    District,
    Locality,
    SportType,
    SportObjectType,
)

app = FastAPI()


@app.get("/sport-object/", response_model=list[SportObject_Pydantic])
async def get_sport_objects():
    query = SportObject.all()
    return await SportObject_Pydantic.from_queryset(query)


@app.get("/federation-entity/", response_model=list[FederationEntity_Pydantic])
async def get_entities():
    return await FederationEntity_Pydantic.from_queryset(FederationEntity.all())


@app.get("/district/", response_model=list[District_Pydantic])
async def get_districts():
    return await District_Pydantic.from_queryset(District.all())


@app.get("/locality/", response_model=list[Locality_Pydantic])
async def get_localities():
    return await Locality_Pydantic.from_queryset(Locality.all())


@app.get("/sport-type/", response_model=list[SportType_Pydantic])
async def get_sport_types():
    return await SportType_Pydantic.from_queryset(SportType.all())


@app.get("/sport-object-type/", response_model=list[SportObjectType_Pydantic])
async def get_sport_object_types():
    return await SportObjectType_Pydantic.from_queryset(SportObjectType.all())


register_tortoise(
    app=app,
    db_url=DB_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
)


@app.on_event("startup")
async def startup():
    if LOAD_DATA:
        await load()
