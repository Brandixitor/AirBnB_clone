#!/usr/bin/python3
"""This is the Console module."""
import cmd
import shlex
import models
import ast

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The Console class of our HBNB project."""
    prompt = "(hbnb) "

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **",
        "missingAttr": "** attribute name missing **",
        "missingValue": "** value missing **"
    }

    classes = [
        "BaseModel", "Amenity", "City", "Place", "Review", "State", "User"
    ]

    def do_quit(self, arg):
        """
        Exits the program.
            usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program.
            usage: EOF (Ctrl+D)
        """
        return True

    def emptyline(self):
        """Handles the emptyline behaviour."""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints the id.
            usage: create <class_name>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            new = eval(args[0])()
            new.save()
            print(new.id)
        else:
            print(self.errors["wrongClass"])

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
            usage: show <class_name> <id>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_destroy(self, arg):
        """
        Deletes an instance.
            usage: destroy <class_name> <id>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
            usage: all [class_name]
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print([v.__str__() for v in models.storage.all().values()])
        elif args[0] in self.classes:
            print([v.__str__() for v in models.storage.all().values()
                   if type(v) is eval(args[0])])
        else:
            print(self.errors["wrongClass"])

    def do_update(self, arg):
        """
        Updates an instance by adding or updating attribute.
            usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    if len(args) < 3:
                        print(self.errors["missingAttr"])
                    else:
                        if len(args) < 4:
                            print(self.errors["missingValue"])
                        else:
                            obj = models.storage.all()[key]
                            try:
                                attr_type = type(getattr(obj, args[2]))
                                args[3] = attr_type(args[3])
                            except:
                                try:
                                    args[3] = int(args[3])
                                except:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        pass

                            setattr(obj, args[2], args[3])
                            obj.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def count(self, arg):
        """
        Prints the number of instances of a class.
            usage: count <class_name>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            instances = str(models.storage.all().keys())
            print(instances.count(args[0]))
        else:
            print(self.errors["wrongClass"])

    def default(self, line):
        """Handles the default behaviour."""
        funcs = {"all": self.do_all, "count": self.count, "show": self.do_show,
                 "destroy": self.do_destroy, "update": self.do_update}
        cmd = line.split('.', 1)
        class_name = cmd[0]
        args = [None]
        if len(cmd) > 1:
            args = cmd[1].strip("()").split('(')
        if args[0] in funcs:
            func = funcs[args[0]]
            params = class_name + ' '
            if len(args) > 1:
                if args[0] == "update" and args[1][-1] == '}':
                    str_dict = args[1].split(' ', 1)[1]
                    upd_dict = ast.literal_eval(str_dict)
                    params += args[1].split(',', 1)[0] + ' '
                    for k, v in upd_dict.items():
                        fparams = '{} "{}" "{}"'.format(params, str(k), str(v))
                        func(fparams)
                    return
                else:
                    params += args[1].replace(',', '')
            func(params)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
