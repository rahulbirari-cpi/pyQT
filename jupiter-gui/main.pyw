from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

import sys


class main_window(QMainWindow):

    def __init__(self):
        super(main_window, self).__init__()
        self.setGeometry(200, 200, 700, 300)
        self.setWindowTitle("Jupiter")
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Main Window")
        self.label.move(50, 50)

        # Create a self.button in the window
        self.button = QPushButton(self)
        self.button.setText("Click Me")
        self.button.move(200, 200)

        # Connect event to function 
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def run_gui():

    # Create the application
    app = QApplication(sys.argv)

    MainWindow = main_window()

    MainWindow.show()

    sys.exit(app.exec_())    



# Run the main function
run_gui()