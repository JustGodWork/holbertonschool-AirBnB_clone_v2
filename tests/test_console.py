#!/usr/bin/python3
"""
    Unittest for console class
"""


import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBTNCommand(unittest.TestCase):
    """
    Test cases for the console
    """
    def setUp(self):
        self.cli = HBNBCommand()

    def test_do_create_no_args(self):
        """
        Test create command with no arguments
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        """
        Test create command with invalid class
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_create_valid_class_no_params(self):
        """
        Test create command with valid class and no params
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_valid_class_with_params(self):
        """
        Test create command with valid class and params
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel name=\"John\"")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_valid_class_with_param_int(self):
        """
        Test create command with valid class and integer param
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel number=89")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_valid_class_with_param_float(self):
        """
        Test create command with valid class and float param
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel number=89.9")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_valid_class_with_invalid_params(self):
        """
        Test create command with valid class and invalid params
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel name")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_valid_class_with_different_types_of_params(self):
        """
        Test create command with valid class and different types of params
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel name=\"John\" age=30 weight=75.5")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_dbstorage(self):
        """
        Test create command with dbstorage
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                mock_storage.type = 'db'
                self.cli.onecmd("create BaseModel name=\"John\"")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
                self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_dbstorage_many_args(self):
        """
        Test create command with dbstorage
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                from models.state import State
                mock_storage.type = 'db'
                state = State(name="California")
                state.save()
                self.cli.onecmd("create City state_id=\"{}\" name=\"San Francisco\"".format(state.id))
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
                self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_filestorage(self):
        """
        Test create command with filestorage
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                mock_storage.type = 'file'
                self.cli.onecmd("create BaseModel name=\"John\"")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
                self.assertNotEqual(f.getvalue(), "** class name missing **\n")


if __name__ == '__main__':
    unittest.main()
