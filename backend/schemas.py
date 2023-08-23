from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str



class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
#band
class BandBase(BaseModel):
    Name: str
      

class BandCreate(BandBase):
    pass

class Band(BandBase):
    BandID: int

class Config:
        orm_mode = True
#podium
class PodiumBase(BaseModel):
    Name: str
   

class PodiumCreate(PodiumBase):
    pass

class Podium(PodiumBase):
    PodiumID: int
class Config:
        orm_mode = True
#festival
class FestivalBase(BaseModel):
    Name: str
    Location: str
       

class FestivalCreate(FestivalBase):
    pass

class Festival(FestivalBase):
    FestivalID: int
    Price: float
    Year: int

class Config:
        orm_mode = True
#lineup
class Lineupbase(BaseModel):
  Genre:  str    
       

class FestivalCreate(FestivalBase):
    pass

class Festival(FestivalBase):
    LineupID: int
    Band_id: int
    Festival_id: int
    Podium_id: int
    owner_id : int
    Score: float


class Config:
        orm_mode = True