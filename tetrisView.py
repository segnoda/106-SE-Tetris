from PyQt5.QtWidgets import (QMainWindow, QFrame, QDesktopWidget, QApplication,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel,
                             QGridLayout)
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QFont
import sys, random
from pyqtwindow import Ui_MainWindow



class tetrisView(QMainWindow, Ui_MainWindow):
    msg2Statusbar = pyqtSignal(str)
    BoardWidth=10
    BoardHeight=22
    Speed=300

    def __init__(self, parent):
        super(tetrisView, self).__init__(parent)
        self.setupUi(self)
        self.initBoard()
        
    def initBoard(self):
        self.timer=QBasicTimer()
        self.curX=0
        self.curY=0
        self.board=[]
        self.isStarted=False
        self.isPaused=False
      
       
        self.startButton.clicked.connect(self.buttonClicked)
        self.pauseButton.clicked.connect(self.buttonClicked)
        self.exitButton.clicked.connect(self.buttonClicked)
        self.resize(380, 600)
        self.setWindowTitle('Tetris')
        self.show()
        
    def clearBoard(self):
        for i in range(tetrisView.BoardWidth * tetredisView.BoardHeight):
            self.board.append(0);
    def start(self):
        if self.isPaused:
            return
        self.isStarted=True
        self.msg2Statusbar.emit(str(0))
        self.timer.start(tetrisView.Speed, self)

    def buttonClicked(self):
        sender=self.sender()
        if sender.text()=="START":  
            self.startButton.setEnabled(False)
            self.pauseButton.setEnabled(True)
            self.scores.setText("0")
            self.lines.setText("0")
            self.statusBar.showMessage("Game start!")
        elif sender.text()=="PAUSE":
            self.pauseButton.setEnabled(False)
            self.startButton.setEnabled(True)
            self.statusBar.showMessage("Game pause!")
        elif sender.text()=="EXIT":
            self.close()
        
    def keyPressEvent(self, event):

        key=event.key()

        if key == Qt.Key_Left:
            self.statusBar.showMessage("left")
        elif key == Qt.Key_Right:
            self.statusBar.showMessage("right")
        elif key == Qt.Key_Down:
            self.statusBar.showMessage("down")
        elif key == Qt.Key_Up:
            self.statusBar.showMessage("up")
        elif key == Qt.Key_Space:
            self.statusBar.showMessage("space")
        elif key==Qt.Key_Escape:
            self.close()


    def timerEvent(self, event):
        if event.timerId()==self.timer.timerId():
            Speed=300
        else:
            super(tetrisView, self).timerEvent(event)
    


