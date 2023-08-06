#!/usr/bin/python3
"""we create the City class that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """We create public attributes"""
    state_id = ""
    name = ""
