#!/usr/bin/python3
'''A console for the AirBnb project'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''
    A command line interpreter
    '''
    prompt = '(hbnb) '

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
