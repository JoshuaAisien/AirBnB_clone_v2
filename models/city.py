#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
class City(BaseModel, Base):
    """ The city class"""
    __tablename__ = 'cities'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_0900_ai_ci'}

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # relationships
    places = relationship('Place', back_populates='cities', cascade="all, delete-orphan")
