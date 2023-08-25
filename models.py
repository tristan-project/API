from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from uuid import UUID, uuid4

def generate_uuid():
    return str(uuid4())

# Create a base class for declarative models
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")
    lineups = relationship("Lineup", back_populates="user")




class Item(Base):
    __tablename__ = "items"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(String, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")

class  Band(Base):
    __tablename__ = "bands"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    name = Column(String, index=True)  # Changed to lowercase for consistency
    lineups = relationship("Lineup", back_populates="band")



class Podium(Base):
    __tablename__ = "podiums"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    name = Column(String, index=True)  # Changed to lowercase for consistency
    lineups = relationship("Lineup", back_populates="podium")

class Festival(Base):
    __tablename__ = "festivals"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    name = Column(String, index=True)  # Changed to lowercase for consistency
    lineups = relationship("Lineup", back_populates="festival")

class Lineup(Base):
    __tablename__ = "lineups"
    id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    band_id = Column(String, ForeignKey("bands.id"))  # Changed to lowercase for consistency
    festival_id = Column(String, ForeignKey("festivals.id"))  # Changed to lowercase for consistency
    podium_id = Column(String, ForeignKey("podiums.id"))  # Changed to lowercase for consistency
    owner_id = Column(String, ForeignKey("users.id"))
    score = Column(Float, index=True)  # Changed to lowercase for consistency
    year = Column(Integer, index=True)
    number_of_songs = Column(Integer, index=True)  # Changed to lowercase for consistency
    band = relationship("Band", back_populates="lineups")
    podium = relationship("Podium", back_populates="lineups")
    festival = relationship("Festival", back_populates="lineups")
    user = relationship("User", back_populates="lineups")

# Create a database engine and a session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the table in the database
Base.metadata.create_all(engine)