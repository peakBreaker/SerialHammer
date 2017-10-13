from functools import wraps

def print_help(options):
    print("::: These are your options :::\n")
    print("help -> prints this helpful dialog")
    for option in options.keys():
        print(option + "\n        ->  " + options[option].__doc__)

    print("\n #### Good luck out there! ####")
    return


def prompts_user(function):
    "a decorator for giving user a prompt"
    @wraps(function)
    def wrapper(*args):
        try:
            options = {option.__name__: option for option in function(args)}
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
                        print(options[_resp[0]].__doc__)
                    # Otherwise we print and call the function
                    else:
                        options[_resp[0]](_resp)  # Call the function
                else:
                    print("""
                            Im sorry dave, I cant do that.
                            Try writing 'help'
                            """)

        except KeyboardInterrupt:
            return
    return wrapper
