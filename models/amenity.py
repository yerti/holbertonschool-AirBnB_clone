#!/usr/bin/python3
"""We create the Amenity class that inherits from BaseModel"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """We create public attributes"""
    name = ""
