#!usr/bin/python

import serial

welcome = """
  ____            _       _ _   _
 / ___|  ___ _ __(_) __ _| | | | | __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \ / _ \ '__| |/ _` | | |_| |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  ___) |  __/ |  | | (_| | |  _  | (_| | | | | | | | | | | |  __/ |
 |____/ \___|_|  |_|\__,_|_|_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|
                SerialHammer By Anders L. Hurum v0.1
  ___________________________________________________________________
"""

options = """
::: These are your options :::
    help -> Prints out this help dialog
    Go North -> Goes north

"""


def promptUser():
    while True:
        print("Choose your command")
        _resp = input("> ")
        if _resp == 'help':
            print(options)
        elif _resp == 'valid':
            return _resp
        else:
            print("invalid command")


def main():
    print(welcome)
    call = promptUser()


if __name__ == '__main__':
    main()
