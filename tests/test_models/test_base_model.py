#!/usr/bin/python3
""" Test Module for BaseModel class """
import models
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test Case class definition """
    def test_no_args_instantiation(self):
        """ Tests for instance of class object """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_unique_attributes(self):
        """ Attributes of 2 instances of class should not be equal """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_attribute_type(self):
        """ Type of created_at and updated_at is datetime """
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))
        self.assertEqual(datetime, type(b1.created_at))
        self.assertEqual(datetime, type(b1.updated_at))

    def test_str(self):
        """ Test for the returned string for instance """
        b1 = BaseModel()
        s1 = b1.__str__()
        self.assertIn("[BaseModel] ({})".format(b1.id), s1)
        self.assertIn("'id': '{}'".format(b1.id), s1)
        self.assertIn("'created_at': {}".format(repr(b1.created_at)), s1)
        self.assertIn("'updated_at': {}".format(repr(b1.updated_at)), s1)

    def test_new_instance_stored_in_objects(self):
        """ New instance created is stored and can be retrieved """
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_save_method(self):
        """ Instance save method updates the updated_at with datetime.now"""
        a = BaseModel()
        a_upd = a.updated_at
        a.save()
        self.assertGreater(a.updated_at, a_upd)

    def test_save_updates_file(self):
        """Save updates the json file"""
        a = BaseModel()
        a.save()
        a_id = "BaseModel" + "." + a.id
        with open("file.json", "r") as rdfile:
            self.assertIn(a_id, rdfile.read())

    def test_to_dict(self):
        """ Test the dictionary attribute values of instance """
        self.b = BaseModel()
        self.b.name = "airbnb"
        self.b.task = 3
        self.b_dic = self.b.to_dict()
        self.assertEqual(self.b_dic['__class__'], self.b.__class__.__name__)
        self.assertEqual(self.b_dic['name'], "airbnb")
        self.assertEqual(self.b_dic['task'], 3)

    def test_dict_datetime_type(self):
        """ data of updated_at and created_at is string """
        self.c = BaseModel()
        self.c_dic = self.c.to_dict()
        self.assertIsInstance(self.c_dic['updated_at'], str)
        self.assertIsInstance(self.c_dic['created_at'], str)

    def test_recreated_inst_ID(self):
        """ A recreated instance with kwargs assumes all attr from kwargs """
        a = BaseModel()
        a.name = "alx"
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertEqual(a.id, b.id)

    def test_recreated_ins_attr(self):
        """ The attributes are the same for crecreated instance """
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertEqual(b.name, "alx")
        self.assertEqual(b.task, 4)

    def test_recreated_ins_created_at_type_is_datetime(self):
        """ The recreated instance created_at type is datetime """
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsInstance(b.created_at, datetime)

    def test_recreated_ins_updated_at_type_is_datetime(self):
        """ The recreated instance updated_at type is datetime """
        a = BaseModel()
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsInstance(b.updated_at, datetime)

    def test_recreated_isnot_original(self):
        """ The recreated instance is not equal to the original instance """
        a = BaseModel()
        a.name = "alx"
        a.task = 4
        a_dic = a.to_dict()
        b = BaseModel(**a_dic)
        self.assertIsNot(a, b)

    def test_attr_with_empty_kwargs(self):
        """ new instance created without any kwargs """
        a = BaseModel()
        a.name = "africa"
        a_created = a.created_at
        a_dic = a.to_dict()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)
        self.assertGreater(b.created_at, a_created)


if __name__ == "__main__":
    unittest.main()
