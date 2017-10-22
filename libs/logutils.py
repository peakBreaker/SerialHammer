"This file contains utils for doing stuff with logs"
import os

def LogLineGenerator():
    "Checks the files in logs dir and generates lines from userselected file"
    try:
        # First give the user the possible choices
        def _listlogs():
            _logs = os.listdir('./logs/')
            print("Avaliable logs ::")
            for log in _logs:
                print("File :: " + log)
                with open("./logs/" + log, 'r') as l:
                    print("         Description  :: " + l.readline())
            print("Type the name of the file you wish to analyse")
            return _logs
        logs = _listlogs()
        # Next prompt the user to select a log
        userLog = ""
        while True:
            userLog = input("  > ")
            if userLog in logs:
                print("You selected a valid log! ")
                break
            elif userLog == "ls":
                _listlogs()
            elif userLog == "exit":
                return False
            else:
                print("Couldnt find a log with that name - Try again")
                print(":: Avaliable commands ::\n       'ls' -> list logs "
                      "\n       'exit' -> exit state")
    except KeyboardInterrupt:
        return False
    # Finally we make the generator
    while True:
        with open("./logs/" + userLog, 'r') as l:
            # line = l.readline()
            print("Opening the log :: %s" % userLog)
            for line in l:
                yield line
            else:
                print("---- Seems I reached the EOF ----")
                yield None
