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

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
