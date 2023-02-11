#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def test_no_args_instantiation(self):
        c1 = City()
        self.assertIsInstance(c1, City)

    def test_City_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(City, BaseModel))
