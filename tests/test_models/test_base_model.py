#!/usr/bin/python3
"""
Test BaseModel class module
"""
from statistics import mode
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel
    """

    def test_init(self):
        """
        Test attributes exists
        """
        model = BaseModel()
        self.assertTrue(type(model.id), str)
        self.assertTrue(type(model.created_at), datetime)
        self.assertTrue(type(model.updated_at), datetime)
        self.assertEqual(model.updated_at.year, model.created_at.year)
        self.assertEqual(model.updated_at.month, model.created_at.month)
        self.assertEqual(model.updated_at.day, model.created_at.day)
        self.assertEqual(model.updated_at.hour, model.created_at.hour)

    def test_str_representaion(self):
        """string representaion test.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(
            str(my_model),
            '[{}] ({}) {}'.format(
                my_model.__class__.__name__,
                my_model.id,
                my_model.__dict__
            )
        )
