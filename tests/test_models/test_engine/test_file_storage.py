#!/usr/bin/python3
""" Test Module for FileStorage class """
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Test Class definition """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_no_args_instantiation(self):
        """ Test for an instance of FileStorage """
        f1 = FileStorage()
        self.assertIsInstance(f1, FileStorage)

    def test_arg_instantiation(self):
        """ Test for instantiation of FileStorage with args """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_new(self):
        """ Tests that new objects are stored in the __objects  attribute"""
        f1 = storage.all()
        b1 = BaseModel()
        b1_id = "BaseModel" + "." + b1.id
        self.assertIn(b1_id, f1.keys())
        self.assertIn(b1, f1.values())

    def test_all_one_instance(self):
        """ Tests the all method returns one object"""
        FileStorage._FileStorage__objects = {}
        b1 = BaseModel()
        f1 = storage.all()
        self.assertEqual(1, len(f1))

    def test_all_more_instances(self):
        """ Tests the all method returns all objects"""
        FileStorage._FileStorage__objects = {}
        u1 = User()
        s1 = State()
        p1 = Place()
        r1 = Review()
        a1 = Amenity()
        f1 = storage.all()
        self.assertEqual(5, len(f1))


if __name__ == "__main__":
    unittest.main()
