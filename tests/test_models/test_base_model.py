#!/usr/bin/python3
from models.base_model import BaseModel
import datetime
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        ''' tests BaseModel init/constructor '''
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        p1 = r'^[0-9a-f]{8}-[0-9a-f]{4}'
        p2 = r'-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
        p3 = r'[0-9a-f]{12}$'
        self.assertRegex(base_model.id, p1+p2+p3, "id is not a valid uuid4")
        self.assertIsInstance(base_model.created_at, datetime.date)
        self.assertIsInstance(base_model.updated_at, datetime.date)

    def test_save(self):
        ''' test BaseModel save '''
        base_model = BaseModel()
        updated_at_prev = base_model.updated_at
        base_model.save()
        self.assertGreater(base_model.updated_at, updated_at_prev)

    def test_to_dict(self):
        ''' test BaaseModel to_dict '''
        base_model = BaseModel()
        model_json = base_model.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertIn('id', model_json)
        self.assertIn('created_at', model_json)
        self.assertIn('updated_at', model_json)
