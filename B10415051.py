# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 600)
        MainWindow.setStyleSheet("""
                * {
                    background: #006400;
                    color: #ffffff;
                    front-size: 14px;
                }
                QPushButon {
                    background: #13398b;
                    border-raduis: 8px;
                }
                QPushButton#exitButton:hover {
                    background: #ff6259;
                }
                QPushButton:disabled {
                    color: #7f8081;
                    background: #042569;
                }
                QFrame {
                    background: #8FBC8F;
                    border: 2px solid #13398b;
                }
                QLabel {
                    background: #006400;
                    border: none;
                }
                QLabel#scores {
                    frond-size: 30px;
                }
                QLabel#lines {
                    font-size: 15px;
                }
                QStatusBar {
                    background: #006400;
                }
                """)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.score = QtWidgets.QLabel(self.centralWidget)
        self.score.setGeometry(QtCore.QRect(300, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score.setObjectName("score")
        self.scores = QtWidgets.QLabel(self.centralWidget)
        self.scores.setGeometry(QtCore.QRect(300, 70, 58, 15))
        self.scores.setObjectName("scores")
        self.line = QtWidgets.QLabel(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(290, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line.setObjectName("line")
        self.lines = QtWidgets.QLabel(self.centralWidget)
        self.lines.setGeometry(QtCore.QRect(300, 120, 58, 15))
        self.lines.setObjectName("lines")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 251, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(280, 410, 93, 28))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.startButton.setFont(font)
        self.startButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(False)
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(280, 450, 93, 28))
        self.pauseButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pauseButton.setObjectName("pauseButton")
        self.exitButton = QtWidgets.QPushButton(self.centralWidget)
        self.exitButton.setGeometry(QtCore.QRect(280, 490, 93, 28))
        font = QtGui.QFont()
        font.setKerning(True)
        self.exitButton.setFont(font)
        self.exitButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.exitButton.setObjectName("exitButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 380, 21))
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
        self.score.setText(_translate("MainWindow", "SCORE"))
        self.scores.setText(_translate("MainWindow", "TextLabel"))
        self.line.setText(_translate("MainWindow", "Complete"))
        self.lines.setText(_translate("MainWindow", "TextLabel"))
        self.startButton.setText(_translate("MainWindow", "START Button"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE Button"))
        self.exitButton.setText(_translate("MainWindow", "EXIT Button"))

