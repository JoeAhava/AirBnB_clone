#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        ''' tests BaseModel init/constructor '''
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.createdAt, DateTime)
        self.assertRaises(TypeError, base_model.width, "hello")
