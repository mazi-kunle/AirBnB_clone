#!/usr/bin/python3
"""
Test State class module
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test State
    """

    def test_attr_type(self):
        """
        Test attributes types
        """
        state = State()
        state.name = ""
        self.assertTrue(type(state.name), str)

    def test_attr_not_none(self):
        """
        Test attributes is not None
        """
        state = State()
        state.name = ""
        self.assertIsNotNone(state.name)
