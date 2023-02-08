#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_instantiation(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_unique_attributes(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_attribute_type(self):
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))
        self.assertEqual(datetime, type(b1.created_at))
        self.assertEqual(datetime, type(b1.updated_at))

    def test_str(self):
        b1 = BaseModel()
        s1 = b1.__str__()
        self.assertIn("[BaseModel] ({})".format(b1.id), s1)
        self.assertIn("'id': '{}'".format(b1.id), s1)
        self.assertIn("'created_at': {}".format(repr(b1.created_at)), s1)
        self.assertIn("'updated_at': {}".format(repr(b1.updated_at)), s1)

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

    def test_recreated_inst_ID(self):
        a = BaseModel()
        a.name = "alx"
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertEqual(a.id, b.id)

    def test_recreated_ins_attr(self):
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertEqual(b.name, "alx")
        self.assertEqual(b.task, 4)

    def test_recreated_ins_created_at_type_is_datetime(self):
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsInstance(b.created_at, datetime)

    def test_recreated_ins_updated_at_type_is_datetime(self):
        a = BaseModel()
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsInstance(b.updated_at, datetime)

    def test_recreated_isnot_original(self):
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsNot(a, b)

    def test_attr_with_empty_kwargs(self):
        a = BaseModel()
        a.name = "africa"
        a_created = a.created_at
        a_dic = a.to_dict()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)
        self.assertGreater(b.created_at, a_created)