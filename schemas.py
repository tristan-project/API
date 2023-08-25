from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from typing import Optional



class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: UUID
    owner_id: str

    class Config:
        from_attributes = True





class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str



class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool
    items: list[Item] = []




class UserUpdate(BaseModel):  # For updating a user
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]


class BandBase(BaseModel):
    name: str  # Changed to lowercase for consistency


class BandCreate(BandBase):
    pass


class Band(BandBase):
    id: UUID  # Changed to snake_case for consistency


class PodiumBase(BaseModel):
    name: str  # Changed to lowercase for consistency


class PodiumCreate(PodiumBase):
    pass


class Podium(PodiumBase):
    podium_id: str  # Changed to snake_case for consistency

    class Config:
        from_attributes = True


class FestivalBase(BaseModel):
    name: str
    location: str  # Changed to lowercase for consistency


class FestivalCreate(FestivalBase):
    pass


class Festival(FestivalBase):
    festival_id: str  # Changed to snake_case for consistency
    price: float
    year: int

    class Config:
        from_attributes = True


class LineupBase(BaseModel):  # Fixed typo in class name
    genre: str  # Changed to lowercase for consistency


class LineupCreate(LineupBase):
    pass



class Lineup(LineupBase):  # Fixed the class name
    lineup_id: str  # Changed to snake_case for consistency
    band_id: str
    festival_id: str
    podium_id: str
    owner_id: str
    score: float

    class Config:
        from_attributes = True