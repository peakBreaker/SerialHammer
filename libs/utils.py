
def print_help(options):
    print("::: These are your options :::\n")
    print("help -> prints this helpful dialog")
    for key in options.keys():
        print(key + " -> " + options[key][2])

    print("\n #### Good luck out there! ####")
    return


def prompts_user(function):
    "a decorator for giving user a prompt"
    def wrapper(*args):
        try:
            options = function(args)
            while True:
                print(" ")
                _rawResp = input("%s > " % function.__name__)
                _resp = _rawResp.split(" ")
                # Check if user gave valid input
                if _resp[0] == "help":
                    print_help(options)
                elif _resp[0] in options.keys():
                    # First check if user wanted help
                    if "--help" in _resp or "-h" in _resp:
                        print(options[_resp[0]][2])
                    # Otherwise we print and call the function
                    else:
                        print("user called functionality! ")
                        print(options[_resp[0]][0]) # First print the msg
                        options[_resp[0]][1](_resp) # Call the function
                else:
                    print("""
                            Im sorry dave, I cant do that.
                            Try writing 'help'
                            """)

        except KeyboardInterrupt:
            return
    return wrapper
