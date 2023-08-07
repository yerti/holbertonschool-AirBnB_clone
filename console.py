#!/usr/bin/python3
"""The starting point for the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that implements a command line interface"""
    prompt = '(hbnb) '
    classes_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]
    int_attrs = ["attribute1", "attribute2"]
    float_attrs = ["attribute3", "attribute4"]

    def do_EOF(self, line):
        """Quits the console when (Ctrl+D) entered"""
        print()
        return True

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """This will give a blank line"""
        pass

    def do_help(self, line):
        """Show help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit  create  show  destroy  all  update")
        print("\n")

    def do_create(self, line):
        """Instance creator for test classes"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Shows information about an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        for key, value in all_objs.items():
            if key == obj_key:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        for key, value in all_objs.items():
            if key == obj_key:
                del all_objs[key]
                storage.__objects = all_objs
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all instances"""
        objs_list = []
        storage = FileStorage()
        all_objs = storage.all()
        check = False
        if not line:
            for key, value in all_objs.items():
                objs_list.append(str(value))
            print(objs_list)
            return
        else:
            args = line.split()
            for key, value in all_objs.items():
                test_obj_type = key.split(".")
                if test_obj_type[0] == args[0]:
                    objs_list.append(str(value))
                    check = True
                if check:
                    print(objs_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name and ID"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False
        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value
        if not instance_found:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[2] in HBNBCommand.int_attrs:
            setattr(instance_found, args[2], int(args[3]))
        elif args[2] in HBNBCommand.float_attrs:
            setattr(instance_found, args[2], float(args[3]))
        else:
            setattr(instance_found, args[2], args[3])
        instance_found.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
