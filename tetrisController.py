from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tetrisView import *
from tetrisModel import *

import sys, random

class tetrisController(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.window=tetrisView(self)
        self.window.startButton.clicked.connect(self.buttonClicked)
        self.window.pauseButton.clicked.connect(self.buttonClicked)
        self.window.exitButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):

        sender=self.sender()
        if sender.text()=='START':
            self.start()
        elif sender.text()=='PAUSE':
            self.pause()
        elif sender.text()=='EXIT':
            self.exit()

    def start(self):
        self.currentState = self.window.game.model.getState()
        if self.currentState=='START':
            return
        self.currentState='START'
        self.window.game.start()

    def pause(self):
        self.currentState = self.window.game.model.getState()
        if self.currentState!='START':
            return
        self.currentState='PAUSE'
        self.window.game.pause()

    def exit(self):
        self.window.game.exit()

    def getUserInput(self, sender):
        print('fuck')
        if sender.text()=='START':
            self.start()
        elif sender.text()=='PAUSE':
            self.pause()

if __name__ == '__main__':
    
    app = QApplication([])
    tetris = tetrisController()
    sys.exit(app.exec_())
