#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_no_args_instantiation(self):
        p1 = Place()
        self.assertIsInstance(p1, Place)

    def test_Place_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(Place, BaseModel))
