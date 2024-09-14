#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
import uuid
from datetime import datetime
import models
import json


Base = declarative_base() #This base class is used to define all the tables in your database as Python classes, with the columns as class attributes.
class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        if not kwargs:
            # New instance creation
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # Update dict with kwargs
            self.__dict__.update(kwargs)

            # dynamically set attributes with values
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            # Convert strings to datetime objects
            if 'created_at' in kwargs and isinstance(kwargs['created_at'], str):
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()

            if 'updated_at' in kwargs and isinstance(kwargs['updated_at'], str):
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

            # If id is not provided, assume this is a new instance and add it to storage
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f"{cls} {self.id} {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance to dictionary for JSON serialization"""
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_sa_instance_state"):
                continue  # Skip this key

            if isinstance(value, datetime):
                # Convert datetime to ISO 8601 string
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value

        # Add class name to the dictionary
        obj_dict['__class__'] = self.__class__.__name__

        # Delete `_sa_instance_state` if it exists in `self.__dict__`
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']

        return obj_dict

    def delete(self):
        """ a new public instance method: def delete(self):
         to delete the current instance from the storage (models.storage) by calling the method delete
         """
        models.storage.delete(self)


