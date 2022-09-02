#!/usr/bin/python3
'''This module contains the baseModel class.'''

from datetime import datetime
import uuid
import models


class BaseModel:
    '''
    A class that defines all common attributes/methods for other classes.
    '''
    def __init__(self, *args, **kwargs):
        '''
        An init function.
        '''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(kwargs[key])
                if key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        A custom __str__ method
        '''
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''
        updates the public instance attribute updated_at with
        the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

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

        new_dict['__class__'] = str(type(self).__name__)

        return new_dict
