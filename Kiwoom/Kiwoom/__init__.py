import sys
from Main import *
from PyQt5.QtWidgets import *

class Main():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.kxing = KXing()
        self.app.exec_()

if __name__ == "__main__":
    Main()