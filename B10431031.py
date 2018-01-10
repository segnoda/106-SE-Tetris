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
        MainWindow.resize(400, 580)
        MainWindow.setStyleSheet("""
                * {
                    background: #072053;
                    color: #ffffff;
                    font-size: 14px;
                }
                QPushButton {
                    background: #13398b;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background: #1d68d9;
                }
                QPushButton#exitButton:hover {
                    background: #ff6259;
                }
                QPushButton:disabled {
                    color: #7f8081;
                    background: #042569;
                }
                QFrame {
                    background: #0d1e36;
                    border: 2px solid #13398b;
                }
                QLabel {
                    background: #072053;
                    border: none;
                }
                QLabel#scores {
                    font-size: 30px;
                }
                QLabel#lines {
                    font-size: 30px;
                }
                QStatusBar {
                    background: #13398b;
                }
                """)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(15, 400, 100, 30))
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(False)
        self.startButton.setFlat(False)
        self.startButton.setFocusPolicy(Qt.ClickFocus)
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(15, 440, 100, 30))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setFocusPolicy(Qt.ClickFocus)
        self.exitButton = QtWidgets.QPushButton(self.centralWidget)
        self.exitButton.setGeometry(QtCore.QRect(15, 480, 100, 30))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setFocusPolicy(Qt.ClickFocus)
        self.score = QtWidgets.QLabel(self.centralWidget)
        self.score.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score.setObjectName("score")
        self.scores = QtWidgets.QLabel(self.centralWidget)
        self.scores.setGeometry(QtCore.QRect(20, 60, 58, 40))
        self.scores.setObjectName("scores")
        self.line = QtWidgets.QLabel(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 58, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line.setObjectName("line")
        self.lines = QtWidgets.QLabel(self.centralWidget)
        self.lines.setGeometry(QtCore.QRect(20, 140, 58, 40))
        self.lines.setObjectName("lines")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(130, 20, 250, 520))
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

