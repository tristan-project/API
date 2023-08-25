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





def get_festivals(db: Session):
    return db.query(models.Festival).all()



def create_festivals(db: Session, festival: schemas.FestivalCreate):
    db_festival = models.Festival(name=festival.name)
    db.add( db_festival)
    db.commit()
    db.refresh( db_festival)
    return  db_festival.id




def get_poduims(db: Session):
    return db.query(models.Podium).all()



def create_poduims(db: Session, poduim: schemas.PodiumCreate):
    db_poduim = models.Podium(name=poduim.name)
    db.add( db_poduim)
    db.commit()
    db.refresh( db_poduim)
    return  db_poduim.id




