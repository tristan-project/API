from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from uuid import UUID, uuid4


import crud as crud
import models as models
import schemas as schemas
import database as database
import os
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     #db_user = crud.get_user_by_email(db, email=user.email)
#     ##   raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

@app.post("/users", response_model=schemas.User)  # Use the schema for response
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("Received user data:", user)  # <-- Add this print statement

    return crud.create_user(db, user)


@app.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}")
async def remove_user(user_id: str, db: Session = Depends(get_db)):  # Use UUID
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )
    return {"status": "User deleted"}



@app.put("/users/{user_id}")
async def update_existing_user(user_id: str, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_data = user_update.dict(exclude_unset=True)
    updated_user = crud.update_user(db, user_id, updated_data)
    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )
    return updated_user




@app.post("/users/{user_id}/items/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items


@app.get("/bands", response_model=list[schemas.Band])
def read_bands(db: Session = Depends(get_db)):
    bands = crud.get_bands(db)
    return bands


@app.post("/bands", response_model=schemas.Band, status_code=status.HTTP_201_CREATED)
def create_band_endpoint(band: schemas.BandCreate, db: Session = Depends(get_db)):
    band_id = crud.create_band(db, band)
    return {"id": band_id, "name": band.name}




@app.get("/festivals", response_model=list[schemas.Festival])
def read_festivals(db: Session = Depends(get_db)):
    festivals = crud.get_festivals(db)
    return festivals


@app.post("/festivals", response_model=schemas.Festival, status_code=status.HTTP_201_CREATED)
def create_festivals_endpoint(festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    festivals = crud.create_festivals(db, festival)
    return {"id": festivals, "name": festival.name}




@app.get("/poduims", response_model=list[schemas.Podium])
def read_poduims(db: Session = Depends(get_db)):
    poduims = crud.get_festivals(db)
    return poduims


@app.post("/poduims", response_model=schemas.Podium, status_code=status.HTTP_201_CREATED)
def create_poduims_endpoint(poduim: schemas.PodiumCreate, db: Session = Depends(get_db)):
    poduims = crud.create_poduims(db, poduim)
    return {"id": poduims, "name": poduim.name}
