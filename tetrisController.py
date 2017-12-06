from PyQt5.QtWidgets import (QMainWindow, QFrame, QDesktopWidget, QApplication,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel,
                             QGridLayout)
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor , QFont
import sys, random
from tetrisView import tetrisView
from tetrisModel import tetrisModel 

class tetrisController(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.window=tetrisView(self)
 
        











if __name__ == '__main__':
    
    app = QApplication([])
    tetris = tetrisController()
    
    sys.exit(app.exec_())
