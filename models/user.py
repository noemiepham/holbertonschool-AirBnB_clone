#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class defined"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

