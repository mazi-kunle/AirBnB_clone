#!/usr/bin/python3
'''This is a module containing the code for the file storage'''

import json
from os.path import exists as file_exists
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class FileStorage:
    '''
    A file storage class.
    '''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''
        An init function
        '''
        pass

    def all(self):
        '''
        returns the dictionary objects.
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serialize __objects to the json file.
        '''
        # extract all the attributes of the instance to a dictionary.
        json_dict = {}
        for key in self.__objects:
            json_dict[key] = self.__objects[key].to_dict()

        # write the dictionary to a json file.
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        # check if file exists
        if (file_exists(self.__file_path)):
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key in json_obj:
                self.__objects[key] = \
                        classes[json_obj[key]['__class__']](**json_obj[key])
