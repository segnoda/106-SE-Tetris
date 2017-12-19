from PyQt5.QtWidgets import (QMainWindow, QFrame, QDesktopWidget, QApplication,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel,
                             QGridLayout)
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor , QFont
import sys, random
from tetrisView import *
from tetrisModel import *

class tetrisController(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):


        self.window=tetrisView(self)
       
        self.currentState=self.window.model.getState()
        self.window.startButton.clicked.connect(self.buttonClicked)
        self.window.pauseButton.clicked.connect(self.buttonClicked)
        self.window.exitButton.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        sender=self.sender()
        if sender.text()=="START":
            self.start()
        elif sender.text()=="PAUSE":
            self.pause()
        elif sender.text()=="EXIT":
            self.exit()
    def start(self):
        if self.currentState=="START":
            return
        self.currentState="START"
        self.window.start()
    def pause(self):
        if self.currentState!="START":
            return
        self.currentState="PAUSE"
        self.window.pause()
    def exit(self):
        self.window.exit()

    def getUserInput(self, sender):
        if sender.text()=="START":
            self.start()
        elif sender.teext()=="PAUSE":
            self.pause()








if __name__ == '__main__':
    
    app = QApplication([])
    tetris = tetrisController()
    
    sys.exit(app.exec_())
