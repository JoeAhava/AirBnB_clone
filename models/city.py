#!/usr/bin/python3
"""City class that inherit from Basemodel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Simple City model"""
    state_id = ""
    name = ""
