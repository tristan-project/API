from sqlite3 import IntegrityError
from sqlalchemy.orm import Session

from uuid import UUID, uuid4

from models import User
import models as models
import schemas as schemas
from utils import hash_password


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    print("Creating user with data:", user)
    hashed_password = hash_password(user.password)
    db_user = models.User(first_name = user.first_name, last_name = user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# def create_user(db: Session, user: schemas.UserCreate):
#     # Convert the Pydantic model to an SQLAlchemy model
#     db_user = User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def update_user(db: Session, user_id: str, updated_data: dict):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in updated_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user



def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#  gebruikersid, band

def get_bands(db: Session):
    return db.query(models.Band).all()



def create_band(db: Session, band: schemas.BandCreate):
    db_band = models.Band(name=band.name)
    db.add(db_band)
    db.commit()
    db.refresh(db_band)
    return db_band.id


# def get_band_by_name(db: Session, name: str):
#     """Fetch a band by its name."""
#     return db.query(models.Band).filter(models.Band.name == name).first()

# def create_band(db: Session, band: schemas.BandCreate) -> str:
#     """Create a new band if it doesn't exist and return its id."""
#     existing_band = get_band_by_name(db, band.name)  # Note: changed `band.Name` to `band.name`
    
#     if existing_band:
#         # Band already exists, return its ID
#         return existing_band.id
#     else:
#         db_band = models.Band(**band.dict())
#         db.add(db_band)
#         db.commit()
#         db.refresh(db_band)
#         return db_band.id  # return the id of the newly created band

#  creatie festival   
 
def get_festival_by_name(db: Session, name: str):
    """Fetch a festival by its name."""
    return db.query(models.Festival).filter(models.Festival.Name == name).first()
    
def create_festival(db: Session, festival: schemas.FestivalCreate) -> int:
    """Create a new festival if it doesn't exist and return its FestivalID."""
    existing_festival = get_festival_by_name(db, festival.Name)  # zorg dat je deze functie ook hebt
    if existing_festival:
        # Festival already exists, return its ID
        return existing_festival.FestivalID
    else:
        db_festival = models.Festival(**festival.dict())
        db.add(db_festival)
        try:
            db.commit()
            db.refresh(db_festival)
            return db_festival.FestivalID  # return the FestivalID of the newly created festival
        except IntegrityError:
            db.rollback()
            raise ValueError(f"Festival with name {festival.Name} already exists!")  

#  creatie podium
def get_podium_by_name(db: Session, name: str):
    """Fetch a podium by its name."""
    return db.query(models.Podium).filter(models.Podium.Name == name).first()

def create_podium(db: Session, podium: schemas.PodiumCreate) -> int:
    """Create a new podium if it doesn't exist and return its PodiumID."""
    existing_podium = get_podium_by_name(db, podium.Name)
    if existing_podium:
        # Podium already exists, return its ID
        return existing_podium.PodiumID
    else:
        db_podium = models.Podium(**podium.dict())
        db.add(db_podium)
        try:
            db.commit()
            db.refresh(db_podium)
            return db_podium.PodiumID  # return the PodiumID of the newly created podium
        except IntegrityError:
            db.rollback()
            raise ValueError(f"Podium with name {podium.Name} already exists!")



