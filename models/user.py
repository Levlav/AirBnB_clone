#!/usr/bin/python
"""class User that inherits from the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent the class user and her attributes
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
