#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os
# retrieve the storage type from environmental variables
storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    # create an instance of DBstorage and store it in the instance storage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    # create an instance of FIlestorage and store it in the instance storage
    storage = FileStorage()

# to load the initilize storage, creating tables or load from file
storage.reload()
