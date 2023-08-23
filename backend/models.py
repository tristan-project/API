from backend.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, StringFloat, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Maak een basis klasse voor declaratieve modellen
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    lineups = relationship("Lineup", back_populates="user")
    


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Band(Base):
    __tablename__ = "Bands"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
       

    lineups = relationship("Lineup", back_populates="band")


class Podium(Base):
    __tablename__ = "Podiums"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    
    lineups = relationship("Lineup", back_populates="podium")
  
class Festival(Base):
    __tablename__ = "Festivals"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)


    lineups = relationship("Lineup", back_populates="festival")


class LineUp(Base):
    __tablename__ = "LineUps"

    id = Column(Integer, primary_key=True, index=True) 
    Band_id = Column(Integer, ForeignKey("Bands.id"))
    Festival_id = Column(Integer, ForeignKey("Festivals.id"))
    Podium_id = Column(Integer, ForeignKey("Podiums.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    Score = Column(Float, index=True) 
    Year = Column(Integer, index=True) 
    Number_of_songs= Column(Integer, index=True)


    band = relationship("Band", back_populates="lineups")
    podium = relationship("Podium", back_populates="lineups")
    festival = relationship("Festival", back_populates="lineups")
    user = relationship("User", back_populates="lineups")

# Maak een database engine en een sessie
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Maak de tabel in de database
Base.metadata.create_all(engine)