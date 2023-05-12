#!/usr/bin/python3
"""
This module defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The Base class"""
    def __init__(self, *args, **kwargs):
        """constructor of a base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at",
                          None) and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at",
                          None) and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.utcnow()
            if kwargs["id"] is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """print formated string"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """updates the publice instance attribute
        updated_at with the current datetime"""
        if self.updated_at is not datetime.now():
            self.updated_at = datetime.now()
        else:
            models.storage.new(self.to_dict())
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = {
            "__class__": self.__class__.__name__
        }
        # update with instance attributes stored under the hood
        my_dict.update(self.__dict__)

        if "created_at" in my_dict:
            my_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in my_dict:
            my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
