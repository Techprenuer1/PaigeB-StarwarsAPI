import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
# from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship("Favorites", backref="user")

    
  
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_characters = Column(Integer(250), ForeignKey('characters.id'))
    favorite_planet = Column(Integer(250), ForeignKey('planet.id'))
    favorite_vehicle = Column(Integer(250), ForeignKey('vehicle.id'))
    user_id = Column(Integer(250)), ForeignKey('user.id')




class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(Integer)  
    homeworld = Column(String(250)) 
    favorite = relationship('favorites', backref="characters") 
    # person = relationship(Person)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    rotation_period = Column(Integer)
    favorite = relationship('favorites', backref='planet')
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    passengers = Column(Integer)
    starship_class = Column(String(250))
    favorite = relationship('favorites', backref='vehicle')




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
