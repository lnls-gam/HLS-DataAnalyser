import pandas as pd
import numpy as np
import matplotlib as plt
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Initializing the inherited class
        super(Ui, self).__init__()
        # Load the .ui file
        uic.loadUi('gui.ui', self)
        # Show the screen
        self.show()

class Plot:
    pass

class Data:
    pass

class DataOperator:
    pass

class App(QtWidgets.QApplication):
    def __init__(self):
        # Initializing the application and its UI
        super(App,self).__init__(sys.argv)
        self.ui = Ui()
        # Calling the app to execute
        self.exec_()

        # Initializing the app's tools
        self.createEventListeners()
        self.startApp()

    def createEventListeners(self):
        pass

    def startApp(self):
        pass

if __name__ == "__main__":
    App()