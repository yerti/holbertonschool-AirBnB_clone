#!/usr/bin/python3
import cmd
import json

"""The starting point for the command interpreter"""
class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that implements a command line interface"""
    def emptyline(self):
        """This will give a blank line"""
        pass

    completekey = None
    prompt = '(hbnb)'

    def __init__(self):
        super().__init__()

    def do_help(self, line):
        """"Show help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit  create")
        print("\n")

    def do_quit(self, line):
        """Command to exit the program"""
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        """Command to handle the end of the file (Ctrl+D)"""
        return True

    def do_create(self, line):
        """Instance creator for test classes"""
        if not line:
            print("** class name missing **")
        else:
            from models.base_model import BaseModel
            try:
                cls = eval(line)
                instance = cls()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")
    
    def do_show(self, line):
        """Muestra información de una instancia"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                from models import storage
                obje_key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if obje_key in objects:
                    print(objects[obje_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            from models import storage
            class_name = args[0]
            objects = storage.all()
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) < 2 :
                print("** instance id missing **")
            else:
                instance_id = args[1]
                obj_key = "{}.{}".format(class_name, instance_id)
                if obj_key in objects:
                    del objects[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
    
    def do_all(self, line):
        """Prints all string representations of all instances"""
        from models import storage
        args = line.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = eval(args[0])
                if cls.__name__ not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    print([str(obj) for obj in objects.values() if isintance(obj, cls)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name and ID"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        from models import storage
        class_name = args[0]
        objects = storage.all()
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print ("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
                
        new_value = args[3]
        obj_instance = objects[obj_key]
        try:
            if hasattr(obj_instance, attribute_name):
                attr_type = type(getattr(obj_instance, attribute_name))
                if attr_type is int:
                    new_value = int(new_value)
                elif attr_type is float:
                    new_value = float(new_value)
                if attribute_name not in ["id", "created_at", "updated_at"]:
                    setattr(obj_instance, attribute_name, new_value)
                    storage.save()
                else:
                    print("** cannot update 'id', 'created_at', or 'updated_at' **")
            else:
                print("** attribute doesn't exist **") 
        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
