from tortoise import fields, models, validators

import enum


class FederationEntity(models.Model):
    """Субъект федерации"""

    name = fields.CharField(max_length=255, unique=True)
    districts: fields.ForeignKeyRelation["District"]


class District(models.Model):
    """Муниципальный округ"""

    federation_entity = fields.ForeignKeyField(
        "FederationEntity", related_name="districts"
    )
    name = fields.CharField(max_length=255, unique=True)
    localities: fields.ForeignKeyRelation["Locality"]


class Locality(models.Model):
    """Населённый пункт"""

    district = fields.ForeignKeyField("District", related_name="localities")
    name = fields.CharField(max_length=255, unique=True)
    name_en = fields.CharField(max_length=255, null=True)
    sport_objects: fields.ForeignKeyRelation["SportObject"]


class SportType(models.Model):
    """Вид спорта"""

    name = fields.CharField(max_length=255, unique=True)
    sport_objects: fields.ManyToManyRelation["SportObject"]


class SportObjectType(models.Model):
    """Тип спортивного комплекса"""

    name = fields.CharField(max_length=255, unique=True)
    sport_objects: fields.ForeignKeyRelation["SportObject"]


class SportObjectSignificance(enum.StrEnum):
    REGIONAL = "регионально-значимый"
    FEDERAL = "федерально-значимый"


class ContestType(models.Model):
    """Какие соревнования проводятся в спортивном объекте"""

    name = fields.CharField(max_length=255, unique=True)
    sport_objects: fields.ManyToManyRelation["SportObject"]


class SportObject(models.Model):
    """Спортивный объект"""

    locality = fields.ForeignKeyField("Locality", related_name="sport_objects")
    name = fields.CharField(max_length=255, unique=True)
    name_en = fields.CharField(max_length=255, null=True)
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
    address = fields.CharField(max_length=255)
    address_en = fields.CharField(max_length=255, null=True)

    sport_types = fields.ManyToManyField("SportType", related_name="sport_objects")
    object_type = fields.ForeignKeyField(
        "SportObjectType", related_name="sport_objects"
    )

    significance_level = fields.CharEnumField(SportObjectSignificance, null=True)
    contest_types = fields.ManyToManyField("ContestType", related_name="sport_objects")

    site_url = fields.CharField(max_length=255, null=True)
    # TODO: finish fields
