#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = City
        self.class_name = self.value.__name__

    def test_state_id(self):
        """ """
        new = self.value(state_id="CA")
        self.assertEqual(new.state_id, "CA")

    def test_name(self):
        """ """
        new = self.value(name="Wifi")
        self.assertEqual(new.name, "Wifi")

    def test_updated_at(self):
        """ """
        from models.state import State
        state = State(name="California")
        state.save()
        prev = self.value(name="Wifi", state_id=state.id)
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
