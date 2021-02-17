#!/usr/bin/python3
"""This is the City Model module.

Contains the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a City.

    Attributes:
        state_id (str): the city's state id.
        name (str): the city's name.
    """

    state_id = ""
    name = ""
