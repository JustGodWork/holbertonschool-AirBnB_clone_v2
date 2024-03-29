#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
),


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review",
            cascade="all, delete",
            backref="place"
        )
        amenity_ids = []
        amenities = relationship(
            "Amenity",
            secondary='place_amenity',
            viewonly=False,
            back_populates="place_amenities"
        )
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id"""
            reviews_list = []
            from models import storage
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """
                Getter attribute that returns the list of
                Amenity instances based on the attribute
                amenity_ids that contains all the Amenity.id
            """
            amenities_list = []
            from models import storage
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """
                Setter attribute that handles append
                method for adding an Amenity.id
                to the attribute amenity_ids
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
