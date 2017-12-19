from PyQt5.QtWidgets import (QMainWindow, QFrame, QDesktopWidget, QApplication,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel,
                             QGridLayout)
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QFont
from tetrisModel import *
import sys, random
from pyqtwindow import Ui_MainWindow



class tetrisView(QMainWindow, Ui_MainWindow):
    BoardWidth=10
    BoardHeight=22
    Speed=300

    def __init__(self, parent):
        super(tetrisView, self).__init__(parent)
        self.setupUi(self)
        self.initBoard()
        
    def initBoard(self):
        self.timer=QBasicTimer()
        self.model=tetrisModel()
        self.currentPiece=tetrisModel()
        self.waiting=False
        self.curX=0
        self.curY=0
        self.board=[]
        self.isStarted=False
        self.isPaused=False


        self.resize(380, 600)
        self.setWindowTitle('Tetris')
        self.clearBoard()
        self.show()
        
    def clearBoard(self):
        for i in range(tetrisView.BoardWidth * tetredisView.BoardHeight):
            self.board.append(PiecesShape.NoShape);
    def start(self):
        self.model.setState("START")
        self.startButton.setEnabled(False)
        self.pauseButton.setEnabled(True)
        self.scores.setText("0")
        self.lines.setText("0")
        self.statusBar.showMessage("Game start!")  
        self.clearBoard()
        self.newPiece()
        self.timer.start(tetrisView.Speed, self)
    def pause(self):
        self.model.setState("PAUSE")
        self.pauseButton.setEnabled(False)
        self.startButton.setEnabled(True)
        self.statusBar.showMessage("Game pause!")
        self.timer.stop()
        self.frame.update()
    def exit(self):
        self.statusBar.showMessage("Bye!")
        self.close()

    def keyPressEvent(self, event):
        if self.model.getState()!="START":
            return
        key=event.key()

        if key == Qt.Key_Left:
            self.statusBar.showMessage("left")
            self.Move(self.currentPiece, self.curX-1, self.curY)
        elif key == Qt.Key_Right:
            self.statusBar.showMessage("right")
            self.Move(self.currentPiece, self.curX+1, self.curY)
        elif key == Qt.Key_Down:
            self.statusBar.showMessage("down")
            self.Move(self.currentPiece, self.curX, self.curY-1)
        elif key == Qt.Key_Up:
            self.statusBar.showMessage("up")
        elif key == Qt.Key_Space:
            self.statusBar.showMessage("space")
            self.dropDown()
        elif key==Qt.Key_Escape:
            self.close()


    def timerEvent(self, event):
        if event.timerId()==self.timer.timerId():
            if self.waiting:
                self.waiting=False
                self.newPiece()
            else:
                self.autoDown()
        else:
            super(tetrisView, self).timerEvent(event)
    def newPiece(self):
        self.currentPiece.setRandomShape()
        self.curX=tetrisView.BoardWidth//2+1
        self.curY=tetrisView.BoardHeight-1+self.currentPiece.minY()
        if not self.Move(self.currentPiece, self.curX, self.curY):
            self.currentPiece.setShape(PiecesShape.NoShape)
            self.timer.stop()
    def dropDown(self):
        newY=self.curY
        while newY>0:
            if not self.Move(self.currentPiece, self.curX, newY-1):
                break
            newY-=1
        self.pieceDropped()
    def autoDown(self):
        if not self.Move(self.currentPiece, self.curX,self.curY-1):
            self.pieceDropped()
    def shapeAt(self, x, y):
        return self.board[(y*tetrisView.BoardWidth)+x]
    def setShapeAt(self , x, y, shape):
        self.board[(y * tetrisView.BoardWidth) + x]=shape
    def pieceDropped(self):
        for i in range(4):
            x=self.curX+self.currentPiece.x(i)
            y=self.curY-self.currentPiece.y(i)
            self.setShapeAt(x, y, self.currentPiece.getShape())
        if not self.waiting:
            self.newPiece()
    def Move(self, newPiece, newX, newY):
        for i in range(4):
            x=newX+newPiece.x(i)
            y=newY-newPiece.y(i)
            if x<0 or x>= tetrisView.BoardWidth or y<0 or y>= tetrisView.BoardHeight:
                return False
            if self.shapeAt(x, y) !=PiecesShape.NoShape:
                return False
        self.currentPiece=newPiece
        self.curX=newX
        self.curY=newY
        self.update()
        return True
    def squareWidth(self):
        return self.contentsRect().width()//tetrisView.BoardWidth
    def squareHeight(self):
        return self.contentsRect().height()//tetrisView.BoardHeight
    def paintEvent(self, event):
        
        painter = QPainter(self)
        print(painter.device())
        rect = self.contentsRect()
        
        boardTop = rect.bottom() - tetrisView.BoardHeight * self.squareHeight()
        
        for i in range(tetrisView.BoardHeight):
            for j in range(tetrisView.BoardWidth):
                
                shape = self.shapeAt(j, tetrisView.BoardHeight - i - 1)
                
                if shape != PiecesShape.NoShape:
                    self.drawSquare(painter,rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)
        if self.currentPiece.getShape() != PiecesShape.NoShape:
              
            for i in range(4):
                x = self.curX + self.currentPiece.x(i)
                y = self.curY - self.currentPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (tetrisView.BoardHeight - y - 1) * self.squareHeight(),
                    self.currentPiece.getShape())
                
    def drawSquare(self, painter, x, y, shape):        

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


