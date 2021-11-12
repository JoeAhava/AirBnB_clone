#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBnb Clone Console\n'
    prompt = '(hbnb) '
    ''' Entry point of console program and commands center '''

    def emptyline(arg):
        pass

    def do_EOF(self, arg): 
        '''Quit command to exit the program
        '''
        print("")
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
