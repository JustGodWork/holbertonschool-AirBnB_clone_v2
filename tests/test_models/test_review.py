#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = Review
        self.class_name = self.value.__name__

    def test_place_id(self):
        """ """
        new = self.value(place_id="CA")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value(user_id="CA")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value(text="This is a text")
        self.assertEqual(type(new.text), str)

    def test_updated_at(self):
        """ """
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.state import State
        user = User(email="qdqs@qsrsq.com", password="pwd")
        user.save()
        state = State(name="California")
        state.save()
        city = City(name="San Francisco", state_id=state.id)
        city.save()
        place = Place(
            name="Wifi",
            city_id=city.id,
            user_id=user.id,
            price_by_night=100,
            number_rooms=4,
            number_bathrooms=2,
            max_guest=4
        )
        place.save()
        prev = self.value(
            place_id=place.id,
            user_id=user.id,
            text="This is a text"
        )
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
