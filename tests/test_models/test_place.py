#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = Place
        self.class_name = self.value.__name__

    def test_city_id(self):
        """ """
        new = self.value(city_id="CA")
        self.assertEqual(new.city_id, "CA")

    def test_user_id(self):
        """ """
        new = self.value(user_id="CA")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(name="My Place")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(description="This is a description")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(number_rooms=4)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=2)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(max_guest=4)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(price_by_night=100)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value(latitude=37.7749)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(longitude=122.4194)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        if (self.db_type == "db"):
            return
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_updated_at(self):
        """ """
        from models.city import City
        from models.user import User
        from models.state import State
        user = User(email="qdqs@qsrsq.com", password="pwd")
        user.save()
        state = State(name="California")
        state.save()
        city = City(name="San Francisco", state_id=state.id)
        city.save()
        prev = self.value(
            name="Wifi",
            city_id=city.id,
            user_id=user.id,
            price_by_night=100,
            number_rooms=4,
            number_bathrooms=2,
            max_guest=4
        )
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
