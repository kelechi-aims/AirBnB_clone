#!/usr/bin/python3

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        return True

    def d0_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
