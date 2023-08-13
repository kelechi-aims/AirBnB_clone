#!/usr/bin/python3
'''
This module contains the BaseModel for the AirBnB_clone.
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    BaseModel class that defines common attributes/methods for other classes.

    Public instance attributes:
        id: string - assign with a uuid when an instance is created.
        created_at: datetime - assign with the current datetime
                    when an instance is created.
        updated_at: datetime - assign with the current datetime when
                    an instance is created and it will be updated
                    every time you change your object.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize a new instance of BaseModel.

        Args:
            *args: Additional arguments (not used).
            **kwargs: Keyword arguments for initializing instances.
        '''
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], time_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        Returns string representation of BaseModel instance.
        '''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        Updates the updated_at attribute with the current datetime.
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary representation of BaseModel instance.
        '''
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
