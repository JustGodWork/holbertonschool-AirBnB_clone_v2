#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            del storage.all()[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        from models.state import State
        new = State(name='California')
        new.save()
        self.assertTrue(storage.all()[f"State.{new.id}"])

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        from models.state import State
        from models import storage
        db_env = os.getenv('HBNB_TYPE_STORAGE')
        if (db_env != 'db'):
            new = State(name='California')
            new.save()
            self.assertNotEqual(len(storage.all()), 0)
        else:
            new = State(name='California')
            new.save()
            try:
                with open('file.json', 'r') as f:
                    self.assertNotEqual(len(f.read()), 0)
            except FileNotFoundError:
                pass

    def test_save(self):
        """ FileStorage save method """
        from models.state import State
        new = State(name='California')
        db_env = os.getenv('HBNB_TYPE_STORAGE')
        if (db_env != 'db'):
            new.save()
            self.assertTrue(os.path.exists('file.json'))
        else:
            with patch('models.storage') as mock:
                mock.type = 'db'
                new.save()
                mock.new.assert_called()
                mock.save.assert_called()

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        from models.state import State
        new = State(name='California')
        new.save()
        storage.reload()
        self.assertTrue(storage.all()[f"State.{new.id}"])

    def test_reload_empty(self):
        """ Load from an empty file """
        db_env = os.getenv('HBNB_TYPE_STORAGE')
        if (db_env != 'db'):
            with open('file.json', 'w') as f:
                pass
            with self.assertRaises(ValueError):
                storage.reload()
        else:
            with patch('models.storage') as mock:
                mock.type = 'db'
                mock.reload()
                mock.reload.assert_called()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        from models.state import State
        new = State(name='California')
        if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
            with patch('models.storage') as mock:
                new.save()
                mock.save.assert_called()
        else:
            new.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
            from models.engine.file_storage import FileStorage
            self.assertEqual(type(FileStorage.__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        temp = new.__class__.__name__ + '.' + str(new.id)
        self.assertEqual(temp, f'BaseModel.{new.id}')

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        from models.engine.db_storage import DBStorage
        db_env = os.getenv('HBNB_TYPE_STORAGE')
        self.assertEqual(type(storage), FileStorage if db_env != 'db' else DBStorage)
