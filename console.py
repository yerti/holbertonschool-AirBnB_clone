#!/usr/bin/python3
"""
The starting point for the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb)'
    
    def emptyline(self):
        """This will give a blank line"""
        pass
    def __init__(self):
        super().__init__()

    def do_help(self, line):
        """Show help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit  create  show  destroy  all  update")
        print("\n")

    def do_quit(self, line):
        """Command to exit the program"""
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        """Command to handle the end of the file (Ctrl+D)"""
        return True



    def do_create(self, arg):
        """Instance creator for test classes"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)


    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        if not arg:
            print([str(v) for v in storage.all().values()])
        elif args[0] in ['BaseModel']:
            print([str(v) for v in storage.all().values()if isinstance(v, eval(args[0]))])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_show(self, arg):
        """Shows information about an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and ID"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(objs[key], args[2], args[3])
                storage.save()
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
