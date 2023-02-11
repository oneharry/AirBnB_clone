#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def test_no_args_instantiation(self):
        u1 = User()
        self.assertIsInstance(u1, User)
    def test_User_inherits_from_BaseModel(self):
        u1 = User()
        self.assertIsInstance(u1, BaseModel)
