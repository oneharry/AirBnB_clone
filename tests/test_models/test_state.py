#!/usr/bin/python3
""" Test Module for class State """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test State definition """
    def test_no_args_instantiation(self):
        """ Tests for thr instance type """
        s1 = State()
        self.assertIsInstance(s1, State)

    def test_State_inherits_from_BaseModel(self):
        """ Tests if class State inherited from class BaseModel """
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
