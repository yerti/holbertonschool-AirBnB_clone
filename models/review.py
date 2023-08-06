#!/usr/bin/python3
"""we create the Review class that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """We create public attributes"""
    place_id = ""
    user_id = ""
    text = ""
