#!/usr/bin/python3
import cmd


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
        """Show help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit")
        print("\n")

    def do_quit(self, line):
        """Command to exit the program"""
        print("Quit command to exit the program")
        return True

    def do_EOF(self, line):
        """Command to handle the end of the file (Ctrl+D)"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
