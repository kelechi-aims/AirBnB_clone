#!/usr/bin/python3
'''
Module for the class FileSorage
'''
import json
from os.path import exists


class FileStorage:
    '''
    This class handles the serializes instances and deserializes
    of instances to/from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary to store objects b class name and id

    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary of objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Adds a new object to the dictionary.

        Args:
            obj (BaseModel): The object to be added.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialises and saves the objects to the JSON file.
        '''
        serialized = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        '''
        Deserializes and loads the objects from the JSON file.
        '''
        from models.base_model import BaseModel
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r')as file:
                data = json.load(file)
                for key, value in data.items():
                   class_name = value['__class__']
                   self.new(eval(class_name)(**value))
