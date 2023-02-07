#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_save_method(self):
        self.a = BaseModel()
        self.a_upd = self.a.updated_at
        self.a.save()
        self.assertGreater(self.a.updated_at, self.a_upd)

    def test_to_dict(self):
        self.b = BaseModel()
        self.b.name = "airbnb"
        self.b.task = 3
        self.b_dic = self.b.to_dict()
        self.assertEqual(self.b_dic['__class__'], self.b.__class__.__name__)
        self.assertEqual(self.b_dic['name'], "airbnb")
        self.assertEqual(self.b_dic['task'], 3)

    def test_dict_datetime_type(self):
        self.c = BaseModel()
        self.c_dic = self.c.to_dict()
        self.assertIsInstance(self.c_dic['updated_at'], str)
        self.assertIsInstance(self.c_dic['created_at'], str)
