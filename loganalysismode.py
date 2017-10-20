"""This file contains the routines and interface for doing analysis on logs

"""
import os


from libs.utils import prompts_user
from libs.logutils import LogLineGenerator
analyserObject = None

class loganalyser(object):
    "Class for doing loganalysis"

    def __init__(self):
        "initiates the loganalyser by getting the logs"
        print("initing the generator")
        self.lineGen = LogLineGenerator()
        # line = next(self.lineGen)
        print(next(self.lineGen))
        if self.lineGen:
            print("Hurray, you now have a valid loganalyser obj with logGen!")
            return
        else:
            print("Something went wrong in getting the logs generator obj")

    def parser(self, arg=False, otherArg=None):
        "Parses every line in the logs to terminal"
        print("parser func was called with args")
        print(arg)
        print(otherArg)
        for line in self.lineGen:
            print(line)
            if line == None:
                return

    def linReg(self):
        "Does a simple linear regression on the logs"
        pass

    def anomalies(self):
        "Checks the logs for values out of the ordinary"
        pass

    @prompts_user
    def selectAnalysis(self):
        self = self[0]
        while True:
            print(self)
            if self.lineGen:
                choicesList = [self.parser, self.linReg, self.anomalies]
                return choicesList
            else:
                self.lineGen = LogLineGenerator()


def analyzelogs():
    "Entry function for analyzing logs"
    analyserObject = loganalyser()
    analyserObject.selectAnalysis()
