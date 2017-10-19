"This file contains utils for doing stuff with logs"
import os

def LogLineGenerator():
    "Checks the files in logs dir and generates lines from userselected file"
    try:
        # First give the user the possible choices
        logs = os.listdir('./logs/')
        print("Avaliable logs ::")
        for log in logs:
            print("File :: " + log)
            with open("./logs/" + log, 'r') as l:
                print("         Description  :: " + l.readline())
        print("Type the name of the file you wish to analyse")
        # Next prompt the user to select a log
        userLog = ""
        while True:
            userLog = input("  > ")
            if userLog in logs:
                print("You selected a valid log! ")
                break
            else:
                print("Couldnt find a log with that name - Try again")
    except KeyboardInterrupt:
        return False
    # Finally we make the generator
    while True:
        with open("./logs/" + userLog, 'r') as l:
            line = l.readline()
            print("Opening the log :: %s -- %s" % (userLog, line))
            for line in l:
                yield line
            else:
                print("---- Seems I reached the EOF ----")
                yield None
