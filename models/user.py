#!usr/bin/pyhton3
""" User that inherits from BaseModel """


from models.base_model import BaseModel


class User(BaseModel):
    """ Simpel user class model """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
