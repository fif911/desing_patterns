from typing import Optional

from pydantic import BaseModel, ValidationError


class Company(BaseModel):
    name: str
    address: str


class Item(BaseModel):
    name: str
    company_id: int
    quantity: int
    stripe_id: int
    description: Optional[str]


if __name__ == '__main__':
    item_in = {"name": "Item", "company_id": 2}
    try:
        Item(**item_in)
    except ValidationError as e:
        print(e)
