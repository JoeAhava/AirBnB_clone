#!/usr/bin/python3
from models.base_model import BaseModel
"""class Place inherit from BaseModel"""


class Place(BaseModel):
    """Simple Place model"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest: integer = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
