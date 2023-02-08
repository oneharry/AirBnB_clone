#!/usr/bin/python3
""" Entry point to the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Deinition of command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Does nothing when no command is passed """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
