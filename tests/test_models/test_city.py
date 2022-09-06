#!/usr/bin/python3
"""
Test City class module
"""
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """
    Test City
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        city = City()
        city.state_id = ""
        city.name = ""
        self.assertTrue(type(city.state_id), str)
        self.assertTrue(type(city.name), str)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        city = City()
        city.state_id = ""
        city.name = ""
        self.assertIsNotNone(city.state_id)
        self.assertIsNotNone(city.name)
