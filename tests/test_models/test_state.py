#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = State
        self.class_name = self.value.__name__

    def test_name3(self):
        """ """
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)

    def test_updated_at(self):
        """ """
        prev = self.value(name="California")
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
