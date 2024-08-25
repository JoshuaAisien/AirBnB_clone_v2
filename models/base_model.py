#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
import uuid
from datetime import datetime
import models


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    create_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
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
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ a new public instance method: def delete(self):
         to delete the current instance from the storage (models.storage) by calling the method delete
         """
        models.storage.delete(self)


