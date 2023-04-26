import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite_characters = Table(
    "favorite_characters",
     Base.metadata,
    Column("user_id", ForeignKey("User.id")),
    Column("character_id", ForeignKey("Character.id")),
)
favorite_planets = Table(
    "favorite_planets",
     Base.metadata,
    Column("user_id", ForeignKey("User.id")),
    Column("planet_id", ForeignKey("Planet.id")),
)
favorite_vehicles = Table(
    "favorite_vehicles",
     Base.metadata,
    Column("user_id", ForeignKey("User.id")),
    Column("vehicle_id", ForeignKey("Vehicle.id")),
)
favorite_starships= Table(
    "favorite_starships",
     Base.metadata,
    Column("user_id", ForeignKey("User.id")),
    Column("starship_id", ForeignKey("Starship.id")),
)

class User(Base):
    __tablename__ ='User'
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(256))
    email = Column(String(256))
    user_name = Column(String(256))
    password = Column(String(256))
    favorite_characters=relationship('Character',secondary="favorite_characters", backref="user_characters", lazy=True)
    favorite_planets=relationship('Planet',secondary="favorite_planets", backref="user_planets", lazy=True)
    favorite_vehicles=relationship('Vehicle',secondary="favorite_vehicles", backref="user_vehicles", lazy=True)
    favorite_starships=relationship('Starship',secondary="favorite_starships", backref="user_starships", lazy=True)

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True, unique = True)
    name = Column(String(256))
    birth_year = Column(String(256))
    eye_color = Column(String(256))
    gender = Column(String(256))
    hair_color = Column(String(256))
    height = Column(String(256)) 
    mass = Column(String(256))
    skin_color = Column(String(256))
    homeworld = Column(String(256))
    
    def to_dict(self):
        return {}

class Starship(Base):
    __tablename__ = 'Starship'
    id = Column(Integer, primary_key=True, unique = True)
    name = Column(String(256))
    model = Column(String(256)) 
    starship_class = Column(String(256))
    manufacturer = Column(String(256))
    cost_in_credits = Column(String(256))
    length = Column(String(256))
    crew = Column(String(256))
    passengers = Column(String(256))
    max_atmosphering_speed = Column(String(256))
    hyperdrive_rating = Column(String(256))
    MGLT = Column(String(256))
    cargo_capacity = Column(String(256))

    def to_dict(self):
        return {}

class Vehicle(Base):
    __tablename__ = "Vehicle"
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(256))
    model = Column(String(256))
    vehicle_class = Column(String(256))
    manufacturer = Column(String(256))
    length = Column(String(256))
    cost_in_credits = Column(String(256))
    crew = Column(String(256))
    passengers = Column(String(256))
    max_atmosphering_speed = Column(String(256))
    cargo_capacity = Column(String(256))

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = "Planet"
    id = Column(Integer, primary_key = True, unique = True)
    name = Column(String(256))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(256))
    population = Column(Integer)
    climate = Column(String(256))
    terrain = Column(String(256))
    surface_water = Column(String(256))

    def to_dict(self):
        return {}

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
