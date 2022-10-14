#!/usr/bin/python3
"""import module"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command line"""
    prompt = "(hbnb)"

    list_class = ["BaseModel", "User", "City",
                  "Amenity", "Place", "State", "Review"]

    def do_quit(self, args):
        """quit"""
        return True

    def do_EOF(self, args):
        """end"""

        return True

    def help_quit(self):
        """help"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """empty"""
        pass

    def do_create(self, args):
        """create class BaseModel"""
        args_input = args.split()
        if len(args_input) == 0:
            print("** class name missing **")
            return
        try:
            string_represent = eval(args_input[0] + '()')
            string_represent.save()
            print(string_represent.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """print the string representation"""
        args_input = args.split()
        if check_exited(args_input):
            object_ref = check_exited(args_input)
            all_inst = models.storage.all()
            if object_ref in all_inst.keys():
                ref = all_inst[object_ref]
                print(ref)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance"""
        args_input = args.split()
        if check_exited(args_input):
            object_ref = check_exited(args_input)
            all_inst = models.storage.all()
            if object_ref in all_inst.keys():
                del all_inst[object_ref]
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """all"""
        instances = models.storage.all()
        if args:
            args_input = args.split()
            print(args_input[0])
            if args_input[0] not in self.list_class:
                print("** class doesn't exist **")
            else:
                new_list = [str(instances[obj]) for obj in instances.keys()
                            if args_input[0] in obj]
                print(new_list)
        else:
            new_list = [str(instances[obj]) for obj in instances.keys()]
            print(new_list)

    def do_update(self, args):
        """update"""
        args_input = args.split()
        if check_exited(args_input):
            object_ref = check_exited(args_input)
            all_inst = models.storage.all()
            if object_ref in all_inst.keys():
                obj = all_inst[object_ref]
                len_arg = len(args_input)
                if len_arg < 3:
                    print("** attribute name missing **")
                    return
                elif len_arg < 4:
                    print("** value missing **")
                    return
                else:
                    try:
                        value = int(args_input[3].replace('"', ""))
                    except:
                        try:
                            value = float(args_input[3].replace('"', ""))
                        except:
                            try:
                                value = str(args_input[3].replace('"', ""))
                            except:
                                pass
                obj.__dict__[args_input[2]] = value
                models.storage.save()
                return
            else:
                print("** no instance found **")
                return


def check_exited(list_args):
    """check Function to valide content"""
    if list:
        len_list = len(list_args)
    if 1 > len_list:
        print("** class name missing **")
        return None
    if list_args[0] not in HBNBCommand.list_class:
        print("** class doesn't exist **")
        return None
    if len_list < 2:
        print("** instance id missing **")
        return None
    obj_reference = list_args[0] + '.' + list_args[1]
    return obj_reference


if __name__ == '__main__':
    HBNBCommand().cmdloop()

