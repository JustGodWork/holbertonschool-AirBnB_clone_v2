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
            Test create command with valid class
            and different types of params
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(
                "create BaseModel name=\"John\" age=30 weight=75.5"
            )
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
                self.assertNotEqual(
                    f.getvalue(),
                    "** class doesn't exist **\n"
                )
                self.assertNotEqual(
                    f.getvalue(),
                    "** class name missing **\n"
                )

    def test_create_state_dbstorage(self):
        """
        Test create command with dbstorage for State and City
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                mock_storage.type = 'db'
                self.cli.onecmd("create State name=\"California\"")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(
                    f.getvalue(),
                    "** class doesn't exist **\n"
                )
                self.assertNotEqual(
                    f.getvalue(),
                    "** class name missing **\n"
                )

    def test_create_state_and_city_dbstorage(self):
        """
        Test create command with dbstorage for State and City
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                mock_storage.type = 'db'
                self.cli.onecmd("create State name=\"California\"")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(
                    f.getvalue(),
                    "** class doesn't exist **\n"
                )
                self.assertNotEqual(
                    f.getvalue(),
                    "** class name missing **\n"
                )
                self.cli.onecmd(f"create City state_id=\"{f.getvalue()}\" name=\"Fremont\"")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called()
                self.assertNotEqual(
                    f.getvalue(),
                    "** class doesn't exist **\n"
                )
                self.assertNotEqual(
                    f.getvalue(),
                    "** class name missing **\n"
                )

    def test_create_state_and_city_dbstorage_with_spacer(self):
        """
        Test create command with dbstorage for State and City
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                from models.state import State
                from models.city import City
                mock_storage.type = 'db'
                # Create and save State
                state = State(name="California")
                state.save()
                mock_storage.new.assert_called_with(state)
                mock_storage.save.assert_called()
                # Create and save City
                city = City(state_id=state.id, name="San_Francisco")
                city.save()
                mock_storage.new.assert_called_with(city)
                mock_storage.save.assert_called()

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
                self.assertNotEqual(
                    f.getvalue(),
                    "** class doesn't exist **\n"
                )
                self.assertNotEqual(
                    f.getvalue(),
                    "** class name missing **\n"
                )

    def test_create_state_city_user_place_dbstorage(self):
        """
            Test create command with dbstorage
            for State, City, User, and Place
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place

        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.storage') as mock_storage:
                mock_storage.type = 'db'
                # Create and save State
                state = State(name="California")
                state.save()
                mock_storage.new.assert_called_with(state)
                mock_storage.save.assert_called()
                # Create and save City
                city = City(
                    state_id=state.id,
                    name="San_Francisco_is_super_cool"
                )
                city.save()
                mock_storage.new.assert_called_with(city)
                mock_storage.save.assert_called()
                # Create and save User
                user = User(
                    email="my@me.com",
                    password="pwd",
                    first_name="FN",
                    last_name="LN"
                )
                user.save()
                mock_storage.new.assert_called_with(user)
                mock_storage.save.assert_called()
                # Create and save Place
                place = Place(
                    city_id=city.id,
                    user_id=user.id,
                    name="My_house",
                    description="A house",
                    number_rooms=4,
                    number_bathrooms=2,
                    max_guest=10,
                    price_by_night=100,
                    latitude=37.7749,
                    longitude=122.4194
                )
                place.save()
                mock_storage.new.assert_called_with(place)
                mock_storage.save.assert_called()


if __name__ == '__main__':
    unittest.main()
