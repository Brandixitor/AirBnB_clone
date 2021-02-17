#!/usr/bin/python3
"""This is the Base Model module.

Contains the BaseModel class which will be the
"base" of all other classes in this project.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """This class will be the “base” of all other classes in this project.

    The goal is to manage all common attributes and methods for other classes.

    Attributes:
        id (str): unique random ID for each BaseModel instance.
        created_at (datetime): the current datetime when instance is created.
        updated_at (datetime): the current datetime when instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the default attributes of the BaseModel object.

        Args:
            *args: unused.
            **kwargs (dict): a dictionary containing wanted attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with all the keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
