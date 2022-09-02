#!/usr/bin/python3
'''This is the module for the review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A Review class
    '''
    place_id = ""
    user_id = ""
    text = ""
