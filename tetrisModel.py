from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys, random
#from tetrisView import tetrisView

class PiecesShape(object):
     NoShape = 0
     ZShape = 1
     SShape = 2
     LineShape = 3
     TShape = 4
     SQShape = 5
     LShape = 6
     MirroredLShape = 7
class tetrisModel(object):

     IDLE_STATE="IDLE"
     PiecesCoordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
     )
     def __init__(self):
          self.pieces=[[0,0] for i in range(4)]
          self.pieceShape=PiecesShape.NoShape
          self.setShape(PiecesShape.NoShape)
          self.state="IDLE"


     def setState(self, astate):
          self.state=astate

     def getState(self):
          return self.state
     def setShape(self, shape):
          table=tetrisModel.PiecesCoordsTable[shape]
          for i in range(4):
               for j in range(2):
                    self.pieces[i][j]=table[i][j]
          self.pieceShape=shape
     def getShape(self):
          return self.pieceShape
     def setRandomShape(self):
          self.setShape(random.randint(1, 7))
     def x(self, index):
          return self.pieces[index][0]
     def y(self, index):
          return self.pieces[index][1]
     def minY(self):
          miny=self.pieces[0][1]
          for i in range(4):
               miny=max(miny,self.pieces[i][0])

          return miny






    
