from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


# from .UI.ui_FirstStacking import Ui_MainWindow
from UI_Demo import Ui_RedTsone

# class UI(QMainWindow):
#     def __init__(self):
#         super(UI,self).__init__()
#         uic.loadUi('./UI/FirstStacking.ui',self)
#         self.show()
class Window(Ui_RedTsone,QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
print('asdasdasdsad')
win = Window()
win.show()
app.exec()
