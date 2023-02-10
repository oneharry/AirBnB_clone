#!/usr/bin/python3
""" Entry point to the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Definition of command interpreter class"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """ Exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Does nothing when no command is passed """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if args:
            try:
                largs = args.split()
                cls = largs[0]
                obj = HBNBCommand.classes[cls]()
                storage.save()
                print("{}".format(obj.id))
            except KeyError:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on
        the class name and id
        """
        if args:
            largs = args.split()
            cls = largs[0]
            if cls in self.classes:
                if len(largs) == 1:
                    print("** instance id missing **")
                else:
                    try:
                        cid = largs[1]
                        dobj = storage.all()
                        print(dobj["{}.{}".format(cls, cid)])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        dic = storage.all()
        if args:
            largs = args.split()
            cls = largs[0]
            if cls not in self.classes:
                print("** class doesn't exist **")
                return
            dic = dict(filter(lambda x: type(x[1]) == eval(cls), dic.items()))
        lobj = [str(v) for k, v in dic.items()]
        print(lobj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
