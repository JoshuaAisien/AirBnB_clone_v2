#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                      )
class Amenity(BaseModel, Base):

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity, back_populates='amenities')

