#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from models.base_model import Base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='State', cascade='all, delete-orphan' )

    @property
    def cities(self):
        """ retruns the list of city instances where state_id equals the current state id"""
        from models import storage
        city_instances = storage.all(City)
        return[values for key, values in city_instances.items() if City.state_id == State.id]


