#!/usr/bin/python3
'''This is the test for the file storage class.'''

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''
    Test FileStorage.
    '''
    def test_all(self):
        '''
        Test the all method.
        '''
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__objects, fs.all())
