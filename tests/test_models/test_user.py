#!/usr/bin/python3
""" Test Module for testing class User """
import unittest
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


if __name__ == "__main__":
    unittest.main()
