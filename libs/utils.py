from functools import wraps
import inspect

hal9000 = """
@@@@@@@@@@@@@@@@@@@@@,#####++###################;@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,####++++#+.`..``##########;@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,###++'+:.:'#@@+;:.;#+#####;@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,##++++`;#@@@@@@@@#,.######;@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,###+`+###+``````+@@@;:####'@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,##';@@##@#########+@#@;###+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@:##.#@#,++#++;+++###,@@####+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@;#@,@@,+##++,`,'''+#+#@@'##+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@'#;'@@'#+++,:`;''++###@@:##+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+##:@@@##++''''''++##@@@.+#+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+##:@@@##++''''''++##@@@.##+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+##;@@;###+++'++++####@@+#@+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+##+:@#:###++++++#####@.+##+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+##@+:@@.```####@@@@#@.+###+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+#@@#@+;@###@@@@@@@@.+@###@+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+#@#####';@@@@@@@@.++@####@+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+#@@@@@@@++;,,..:++@@#@@@#@+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@+@@@@@@@@@#@#++#@@@@@#@@@@@+@@@@@@@@@@@@@@@@@@@@@@

        I'm sorry Dave, I'm afraid I can't do that.
                            -> Try writing help
"""

def inspect_function(func):
    "Gets the arguments from the function"
    # First get argument specifiers
    # print("finding args for function %s" % func.__name__)
    signatures = inspect.signature(func)
    # print(signatures)
    # Getting the signature parameter objects
    _p = {signatures.parameters[p].name: signatures.parameters[p].default
          if signatures.parameters[p].default is not inspect._empty else "N/A"
          for p in signatures.parameters}
    args = []
    for param, val in _p.items():
        userVal = input("Provide optional arg for %s [%s] > " % (param, val))
        args.append(userVal if userVal is not "" else val)
    # print(args)
    return args

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
            # Firsy get the possible options
            options = {option.__name__: option for option in function(*args)}
            while True:
                # Prompt the user response
                print(" ")
                _rawResp = input("%s > " % function.__name__)
                _resp = _rawResp.split(" ")
                # Check if user gave valid input
                if _resp[0] == "help":
                    print_help(options)
                elif _resp[0] in options.keys():
                    called_function = options[_resp[0]]
                    # First check if user wanted help
                    if "--help" in _resp or "-h" in _resp:
                        print(function.__doc__)
                    # Otherwise we print and call the function
                    else:
                        args = inspect_function(called_function)
                        # print("Got args!")
                        # if 'self' in args:
                        #     print("Removing self before calling function")
                        #     args.remove('self')
                        # Give user possibility to supply argument
                        if args or args == []:
                            # print("Calling function with args : ")
                            # print(*args)
                            called_function(*args)  # Call the function
                        else:
                            print("#### UNSUPPORTED FUNCTION ####")
                else:
                    print(hal9000)

        except KeyboardInterrupt:
            return
    return wrapper
