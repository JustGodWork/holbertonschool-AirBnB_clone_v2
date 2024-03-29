#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = Amenity
        self.class_name = self.value.__name__

    def test_name2(self):
        """ """
        new = self.value(name="Wifi")
        self.assertEqual(new.name, "Wifi")

    def test_updated_at(self):
        """ """
        prev = self.value(name="Wifi")
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
