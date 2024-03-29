#!/usr/bin/python3
""" """
from sre_parse import State
from unittest.mock import patch
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.db_type = os.getenv('HBNB_TYPE_STORAGE')
        self.value = BaseModel
        self.class_name = self.value.__name__

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = self.value(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = self.value(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        key = self.class_name + "." + i.id
        if (self.db_type == 'db' and self.value != 'BaseModel'):
            with patch('models.storage') as mock:
                i.save()
                mock.new.assert_called()
                mock.save.assert_called()
        else:
            try:
                with open('file.json', 'r') as f:
                    j = json.load(f)
                    self.assertEqual(j[key], i.to_dict())
            except FileNotFoundError:
                pass

    def test_save2(self):
        """ """
        if ((
            self.db_type == 'db' and self.class_name != 'BaseModel'
            or self.db_type != 'db'
        )):
            with patch('models.storage') as mock:
                mock.type = 'db'
                self.value().save()
                mock.new.assert_called()
                mock.save.assert_called()

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.class_name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        new = self.value(name='test')
        self.assertEqual(new.name, 'test')

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        if (
            self.db_type == 'db' and self.class_name != 'BaseModel'
            or
            self.db_type != 'db'
        ):
            prev = self.value()
            n = prev.to_dict()
            new = self.value(**n)
            new.save()
            self.assertEqual(type(new.updated_at), datetime.datetime)
            self.assertFalse(new.created_at == new.updated_at)
