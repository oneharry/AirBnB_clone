#!/usr/bin/python3
"""This module contains tests for the console"""
import sys
sys.path.insert(0, '../')  # noqa: E402
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class TestConsole(unittest.TestCase):
    """Specific tests for the console"""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_prompt(self):
        """ tests for the prompt value """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_help_cmd(self):
        """ Tests help quit """
        msg = "Exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), msg)

    def test_quit(self):
        """ Test: quit cmd exits the program """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_emptyline(self):
        """ Test: emptyline """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test: EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    """==== Specific tests for the Create method ===="""

    def test_create_without_Class(self):
        """ Test: create cmd with missing class name """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_with_incorrect_Class(self):
        """ Test: create cmd with non existent class name """
        msg = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NoClass")
            self.assertEqual(f.getvalue().strip(), msg)

    def test_create_BaseModel(self):
        """ Test: outputs id of BaseModel Instance created """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip())

    def test_create_User(self):
        """ Test: outputs id of User Instance created """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(f.getvalue().strip())

    def test_create_City(self):
        """ test: outputs id of instance of City cretaed """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertTrue(f.getvalue().strip())

    def test_create_Place(self):
        """ Test: outputs id of Place instance created """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertTrue(f.getvalue().strip)

    """==== Specific tests for the Show method ===="""

    def test_show_without_classname(self):
        """ Test: outputs the erromessage without class"""
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), msg)

    def test_show_with_invalid_classname(self):
        """ Test: with an invalid class """
        msg = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show InvalidClass")
            self.assertEqual(f.getvalue().strip(), msg)

    def test_show_without_ID(self):
        """ Test without an ID argument """
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), msg)

    def test_show_with_invalid_ID(self):
        """ Test with invalid instance ID """
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 8747839280")
            self.assertEqual(f.getvalue().strip(), msg)

    """==== Specific tests for the All method ===="""

    def test_all_no_args(self):
        """Test the all method with no args: class, id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_all_invalid_class(self):
        """Tests the invalid class"""
        msg = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), msg)


class TestConsoleMethodsWithArgs(unittest.TestCase):
    """Test other console methods with arguments"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

        # Create two BaseModel, User, Review, State, City, Amenity, Place instances each
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()
        cls.user1 = User()
        cls.user2 = User()
        cls.review1 = Review()
        cls.review2 = Review()
        cls.state1 = State()
        cls.state2 = State()
        cls.city1 = City()
        cls.city2 = City()
        cls.amenity1 = Amenity()
        cls.amenity2 = Amenity()
        cls.place1 = Place()
        cls.place2 = Place()

    @classmethod
    def tearDownClass(cls):
        """Tear down for the test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


    def test_all_BaseModel(self):
        """Tests all BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("{}".format(self.base1), f.getvalue())
            self.assertIn("{}".format(self.base2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.base1, self.base2)

    def test_BaseModel_all(self):
        """Tests BaseModel.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIn("{}".format(self.base1), f.getvalue())
            self.assertIn("{}".format(self.base2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.base1, self.base2)

    def test_Review_all(self):
        """Tests Review.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            self.assertIn("{}".format(self.review1), f.getvalue())
            self.assertIn("{}".format(self.review2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.review1, self.review2)

    def test_User_all(self):
        """Tests User.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            self.assertIn("{}".format(self.user1), f.getvalue())
            self.assertIn("{}".format(self.user2), f.getvalue())
            self.assertNotIn("{}".format(self.base1), f.getvalue())
            self.assertNotEqual(self.user1, self.user2)

    def test_State_all(self):
        """Tests State.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            self.assertIn("{}".format(self.state1), f.getvalue())
            self.assertIn("{}".format(self.state2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.state1, self.state2)

    def test_City_all(self):
        """Tests City.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            self.assertIn("{}".format(self.city1), f.getvalue())
            self.assertIn("{}".format(self.city2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.city1, self.city2)

    def test_Amenity_all(self):
        """Tests Amenity.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertIn("{}".format(self.amenity1), f.getvalue())
            self.assertIn("{}".format(self.amenity2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.amenity1, self.amenity2)

    def test_Place_all(self):
        """Tests Place.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            self.assertIn("{}".format(self.place1), f.getvalue())
            self.assertIn("{}".format(self.place2), f.getvalue())
            self.assertNotIn("{}".format(self.user1), f.getvalue())
            self.assertNotEqual(self.place1, self.place2)

if __name__ == "__main__":
    unittest.main()
