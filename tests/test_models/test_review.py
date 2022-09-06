#!/usr/bin/python3
"""
Test Review class module
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test Review
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        review = Review()
        review.place_id = ""
        review.user_id = ""
        review.text = ""
        self.assertTrue(type(review.place_id), str)
        self.assertTrue(type(review.user_id), str)
        self.assertTrue(type(review.text), str)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        review = Review()
        review.place_id = ""
        review.user_id = ""
        review.text = ""
        self.assertIsNotNone(review.place_id)
        self.assertIsNotNone(review.user_id)
        self.assertIsNotNone(review.text)
