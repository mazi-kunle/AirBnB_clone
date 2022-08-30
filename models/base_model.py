#!/usr/bin/python3
'''This module contains the baseModel class.'''

from datetime import datetime
import uuid


class BaseModel:
    '''
    A class that defines all common attributes/methods for other classes.
    '''
    def __init__(self):
        '''
        An init function.
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        A custom __str__ method
        '''
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        '''
        updates the public instance attribute updated_at with
        the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of
        __dict__ of the instance.
        '''
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                new_dict[key] = datetime.isoformat(value)
            elif key == 'updated_at':
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value

        new_dict['__class__'] = 'BaseModel'

        return new_dict