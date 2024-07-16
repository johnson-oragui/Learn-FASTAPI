from pydantic import BaseModel, Field
from typing import Union
from enum import Enum


class Item(BaseModel):
    """

    """
    name: str
    price: float = Field(gt=0,
                         lt=9999999)
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300,
        min_length=10
    )
    is_offer: Union[bool, None] = None

class ProductOption(str, Enum):
    """Enumeration of possible product options."""
    SIZE_SMALL = "small"
    SIZE_MEDIUM = "medium"
    SIZE_LARGE = "large"

class User(BaseModel):
    """

    """
    id: int
    username: str
    email: str
    full_name: str | None = None
