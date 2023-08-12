#!/usr/bin/python
"""class review that inherits from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Rep of the class and its attributes
    """
    place_id = ''
    user_id = ''
    text = ''
