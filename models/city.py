#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ City class """
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all")
else:
    class City(BaseModel):
        """ City class """
        state_id = ""
        name = ""
