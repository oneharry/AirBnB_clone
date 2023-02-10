#!/usr/bin/python3
""" Entry point to the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
storage = FileStorage()

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

    def do_destroy(self, line):
        """ Deletes an instance based on the <class name> and <id> """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] and args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif args[0] and len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            obj = storage.all()
            del obj[args[0] + "." + args[1]]
            storage.save()
                
            
    def do_all(self, line):
        """
        Prints all string repr of all instance based
        or not on the class name
        """
        args = line.split(" ")
        if args[0] and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj_arr = []
            obj = storage.all()
            if not args[0]:
                obj_arr = [str(obj_v) for obj_v in obj.values()]
            else:
                for obj_v in obj.values():
                    if obj_v.__class__.__name__ == args[0]:
                        (obj_arr.append(str(obj_v)))
            print(obj_arr)

       
    def do_update(self):
        """
        Updates an instance based on the <class name> and <id> by:
           adding or updating attribute( save the change into JSON file)
        """
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
