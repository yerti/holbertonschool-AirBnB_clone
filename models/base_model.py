#!/usr/bin/python3
"""Contains class BaseModel """

from datetime import datetime
from uuid import uuid4
import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """contructor"""
        if kwargs != {}:
            for kwargs, vars in kwargs.items():
                if kwargs != "__class__":
                    setattr(self, kwargs, vars)
                if kwargs == "updated_at":
                    self.updated_at = datetime.strptime(vars, "%Y-%m-%dT%H:%M:%S.%f")
                if kwargs == "created_at":
                    self.created_at = datetime.strptime(vars, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    storage.new(self)
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.datetime.now()
                    self.updated_at = self.created_at

    def __str__(self):
        """Returns us in chain"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
