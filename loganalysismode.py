"""This file contains the routines and interface for doing analysis on logs

"""
import os


from libs.utils import prompts_user
from libs.logutils import LogLineGenerator


class loganalyser():
    "Class for doing loganalysis"

    def __init__(self):
        "initiates the loganalyser by getting the logs"
        self.lineGen = LogLineGenerator()
        if self.lineGen:
            print("Hurray, you now have a valid loganalyser obj with logGen!")
        else:
            print("Something went wrong in getting the logs generator obj")

    def parser():
        pass

    def linReg():
        pass

    def anomalies():
        pass

    @prompts_user
    def selectAnalysis():
        choicesList = [parser]

if __name__ == '__main__':
    gen = LogLineGenerator()
    print("")
    for line in gen:
        print(line)
        if line == None:
            break
    print("finished with testing the generator")
