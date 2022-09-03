#!/usr/bin/python3
"""
Test BaseModel class module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel
    """

    def test_init(self):
        """
        Test attributes exists
        """
        my_model = BaseModel()
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertEqual(my_model.updated_at.year, my_model.created_at.year)
        self.assertEqual(my_model.updated_at.month, my_model.created_at.month)
        self.assertEqual(my_model.updated_at.day, my_model.created_at.day)
        self.assertEqual(my_model.updated_at.hour, my_model.created_at.hour)
