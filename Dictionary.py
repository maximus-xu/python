import os
import re
import shutil
import configparser
from contextlib import contextmanager

from cmd import Cmd
import click

bucket = []
for i in range(1000):
    bucket += [[]]

class Console(Cmd):
    prompt = "/> "
    intro = "Welcome to dictionary! Type ? to list commands"

    def __init__(self):
        Cmd.__init__(self)
        self.default_color = "blue"

    def do_exit(self, arg):
        print("Byeeeeeeeeeeeeeeee")
        return True

    def do_save(self, arg):
        arg = arg.split(' ')
        bucket[abs(hash(arg[0]))%1000] += [(arg[0], arg[1])]

    def do_get(self, arg):
        for item in bucket[abs(hash(arg))%1000]:
            if arg == item[0]:
                print(item[1])
                return
        print("item not found")

    def do_test(self, arg):
        print("test")

    def do_help(self, arg):
        def g(text, align=10):
            return click.style(text.rjust(align), "green")

        help = f"""
{g("exit")} quit
{g("save <value>")} save the key:value
{g("get <key>:")} get a key 
"""
        print(help)


if __name__ == "__main__":
    Console().cmdloop()

