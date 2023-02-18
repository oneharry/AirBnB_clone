#!/usr/bin/python3
""" Test Module for class State """
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test State definition"""
    def test_no_args_instantiation(self):
        """ test for instance of objest """
        st = State()
        self.assertIsInstance(st, State)

    def test_State_inherits_from_BaseModel(self):
        """ Tests if class State inherited class BaseModel """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """ Validates that State has necessary attributes"""
        st = State()

        self.assertTrue(hasattr(st, "name"))

    def test_new_instance_stored_in_objests(self):
        self.assertIn(State(), storage.all().values())

    def test_attribute_types(self):
        """Validates attribute types"""
        st = State()

        self.assertEqual(str, type(st.id))
        self.assertEqual(datetime, type(st.created_at))
        self.assertEqual(datetime, type(st.updated_at))
        self.assertEqual(str, type(st.name))


if __name__ == "__main__":
    unittest.main()
