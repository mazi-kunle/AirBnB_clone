#!/usr/bin/python3
"""
Test User class module
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test User
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        user = User()
        user.email = ""
        user.password = ""
        user.first_name = ""
        user.last_name = ""
        self.assertTrue(type(user.email), str)
        self.assertTrue(type(user.password), str)
        self.assertTrue(type(user.first_name), str)
        self.assertTrue(type(user.last_name), str)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        user = User()
        user.email = ""
        user.password = ""
        user.first_name = ""
        user.last_name = ""
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.password)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)
