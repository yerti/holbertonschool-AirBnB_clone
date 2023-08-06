#!/usr/bin/python3
"""I create the statte class that will inherit from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """we create the public attribute"""
    name = ""
