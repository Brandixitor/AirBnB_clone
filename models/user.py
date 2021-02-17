#!/usr/bin/python3
"""This is the User Model module.

Contains the User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a User.

    Attributes:
        email (str): the user's email.
        password (str): the user's password.
        first_name (str): the user's first_name.
        last_name (str): the user's last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
