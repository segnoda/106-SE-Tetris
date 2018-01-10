# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 600)
        MainWindow.setStyleSheet("""
                * {
                    background: #111111;
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background: #FF4136;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background: #FF7469;
                }
                QPushButton#exitButton:hover {
                    background: #ff6259;
                }
                QPushButton:disabled {
                    color: #7f8081;
                    background: #BB4136;
                }
                QFrame {
                    background: #0d1e36;
                    border: 2px solid #FF4136;
                }
                QLabel {
                    background: #111111;
                    border: none;
                }
                QLabel#scores {
                    font-size: 20px;
                }
                QLabel#lines {
                    font-size: 20px;
                }
                QStatusBar {
                    background: #FF4136;
                }
                """)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(10, 60, 93, 28))
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(False)
        self.startButton.setFlat(False)
        self.startButton.setFocusPolicy(Qt.ClickFocus)
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(10, 100, 93, 28))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setFocusPolicy(Qt.ClickFocus)
        self.exitButton = QtWidgets.QPushButton(self.centralWidget)
        self.exitButton.setGeometry(QtCore.QRect(10, 140, 93, 28))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setFocusPolicy(Qt.ClickFocus)
        self.score = QtWidgets.QLabel(self.centralWidget)
        self.score.setGeometry(QtCore.QRect(40, 420, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score.setObjectName("score")
        self.scores = QtWidgets.QLabel(self.centralWidget)
        self.scores.setGeometry(QtCore.QRect(60, 450, 58, 15))
        self.scores.setObjectName("scores")
        self.line = QtWidgets.QLabel(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(50, 480, 58, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line.setObjectName("line")
        self.lines = QtWidgets.QLabel(self.centralWidget)
        self.lines.setGeometry(QtCore.QRect(60, 510, 58, 15))
        self.lines.setObjectName("lines")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(119, 9, 251, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 380, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.score.setText(_translate("MainWindow", "SCORE"))
        self.scores.setText(_translate("MainWindow", "TextLabel"))
        self.line.setText(_translate("MainWindow", "LINE"))
        self.lines.setText(_translate("MainWindow", "TextLabel"))
