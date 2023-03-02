from config import DATA_PATH
from models import (
    FederationEntity,
    District,
    Locality,
    SportObject,
    SportObjectType,
    SportType,
    ContestType,
    SportObjectAction,
    SportObjectSignificance,
)

import csv
import datetime as dt
import sys
import asyncio

from pydantic import BaseModel, Field, validator, ValidationError


class SportObjectCSV(BaseModel):
    id: int = Field(alias="id:")
    name: str = Field(alias="Название:")
    name_en: str | None = Field(alias="Название (in english):")
    is_active: bool = Field(alias="Активный:")
    short_description: str | None = Field(alias="Краткое описание:")
    full_description: str | None = Field(alias="Детальное описание:")
    short_description_en: str | None = Field(alias="Краткое описание (in english):")
    full_description_en: str | None = Field(alias="Детальное описание (in english):")
    federation_entity: str = Field(alias="Субъект федерации:")
    district: str = Field(alias="МО:")
    locality: str = Field(alias="Населённый пункт:")
    locality_en: str | None = Field(alias="Населённый пункт (in english):")
    address: str = Field(alias="Адрес:")
    address_en: str | None = Field(alias="Адрес (in english):")
    applied_action: SportObjectAction = Field(alias="Действия с объектом:")
    construction_start_date: dt.date | None = Field(
        alias="Дата начала строительства / реконструкции:"
    )
    construction_end_date: dt.date | None = Field(
        alias="Дата завершения строительства / реконструкции:"
    )
    total_funds: int = Field(alias="Общий объём финансирования:")
    phone_number: str | None = Field(alias="контактный телефон объекта:")
    email: str | None = Field(alias="E-mail:")
    site_url: str | None = Field(alias="URL сайта:")
    sport_object_type: str | None = Field(alias="Тип спортивного комплекса:")
    contest_types: list[str] = Field(alias="Какие соревнования проводятся?:")
    sport_types: list[str] = Field(alias="Виды спорта:")
    latitude: float = Field(alias="Яндекс координата объекта Y:")
    longitude: float = Field(alias="Яндекс координата объекта X:")
    significance: SportObjectSignificance | None = Field(alias="Значимость:")

    @validator("construction_start_date", "construction_end_date", pre=True)
    def parse_dates(cls, v: str) -> dt.date | None:
        if v:
            return dt.datetime.strptime(v, "%d.%m.%Y").date()

    @validator("contest_types", "sport_types", pre=True)
    def parse_lists(cls, v: str) -> list[str]:
        if not v:
            return []
        return [x.strip() for x in v.split(",")]


async def load():
    with open(DATA_PATH) as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            for key in row:
                if row[key] == "":
                    row[key] = None

            try:
                raw_obj = SportObjectCSV(**row)
            except ValidationError as e:
                print(row, e, file=sys.stderr)
                continue
            fed_entity, _ = await FederationEntity.get_or_create(
                name=raw_obj.federation_entity
            )
            district, _ = await District.get_or_create(
                name=raw_obj.district, federation_entity=fed_entity
            )
            locality, _ = await Locality.get_or_create(
                name=raw_obj.locality, name_en=raw_obj.locality_en, district=district
            )
            if raw_obj.sport_object_type:
                sport_object_type, _ = await SportObjectType.get_or_create(
                    name=raw_obj.sport_object_type
                )
            else:
                sport_object_type = None
            sport_types = [
                (await SportType.get_or_create(name=st))[0]
                for st in raw_obj.sport_types
            ]
            contest_types = [
                (await ContestType.get_or_create(name=ct))[0]
                for ct in raw_obj.contest_types
            ]

            saved_object = await SportObject.create(
                name=raw_obj.name,
                name_en=raw_obj.name_en,
                is_active=raw_obj.is_active,
                short_description=raw_obj.short_description,
                full_description=raw_obj.full_description,
                short_description_en=raw_obj.short_description_en,
                full_description_en=raw_obj.full_description_en,
                federation_entity=fed_entity,
                district=district,
                locality=locality,
                address=raw_obj.address,
                address_en=raw_obj.address_en,
                applied_action=raw_obj.applied_action,
                construction_start_date=raw_obj.construction_start_date,
                construction_end_date=raw_obj.construction_end_date,
                total_funds=raw_obj.total_funds,
                phone_number=raw_obj.phone_number,
                email=raw_obj.email,
                site_url=raw_obj.site_url,
                object_type=sport_object_type,
                latitude=raw_obj.latitude,
                longitude=raw_obj.longitude,
                significance_level=raw_obj.significance,
            )
            await saved_object.sport_types.add(*sport_types)
            await saved_object.contest_types.add(*contest_types)


if __name__ == "__main__":
    asyncio.run(load())
