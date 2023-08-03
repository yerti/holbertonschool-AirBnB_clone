#!/usr/bin/python3
"""Contains class BaseModel """

from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict.pop("__class__", None)
        return new_dict
