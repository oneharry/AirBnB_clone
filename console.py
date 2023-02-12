#!/usr/bin/python3
""" Entry point to the command interpreter"""
import cmd
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Definition of command interpreter class"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review
               }

    def do_quit(self, line):
        """ Exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ Does nothing when no command is passed """
        pass

    def do_destroy(self, line):
        """ Deletes an instance based on the <class name> and <id> """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] and not args[0] in self.classes:
            print("** class doesn't exist **")
        elif args[0] and len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            obj = storage.all()
            del obj[args[0] + "." + args[1]]
            storage.save()

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

    def do_update(self, line):
        """
        Updates an instance based on the <class name> and <id> by:
            adding or updating attribute( save the change into JSON file)
        """
        args = shlex.split(line)
        objs = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] and not args[0] in self.classes:
            print("** class doesn't exist **")
        elif args[0] and len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in objs.keys():
            print("** no instance found **")
        elif args[0] and args[1] and len(args) < 3:
            print("** attribute name missing **")
        elif args[2] and len(args) < 4:
            print("** value missing **")
        else:
            my_obj = objs[args[0] + "." + args[1]]
            if args[3].isdigit():
                val = int(args[3])
            elif args[3].isdecimal():
                val = float(args[3])
            else:
                val = str(args[3])

            my_obj.__dict__[args[2]] = args[3]
            storage.save()

    def do_count(self, args):
        """
        Retrieves the number of instances of a class
        """
        dic = storage.all()
        count = 0
        if args:
            largs = args.split()
            cls = largs[0]
            if cls not in self.classes:
                print("** class doesn't exist **")
                return False
            dic = dict(filter(lambda x: type(x[1]) == eval(cls), dic.items()))
        print(len(dic))

    def default(self, line):
        """
        Method called on an input line when the command prefix
        is not recognized.
        """
        methods = {
                "all": self.do_all,
                "show": self.do_show,
                "count": self.do_count,
                "destroy": self.do_destroy,
                "update": self.do_update
                }

        args = line.split(".")
        try:
            clsname = args[0]
            mtd_val = args[1].split("(")
            method = mtd_val[0]

            if "{" in mtd_val[1]:
                values = mtd_val[1].replace(")", "").split(", ", 1)
                id = values[0]
                dic = eval((values[1]))
                for k, v in dic.items():
                    name = " " + k
                    value = " " + str(v)
                    methods[method](args[0] + " " + id + name + value)

            else:
                values = mtd_val[1].replace(")", "").split(",")
                id = values[0]
                if len(values) > 1:
                    name = " " + values[1]
                    value = " " + values[2]
                    methods[method](args[0] + " " + id + name + value)
                else:
                    methods[method](args[0] + " " + id)

        except(IndexError, KeyError):
            print("*** Unknown syntax: {}".format(line))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
