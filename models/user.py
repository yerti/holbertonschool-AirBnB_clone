#!/usr/bin/python3
"""creating a user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """we create public attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
