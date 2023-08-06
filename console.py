#!/usr/bin/python3
"""Entry point for the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class HBNBCommand(cmd.Cmd):
    """Interpreter class from cmd"""
    prompt = '(hbnb) '
    classes_list = ["BaseModel"]
    int_attrs = ["attribute1", "attribute2"]
    float_attrs = ["attribute3", "attribute4"]
    def do_EOF(self, line):
        """Quits the console when Ctrl D entered"""
        print()
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def emptyline(self):
        """Overrides parent empty line method"""
        pass
    def do_help(self, line):
        """Display help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit  create  show  destroy  all  update")
        print("\n")

    def do_create(self, line):
        """Creates a new instance of a specified class and prints
        nstance's unique id"""
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
        """Prints the string repr of an instance based
        on class name and id"""
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
        """Deletes an instance of a class based on class name and id"""
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
        """Prints, as a list of strings, or all instances of a certain
        class, if provided"""
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
        """Updates or adds an attribute to an instance of a class
        instance is identified by class name and id
        only one attribute and value can be updated per call"""
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
