#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base_model import Base
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_collate': 'utf8mb4_0900_ai_ci'}

    name = Column(String(128), nullable=False)

    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')


    @property
    def cities(self):
        """Returns the list of City instances where state_id equals the current State id"""
        from models import storage
        from models.city import City
        city_instances = storage.all(City).values()
        return [city for city in city_instances if city.state_id == self.id]
