#!usr/bin/python3
import models
import json
"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """Simple file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file_:
            json.dump({
                key: value.to_dict() for key, value in self.__objects.items()},
                file_)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r') as file_:
                jd = json.load(f)
                for key in jd.values():
                    cls = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls)(**key))
        except e:
            pass