#!/usr/bin/python3
'''A console for the AirBnb project'''

import cmd
from models.base_model import BaseModel
from models import storage
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


class HBNBCommand(cmd.Cmd):
    '''
    A command line interpreter
    '''
    prompt = '(hbnb) '

    def do_create(self, line):
        '''Create a new instance of a class'''

        if len(line) == 0:
            print('** class name missing **')

        elif line not in classes:
            print("** class doesn't exist **")

        else:
            newInstance = classes[line]()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, line):
        '''
        prints the string representation of an instance based on class and id.
        '''

        if len(line) == 0:
            print('** class name missing **')
            return

        data = line.partition(' ')
        if data[0] not in classes:
            print("** class doesn't exist **")
            return

        if not data[2]:
            print('** instance id missing **')
            return

        _cls, _id = data[0], data[2]
        key = _cls + '.' + _id

        try:
            print(storage._FileStorage__objects[key])

        except KeyError:
            print('** no instance found **')

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        '''

        if len(line) == 0:
            print('** class name missing **')
            return

        data = line.partition(' ')
        _cls = data[0]
        _id = data[2]

        if _cls not in classes:
            print("** class doesn't exist **")
            return

        if not _id:
            print('** instance id missing **')
            return

        key = _cls + '.' + _id

        try:
            del(storage.all()[key])
            storage.save()

        except KeyError:
            print('** no instance found **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        '''

        if line not in classes and len(line) != 0:
            print("** class doesn't exist **")
            return

        _list = []

        if line:
            line = line.split(' ')[0]
            for key, value in storage.all().items():
                if key.split('.')[0] == line:
                    _list.append(str(value))

        else:
            for key, value in storage.all().items():
                _list.append(str(value))

        print(_list)

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        '''

        if len(line) == 0:
            print('** class name missing **')
            return

        data = line.split(' ')
        # check if class exist
        if data[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(data) == 1:
            print('** instance id missing **')
            return

        key = data[0] + '.' + data[1]

        try:
            # check if the id exists.
            instance = storage.all()[key]

        except KeyError:
            print('** no instance found **')
            return
        # check if the attribute name exists.
        if len(data) == 2:
            print('** attribute name missing **')
            return

        if len(data) == 3:
            print('** value missing **')
            return

        attribute_name = data[2]
        attribute_value = data[3]

        try:
            # cast the attribute_value to the attribute type
            instance_dict = instance.__dict__
            _type = type(instance_dict[attribute_name])

            if _type == str:
                attribute_value = eval(attribute_value)

            if _type == int:
                attribute_value = int(eval(attribute_value))

            if _type == float:
                attribute_value = float(eval(attribute_value))

            instance_dict[attribute_name] = attribute_value

        except KeyError:
            if eval(attribute_value).isdigit():
                instance_dict[attribute_name] = int(eval(attribute_value)

            else:
                instance_dict[attribute_name] = eval(attribute_value)

        finally:
            # save the updated instance.
            instance.save()

    def do_count(self, line):
        '''
        retrieve the number of instances of a class
        '''
        count = 0

        for key, value in storage.all().items():
            if (line == key.split('.')[0]):
                count += 1

        print(count)

    def do_quit(self, line):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, line):
        '''command line interpreter is exited on EOF'''

        print()
        return True

    def emptyline(self):
        pass

    def default(self, line):
        '''
        retrive all instances of a class by using: <class name>.all()
        '''
        commands = {
                'all': self.do_all,
                'count': self.do_count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
                }
        # run only commands that has '.', '(', and ')'
        if not ('.' in line and '(' in line and ')' in line):
            super().default(line)
            return

        # extract class name
        _cls = line.split('.')[0]

        # extract the command from line e.g
        # <class name>.count()
        # command = count
        command = line[line.find('.') + 1:line.find('(')]

        if command not in commands.keys():
            super().default(line)
            return

        # extract details from line
        if command in ['show', 'destroy']:
            start = line.find('(')
            end = line.find(')')
            _id = line[start + 2:end - 1]
            cmd = f'{_cls} {_id}'

        elif command == 'update':
            data = eval(line[line.find('('):line.find(')')+1])

            if type(data[1]) == dict:
                _id, attr_dict = data

                for key, value in attr_dict.items():
                    attr_name = key
                    attr_val = value
                    cmd = f'{_cls} {_id} {attr_name} "{attr_val}"'
                    commands[command](cmd)

                return

            else:
                _id, attr_name, attr_val = data
                cmd = f'{_cls} {_id} {attr_name} "{attr_val}"'

        else:
            cmd = f'{_cls}'
        commands[command](cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
