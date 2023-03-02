from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from config import DB_URL, LOAD_DATA, DEBUG
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
    SportObjectSignificance,
    ContestType_Pydantic,
    ContestType,
    SportObjectShort_Pydantic,
)

app = FastAPI(debug=DEBUG)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"]
)


@app.get("/sport-objects/", response_model=list[SportObjectShort_Pydantic])
async def get_sport_objects(
    fed_entity_id: int | None = Query(None, description="ID субъекта федерации"),
    district_id: int | None = Query(None, description="ID МО"),
    locality_id: int | None = Query(None, description="ID населённого пункта"),
    sport_type_id: int | None = Query(None, description="ID вида спорта"),
    sport_object_type_id: int
    | None = Query(None, description="ID типа спортивного комплекса"),
    is_active: bool | None = Query(None, description="Активный ли спортивный комплекс"),
    significance: SportObjectSignificance
    | None = Query(None, description="Значимость спортивного объекта"),
    contest_type_id: int | None = Query(None, description="ID типов соревнований"),
):
    # TODO: return only coordinates (maybe 1-2 extra attributes)
    # TODO: add separate endpoint for full info for popup
    query = SportObject.all()
    if fed_entity_id is not None:
        query = query.filter(locality__district__federation_entity__id=fed_entity_id)

    if district_id is not None:
        query = query.filter(locality__district__id=district_id)

    if locality_id is not None:
        query = query.filter(locality__id=locality_id)

    if sport_type_id is not None:
        query = query.filter(sport_types__id=sport_type_id)

    if sport_object_type_id is not None:
        query = query.filter(object_type__id=sport_object_type_id)

    if is_active is not None:
        query = query.filter(is_active=is_active)

    if significance is not None:
        query = query.filter(significance_level=significance)

    if contest_type_id is not None:
        query = query.filter(contest_types__id=contest_type_id)

    return await SportObjectShort_Pydantic.from_queryset(query)


@app.get("/sport-objects/{sport_object_short_id}", response_model=SportObject_Pydantic)
async def get_sport_object(sport_object_short_id: int):
    return await SportObject_Pydantic.from_queryset_single(
        SportObject.get(id=sport_object_short_id)
    )


@app.get("/federation-entities/", response_model=list[FederationEntity_Pydantic])
async def get_entities():
    return await FederationEntity_Pydantic.from_queryset(FederationEntity.all())


@app.get("/districts/", response_model=list[District_Pydantic])
async def get_districts(
    fed_entity_id: int = Query(None, description="ID субъекта федерации")
):
    query = District.all()
    if fed_entity_id is not None:
        query = query.filter(federation_entity_id=fed_entity_id)
    return await District_Pydantic.from_queryset(query)


@app.get("/localities/", response_model=list[Locality_Pydantic])
async def get_localities(
    district_id: int = Query(None, description="ID МО"),
    fed_entity_id: int = Query(None, description="ID субъекта федерации"),
):
    query = Locality.all()
    if fed_entity_id is not None:
        query = query.filter(district__federation_entity__id=fed_entity_id)

    if district_id is not None:
        query = query.filter(district_id=district_id)

    return await Locality_Pydantic.from_queryset(query)


@app.get("/sport-types/", response_model=list[SportType_Pydantic])
async def get_sport_types():
    return await SportType_Pydantic.from_queryset(SportType.all())


@app.get("/sport-object-types/", response_model=list[SportObjectType_Pydantic])
async def get_sport_object_types():
    return await SportObjectType_Pydantic.from_queryset(SportObjectType.all())


@app.get("/contest-types/", response_model=list[ContestType_Pydantic])
async def get_contest_types():
    return await ContestType_Pydantic.from_queryset(ContestType.all())


register_tortoise(
    app=app,
    db_url=DB_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup():
    if LOAD_DATA and (await SportObject.all().count()) == 0:
        await load()
