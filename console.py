#!/usr/bin/python3
'''A console for the AirBnb project'''

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    A command line interpreter
    '''
    prompt = '(hbnb) '

    def do_create(self, line):
        '''Create a new instance of BaseModel'''

        if len(line) == 0:
            print('** class name missing **')

        elif line != 'BaseModel':
            print("** class doesn't exist **")

        else:
            newInstance = BaseModel()
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
        if data[0] != 'BaseModel':
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

        if _cls != 'BaseModel':
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

        if line != 'BaseModel' and len(line) != 0:
            print("** class doesn't exist **")
            return

        _list = []

        for key, value in storage.all().items():
            _list.append(str(value))

        print(_list)

    def do_quit(self, line):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, line):
        '''command line interpreter is exited on EOF'''

        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
