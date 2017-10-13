#!usr/bin/python

import serial
from libs.utils import prompts_user

welcome = """
  ____            _       _ _   _
 / ___|  ___ _ __(_) __ _| | | | | __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \ / _ \ '__| |/ _` | | |_| |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  ___) |  __/ |  | | (_| | |  _  | (_| | | | | | | | | | | |  __/ |
 |____/ \___|_|  |_|\__,_|_|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|
  ___________________________________________________________________
 |                                                                   |
 |               SerialHammer By peakBreaker v0.2                    |
 |___________________________________________________________________|
"""

# options = """
# ::: These are your options :::
#     help -> Prints out this help dialog
#     Go North -> Goes north
# """


def do_something(*args):
    "Does useful stuff"
    print("I am doing something!")
    return


help = "This is a commandline application for doing fun stuff"
do_something_welcome = "does something.."
# Follows this pattern ==>
# "command" : [printout, optional_function, info_on_command]


@prompts_user
def new_state(*args):
    "Puts prompt into new state"
    print("I am now in a new state, ready to do some crazey stuff")
    new_state_dict = [do_something, main]
    return new_state_dict


@prompts_user
def main(*args):
    """main function docstring!"""
    options = [new_state, do_something]
    return options


if __name__ == '__main__':
    print(welcome)
    main("hey")
