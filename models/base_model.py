#!/usr/bin/python3
"""Contains class BaseModel """


import uuid
import datetime


class BaseModel:
    """The BaseModel class of future classes"""
    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
