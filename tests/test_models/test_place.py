#!/usr/bin/python3
"""
Test Place class module
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test Place
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        place = Place()
        place.city_id = ""
        place.user_id = ""
        place.name = ""
        place.description = ""
        place.number_rooms = 0
        place.number_bathrooms = 0
        place.max_guest = 0
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = []
        self.assertTrue(type(place.city_id), str)
        self.assertTrue(type(place.user_id), str)
        self.assertTrue(type(place.name), str)
        self.assertTrue(type(place.description), str)
        self.assertTrue(type(place.number_bathrooms), int)
        self.assertTrue(type(place.max_guest), int)
        self.assertTrue(type(place.price_by_night), int)
        self.assertTrue(type(place.number_rooms), int)
        self.assertTrue(type(place.number_rooms), float)
        self.assertTrue(type(place.number_rooms), float)
        self.assertTrue(type(place.amenity_ids), list)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        place = Place()
        place.city_id = ""
        place.user_id = ""
        place.name = ""
        place.description = ""
        place.number_rooms = 0
        place.number_bathrooms = 0
        place.max_guest = 0
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = []
        self.assertIsNotNone(place.city_id)
        self.assertIsNotNone(place.user_id)
        self.assertIsNotNone(place.name)
        self.assertIsNotNone(place.description)
        self.assertIsNotNone(place.number_rooms)
        self.assertIsNotNone(place.number_bathrooms)
        self.assertIsNotNone(place.max_guest)
        self.assertIsNotNone(place.price_by_night)
        self.assertIsNotNone(place.latitude)
        self.assertIsNotNone(place.longitude)
        self.assertIsNotNone(place.amenity_ids)
