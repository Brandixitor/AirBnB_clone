#!/usr/bin/python3
"""This model defines a base class for all models in this AirBnB Clone"""
import uuid
import datetime from datetime



class BaseModel:
    """A base class for all AirBnB models"""
    def __init__(self, *args, **kwargs):
        """Initialisation of a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)