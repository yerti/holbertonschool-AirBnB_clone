#!/usr/bin/python3
"""
create new class
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict
