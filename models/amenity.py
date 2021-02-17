#!/usr/bin/python3
"""This is the Amenity Model module.

Contains the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines an Amenity.

    Attributes:
        name (str): the amenity's name.
    """

    name = ""
