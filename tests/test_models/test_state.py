#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def test_no_args_instantiation(self):
        s1 = State()
        self.assertIsInstance(s1, State)

    def test_State_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(State, BaseModel))
