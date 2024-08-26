#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
class City(BaseModel, Base):
    """ The city class"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # relationships
    places = relationship('Place', back_populates='cities', cascade="all, delete-orphan")