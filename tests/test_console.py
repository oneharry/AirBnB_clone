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


class TestConsole(unittest.TestCase):
    """Specific tests for the console"""
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

    def test_show_instance(self):
        """ Test: returns the str representation of instance """
        pass


if __name__ == "__main__":
    unittest.main()
