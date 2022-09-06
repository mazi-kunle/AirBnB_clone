#!/usr/bin/python3
"""
Test Amenity class module
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test Amenity
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        city = Amenity()
        city.name = ""
        self.assertTrue(type(city.name), str)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        city = Amenity()
        city.name = ""
        self.assertIsNotNone(city.name)
