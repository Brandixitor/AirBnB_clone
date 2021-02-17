#!/usr/bin/python3
"""This is the Review Model module.

Contains the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a Review.

    Attributes:
        place_id (str): the review's place id.
        user_id (str): the review's issuer user id.
        text (str): the review.
    """

    place_id = ""
    user_id = ""
    text = ""
