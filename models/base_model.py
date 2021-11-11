#!/usr/bin/Python3
import uuid
from datetime import datetime
"""BaseModel that defines all common attributes/methods for other classes:"""


class BaseModel:
    """Simple Base Model class"""
    def __init__(self, *args, **kwargs):
        """initialize imprtant instance attribute"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        """dictionary representation of an instance (method to_dict())."""

        if "errormessage" not in kwargs:
            for key, value in kwargs.items():
                if key in ["created_at","updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def save(self):
        """Update the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dict format of an object"""
        kvdict = self.__dict__
        strtf = "%Y-%m-%dT%H:%M:%S.%f"
        kvdict["__class__"] = self.__class__.__name__
        kvdict["updated_at"] = self.updated_at.strftime(strtf)
        kvdict["created_at"] = self.created_at.strftime(strtf)
        return kvdict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
