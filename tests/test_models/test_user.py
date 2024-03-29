#!/usr/bin/python3
""" """
import datetime
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.value = User
        self.class_name = self.value.__name__

    def test_first_name(self):
        """ """
        new = self.value(first_name="John")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(last_name="Doe")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(email="johndoe@github.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(password="pwd")
        self.assertEqual(type(new.password), str)

    def test_updated_at(self):
        """ """
        prev = self.value(
            email="qdqsfsde@qdqs.com",
            password="pwd"
        )
        n = prev.to_dict()
        new = self.value(**n)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)
