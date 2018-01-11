from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tetrisModel import *
#from pyqtwindow import *
#from B10415009 import *
#from B10415013 import *
#from B10415015 import *
#from B10415051 import *
from B10431031 import *

import sys, random

class tetrisView(QMainWindow, Ui_MainWindow):
    over = False
    def __init__(self, parent):
        line = 0
        super(tetrisView, self).__init__(parent)
        self.setupUi(self)
        self.game = tetrisGame(self)
        self.game.setGeometry(self.frame.geometry())
        self.scores.setText('0')
        self.lines.setText('0')
        self.show()

    def keyPressEvent(self, event):
        if self.game.model.getState() != 'START':
            return
        if tetrisView.over == True:
            return
        key = event.key()

        print('key')
        if key == Qt.Key_Left:
            self.statusBar.showMessage('left')
            self.game.Move(self.game.currentPiece, self.game.curX - 1, self.game.curY)
        elif key == Qt.Key_Right:
            self.statusBar.showMessage('right')
            self.game.Move(self.game.currentPiece, self.game.curX + 1, self.game.curY)
        elif key == Qt.Key_Down:
            self.statusBar.showMessage('down')
            self.game.Move(self.game.currentPiece, self.game.curX, self.game.curY - 1)
        elif key == Qt.Key_Up:
            self.statusBar.showMessage('up')
            self.game.Move(self.game.currentPiece.rotateLeft(), self.game.curX, self.game.curY)
        elif key == Qt.Key_Space:
            self.game.dropDown()
        elif key == Qt.Key_Space:
            self.statusBar.showMessage('space')
            self.game.dropDown()
        elif key == Qt.Key_Escape:
            self.close()

class tetrisGame(QFrame):

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        self.line = 0
        self.score = 0
        self.timer = QBasicTimer()
        self.model = tetrisModel()
        self.currentPiece = tetrisModel()
        self.waiting = False
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []
        self.isStarted = False
        self.isPaused = False
        self.resize(380, 600)
        self.setWindowTitle('Tetris')
        self.clearBoard()
        self.clearBoard()
        self.gameover = False
        self.parent().startButton.setEnabled(True)
        self.parent().pauseButton.setEnabled(False)


    def clearBoard(self):
        if len(self.board)>220:
            print(len(self.board))
            for a in range(44):
               for b in range(10):
                   self.setShapeAt(b, a, PiecesShape.NoShape)

        else:
            for i in range(tetrisGame.BoardWidth * tetrisGame.BoardHeight):
                self.board.append(PiecesShape.NoShape)



    def start(self):
        self.parent().startButton.setEnabled(False)
        self.parent().pauseButton.setEnabled(True)
        self.parent().statusBar.showMessage('Game start!')
        if  self.gameover == True:
            self.clearBoard()
            self.gameover = False
            tetrisView.over = False
        if self.model.getState() !='PAUSE':
            self.line = 0
            self.score = 0
            self.newPiece()
            self.parent().scores.setText('0')
            self.parent().lines.setText('0')
        self.timer.start(tetrisGame.Speed, self)
        self.model.setState('START')

    def pause(self):

        self.model.setState('PAUSE')
        self.parent().pauseButton.setEnabled(False)
        self.parent().startButton.setEnabled(True)
        self.parent().statusBar.showMessage('Game pause!')
        self.timer.stop()
        self.update()

    def exit(self):
        self.parent().statusBar.showMessage('Bye!')
        self.parent().close()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.waiting:
                self.waiting = False
                self.newPiece()
            else:
                self.autoDown()
        else:
            super(tetrisGame, self).timerEvent(event)

    def newPiece(self):
        self.currentPiece.setRandomShape()
        self.curX = tetrisGame.BoardWidth // 2 + 1
        self.curY = tetrisGame.BoardHeight - 1 + self.currentPiece.minY()
        if not self.Move(self.currentPiece, self.curX, self.curY):
            self.currentPiece.setShape(PiecesShape.NoShape)
            self.timer.stop()

    def dropDown(self):

        newY = self.curY
        while newY > 0:
            if not self.Move(self.currentPiece, self.curX, newY - 1):
                break
            newY -= 1
        self.pieceDropped()

    def autoDown(self):

        if not self.Move(self.currentPiece, self.curX,self.curY - 1):
            self.pieceDropped()

    def shapeAt(self, x, y):

        return self.board[(y * tetrisGame.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):

        self.board[(y * tetrisGame.BoardWidth) + x] = shape

    def pieceDropped(self):

        for i in range(4):
            x = self.curX + self.currentPiece.x(i)
            y = self.curY - self.currentPiece.y(i)
            self.setShapeAt(x, y, self.currentPiece.getShape())

        self.removeFullLines()

        if not self.waiting:
            self.newPiece()

    def removeFullLines(self):
        numFullLines = 0
        rowsToRemove = []

        count = 0
        for i in range(tetrisGame.BoardHeight):
            n = 0
            for j in range(tetrisGame.BoardWidth):
                if not self.shapeAt(j, i) == PiecesShape.NoShape:
                    n = n + 1
            if n == 10:
                rowsToRemove.append(i)
                self.line += 1
                self.parent().lines.setText(str(self.line))
                count = count + 1
        if(count == 4):
            self.score = self.score + 8
            self.parent().scores.setText(str(self.score))
        else:
            self.score = self.score + count
            self.parent().scores.setText(str(self.score))


        rowsToRemove.reverse()

        for m in rowsToRemove:
            for k in range(m, tetrisGame.BoardHeight):
                for l in range(tetrisGame.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.isWaitingAfterLine = True
            self.currentPiece.setShape(PiecesShape.NoShape)
            self.update()

    def Move(self, newPiece, newX, newY):

        for i in range(4):
            x = newX + newPiece.x(i)

            y = newY - newPiece.y(i)
            if x < 0 or x >= tetrisGame.BoardWidth or y < 0 or y >= tetrisGame.BoardHeight + 4:
                return False
            if self.shapeAt(x, y) != PiecesShape.NoShape:
                return False
        self.currentPiece = newPiece
        self.curX = newX
        self.curY = newY

        self.update()
        return True

    def checkfullboard(self):
        check = 0
        for i in range(tetrisGame.BoardWidth):
            check += self.shapeAt(i, 20)
        if  check!=0:
            self.gameover = True
            tetrisView.over = True
            self.parent().startButton.setEnabled(True)
            self.parent().pauseButton.setEnabled(False)
            self.model.setState('GAMEOVER')
            self.parent().statusBar.clearMessage()
            self.parent().statusBar.showMessage('Game Over')



    def squareWidth(self):

        return self.contentsRect().width() // tetrisGame.BoardWidth

    def squareHeight(self):

        return self.contentsRect().height() // tetrisGame.BoardHeight

    def paintEvent(self, event):
        self.checkfullboard()
        painter = QPainter(self)
        
        rect = self.contentsRect()
        boardTop = rect.bottom() - tetrisGame.BoardHeight * self.squareHeight()
        for i in range(tetrisGame.BoardHeight):
            for j in range(tetrisGame.BoardWidth):

                shape = self.shapeAt(j, tetrisGame.BoardHeight - i - 1)

                if shape != PiecesShape.NoShape:
                    self.drawSquare(painter, rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)
        if (self.currentPiece.getShape() != PiecesShape.NoShape):

            for i in range(4):
                x = self.curX + self.currentPiece.x(i)
                y = self.curY - self.currentPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (tetrisGame.BoardHeight - y - 1) * self.squareHeight(),
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
                         x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)
