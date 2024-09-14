#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        if obj is produced it only returns the object od that class
        """
        if cls:
            # filter and return only the objects for the specified class
            filtered_objects = {key:obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}
            return filtered_objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.__class__.__name__+ '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                obj_dict = val.to_dict()
                temp[key] = obj_dict
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val.pop('__class__', None)
                    if class_name:
                        cls = classes.get(class_name)
                        if cls:
                            # Create a new instance of the class
                            obj = cls(**val)
                            self.all()[key] = obj

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

        if '_sa_instance_state' in FileStorage.__objects.keys():
            del FileStorage.__objects['_sa_instance_state']

    def delete(self, obj=None):
        """ Deletes obj from __objects dictionary id it exists"""
        if obj:
            obj_key = f'{obj.__class__.__name__}.{obj.id}'
            if obj_key in FileStorage.__objects:
                del FileStorage.__objects[obj_key]

    def close(self):
        """ method for deserializing the json file to objects"""
        self.reload()

