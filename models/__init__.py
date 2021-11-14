#!/usr/bin/python3

""" BaseModel that defines all common attributes/methods for other classes """

from models.engine.file_storage import FileStorage
"""Instance of FileStorage class"""


storage = FileStorage()
storage.reload()
