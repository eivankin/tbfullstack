from tortoise import fields, models, validators, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

import enum


class FederationEntity(models.Model):
    """Субъект федерации"""

    name = fields.CharField(
        max_length=255, unique=True, validators=[validators.MinLengthValidator(1)]
    )
    districts: fields.ForeignKeyRelation["District"]


class District(models.Model):
    """Муниципальный округ"""

    federation_entity = fields.ForeignKeyField(
        "models.FederationEntity", related_name="districts"
    )
    name = fields.CharField(
        max_length=255, validators=[validators.MinLengthValidator(1)]
    )
    localities: fields.ForeignKeyRelation["Locality"]


class Locality(models.Model):
    """Населённый пункт"""

    district = fields.ForeignKeyField("models.District", related_name="localities")
    name = fields.CharField(
        max_length=255, validators=[validators.MinLengthValidator(1)]
    )
    name_en = fields.CharField(max_length=255, null=True)
    sport_objects: fields.ForeignKeyRelation["SportObject"]


class SportType(models.Model):
    """Вид спорта"""

    name = fields.CharField(
        max_length=255, unique=True, validators=[validators.MinLengthValidator(1)]
    )
    sport_objects: fields.ManyToManyRelation["SportObject"]


class SportObjectType(models.Model):
    """Тип спортивного комплекса"""

    name = fields.CharField(
        max_length=255, unique=True, validators=[validators.MinLengthValidator(1)]
    )
    sport_objects: fields.ForeignKeyRelation["SportObject"]


class SportObjectSignificance(enum.StrEnum):
    REGIONAL = "регионально-значимый"
    FEDERAL = "федерально-значимый"


class SportObjectAction(enum.StrEnum):
    CONSTRUCTION = "строительство"
    RECONSTRUCTION = "реконструкция"
    OTHER = "другое"


class ContestType(models.Model):
    """Какие соревнования проводятся в спортивном объекте"""

    name = fields.CharField(
        max_length=255, unique=True, validators=[validators.MinLengthValidator(1)]
    )
    sport_objects: fields.ManyToManyRelation["SportObject"]


class SportObject(models.Model):
    """Спортивный объект"""

    locality = fields.ForeignKeyField("models.Locality", related_name="sport_objects")
    name = fields.CharField(
        max_length=255, validators=[validators.MinLengthValidator(1)]
    )
    name_en = fields.CharField(
        max_length=255, null=True, validators=[validators.MinLengthValidator(1)]
    )
    is_active = fields.BooleanField()
    short_description = fields.TextField(null=True)
    short_description_en = fields.TextField(null=True)
    full_description = fields.TextField(null=True)
    full_description_en = fields.TextField(null=True)
    latitude = fields.FloatField(
        validators=[
            validators.MinValueValidator(-90.0),
            validators.MaxValueValidator(90.0),
        ]
    )
    longitude = fields.FloatField(
        validators=[
            validators.MinValueValidator(-180.0),
            validators.MaxValueValidator(180.0),
        ]
    )
    address = fields.CharField(
        max_length=255, validators=[validators.MinLengthValidator(1)]
    )
    address_en = fields.CharField(
        max_length=255, null=True, validators=[validators.MinLengthValidator(1)]
    )

    sport_types = fields.ManyToManyField(
        "models.SportType", related_name="sport_objects"
    )
    object_type = fields.ForeignKeyField(
        "models.SportObjectType", related_name="sport_objects", null=True
    )

    significance_level = fields.CharEnumField(SportObjectSignificance, null=True)
    contest_types = fields.ManyToManyField(
        "models.ContestType", related_name="sport_objects"
    )

    site_url = fields.CharField(
        max_length=255, null=True, validators=[validators.MinLengthValidator(1)]
    )
    applied_action = fields.CharEnumField(SportObjectAction, null=True)
    construction_start = fields.DateField(null=True)
    construction_end = fields.DateField(null=True)
    total_funds = fields.BigIntField(default=0)

    email = fields.CharField(
        max_length=255, null=True, validators=[validators.MinLengthValidator(1)]
    )
    phone_number = fields.CharField(
        max_length=50, null=True, validators=[validators.MinLengthValidator(1)]
    )


Tortoise.init_models(["models"], "models")
SportObject_Pydantic = pydantic_model_creator(SportObject, name="SportObject")
FederationEntity_Pydantic = pydantic_model_creator(
    FederationEntity, name="FederationEntity"
)
District_Pydantic = pydantic_model_creator(District, name="District")
ContestType_Pydantic = pydantic_model_creator(ContestType, name="ContestType")
SportObjectType_Pydantic = pydantic_model_creator(
    SportObjectType, name="SporObjectType"
)
SportType_Pydantic = pydantic_model_creator(SportType, name="SportType")
Locality_Pydantic = pydantic_model_creator(Locality, name="Locality")
SportObjectShort_Pydantic = pydantic_model_creator(
    SportObject,
    name="SportObjectShort",
    include=("id", "latitude", "longitude", "is_active"),
)
