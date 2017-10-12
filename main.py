#!usr/bin/python

import serial
from libs.utils import prompts_user

welcome = """
  ____            _       _ _   _
 / ___|  ___ _ __(_) __ _| | | | | __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \ / _ \ '__| |/ _` | | |_| |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  ___) |  __/ |  | | (_| | |  _  | (_| | | | | | | | | | | |  __/ |
 |____/ \___|_|  |_|\__,_|_|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|
                SerialHammer By Anders L. Hurum v0.1
  ___________________________________________________________________
"""

# options = """
# ::: These are your options :::
#     help -> Prints out this help dialog
#     Go North -> Goes north
# """

def do_something(*args):
    print("I am doing something!")
    return

help = "This is a commandline application for doing fun stuff"
do_something_welcome = "does something.."
# Follows this pattern ==>
# "command" : [printout, optional_function, info_on_command]
@prompts_user
def new_state(*args):
    print("I am now in a new state, ready to do some crazey stuff")
    new_state_dict = {"do_something_again": ["Doing something again :o", do_something, "prints out useful stuff"]}
    return new_state_dict

answerDict = {
    "do_something" : [do_something_welcome, do_something, "does soemthing funney"],
    "new_state" : ["Welcome to new state!", new_state, "puts prompt into new state"]}

@prompts_user
def main(*args):
    options = answerDict
    return options


if __name__ == '__main__':
    main("hey")
