#!/usr/bin/python3
from models.base_model import BaseModel
"""Review class inherit from BaseModel"""


class Review(BaseModel):
    """simple Review model"""

    place_id = ""
    user_id = ""
    text = ""
