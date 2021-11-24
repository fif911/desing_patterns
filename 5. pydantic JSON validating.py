import json
from typing import Optional, Union, List

from pydantic import BaseModel, Field, Json, validator, Extra


def normalize_json_field(cls, value: Union[Json, str]) -> str:
    # Values coming from REST API dont need to be converted (it's already string and not object)
    if isinstance(value, str):
        return value

    # The JSON coming from DB to Pydantic needs to be stringified before validating
    return json.dumps(value) if value else None


class BuildingApartmentDetail(BaseModel):
    id: int = Field(None, ge=0, le=999)
    area: float = Field(None, ge=0)

    class Config:
        extra = Extra.forbid


class BuildingApartmentOtherDetail(BuildingApartmentDetail):
    location: str = Field(None, max_length=255)
    space_purpose: str = Field(None, max_length=255)


class BuildingApartmentSchemaBase(BaseModel):
    progress: bool
    totalArea: float = Field(None, ge=0)  # Mandatory if progress == True

    class Config:
        extra = Extra.forbid


class BuildingApartmentSchema(BuildingApartmentSchemaBase):
    # {apartments: [{id: , area: }], totalArea: , CountOfApartments: }
    apartments: List[BuildingApartmentDetail] = None
    countOfApartments: int = Field(None, ge=0, le=999)


class BuildingApartmentOtherUseSchema(BuildingApartmentSchemaBase):
    # {apartments: [{id: , area: , location: , space_purpose: }], TotalArea: }
    apartments: List[BuildingApartmentOtherDetail] = None


class Building(BaseModel):
    property_size_net_s60: Optional[Json] = None

    # validators
    _normalize_json = validator('property_size_net_s60', pre=True, allow_reuse=True, )(normalize_json_field)

    @validator("property_size_net_s60")
    def validate_json(cls, v, ):
        if v is not None:
            BuildingApartmentSchema(**v)
            if v['progress'] is True:
                assert 'totalArea' in v, "totalArea is mandatory for objects in progress"

        return v

    @validator("property_size_net_s60")
    def validate_json(cls, v, ):
        if v is not None:
            BuildingApartmentOtherUseSchema(**v)
            if v['progress'] is True:
                assert 'totalArea' in v, "totalArea is mandatory for objects in progress"

        return v


if __name__ == '__main__':
    # property_size_net_s60
    #   Invalid JSON (type=value_error.json)
    # print(Building(property_size_net_s60="")) # invalid JSON
    # print(Building(property_size_net_s60="asd")) # invalid JSON

    # property_size_net_s60 -> progress
    #   field required (type=value_error.missing)
    # Building(property_size_net_s60="{}")

    # property_size_net_s60 -> progress
    #   field required (type=value_error.missing)
    # Building(property_size_net_s60="""{"apartments":[{"id": 1, "area": 2}],"totalArea": 2, "countOfApartments": 1}""")

    # property_size_net_s60 -> apartmentsssss
    #   extra fields not permitted (type=value_error.extra)
    # Building(property_size_net_s60="""{"apartmentsssss":[{"id": 1, "area": 2}],"totalArea": 2, "countOfApartments": 1,"progress": true}""")

    # property_size_net_s60
    #   totalArea is mandatory for objects in progress (type=assertion_error)
    # Building(
    #     property_size_net_s60="""{"progress": true}""")

    print(Building(property_size_net_s60=None))  # will pass
    print(Building(property_size_net_s60="""null"""))  # will pass
    Building(
        property_size_net_s60="""{"apartments":[{"id": 1, "area": 2}],"totalArea": 2, "countOfApartments": 1,"progress": true}""")
    print(Building(
        property_size_net_s60="""{"apartments":[{"id": 1, "area": 2.2}],"totalArea": 2.14, "countOfApartments": 1,"progress": false}"""))
    Building(property_size_net_s60="""{"totalArea": 2.1,"progress": true}""")
