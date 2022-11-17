import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Card(Base):
    __tablename__ = 'card'
    # Here we define columns for the table card.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image = Column(String(50))
    description = Column(String(50))
    character = relationship('Character', backref='card')

class Character (Base):
    __tablename__ = 'character'
     # Here we define columns for the table character.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    birth_date = Column(String(50))
    gender = Column(String(50))
    height = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    children1 = relationship ('Favorite', back_populates = 'parent1')

class Vehicle (Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table vehicle.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    model = Column(String(50))
    passengers = Column(String(50))
    lenght = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    children2 = relationship ('Favorite', back_populates = 'parent2')

class Planet (Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    climate = Column(String(50))
    population = Column(String(50))
    orbital_period = Column(String(50))
    rotation_period = Column(String(50))
    diameter = Column(String(50))
    children3 = relationship ('Favorite', back_populates = 'parent3')

class Favorite (Base):
    __tablename__= 'favorite'
    # Here we define columns for the table favorite.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    card_id = Column(Integer, ForeignKey('card.id'))
    # Store favorites.
    character_fav = Column(Integer,ForeignKey('character.id'))
    planet_fav = Column(Integer,ForeignKey('planet.id'))
    vehicle_fav = Column(Integer,ForeignKey('vehicle.id'))
    # Save characters, vehicles and planets from children to parent.
    parent1 = relationship ('Character', back_populates = 'children1')
    parent2 = relationship ('Vehicle', back_populates = 'children2')
    parent3 = relationship ('Planet', back_populates = 'children3')

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    password = Column(String(256))

    def to_dict(self):
       return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
