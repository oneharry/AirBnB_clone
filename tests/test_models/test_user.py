#!/usr/bin/python3
""" Test Module for testing class User """
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ TestClass definition """
    def test_no_args_instantiation(self):
        """ Tests for the instance of class object """
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_User_inherits_from_BaseModel(self):
        """ Tests if class user inherited from class BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ Validates that User has necessary attributes"""
        self.assertTrue(hasattr(User(), "email"))
        self.assertTrue(hasattr(User(), "password"))
        self.assertTrue(hasattr(User(), "last_name"))
        self.assertTrue(hasattr(User(), "first_name"))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        self.assertEqual(str, type(User().id))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
