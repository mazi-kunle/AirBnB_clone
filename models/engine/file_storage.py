#!/usr/bin/python3
'''This module contains the FileStorage class.'''

from datetime import datetime
import json
from os import path

class FileStorage:
    '''
    A class to store data.
    '''
    __file_path = "file.json"
    __objects = {}
    

    def all(self):
        '''
        returns a dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        add new obj to dic
        '''
        new_dict = {}
        for key, value in obj.__dict__.items():
            if key == 'created_at':
                new_dict[key] = datetime.isoformat(value)
            elif key == 'updated_at':
                new_dict[key] = datetime.isoformat(value)
            else:
                new_dict[key] = value

        FileStorage.__objects['BaseModel.'+obj.id] = new_dict
        # print('BaseModel.'+obj.id)
        # print(new_dict)
    
    def save(self):
        """
        serializes data and save to JSON file
        """
        # print('file', type(FileStorage.__objects))
        serialized = json.dumps(FileStorage.__objects)
        # print('serialized', serialized)
        with open(FileStorage.__file_path, 'w') as json_file:
            json_file.write(serialized)

    def reload(self):
        """
        deserializes the JSON file to obj
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as open_file:
                # print(data)
                FileStorage.__objects = json.load(open_file)
