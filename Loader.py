# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import threading
import Recoil
import os

class Ui_MainWindow(object):
    def __login(self):
        __u = self.txtUser.text()
        __p = self.txtPass.text()

        if __u and __p:
            __mydb = mysql.connector.connect(
            host="185.28.23.167",
            user="ezforus_dev",
            password="YQAGTc5",
            database="ezforus_UserList"
            )
            
            __mycursor = __mydb.cursor()
            __mycursor.execute("SELECT `id` FROM `PY` WHERE `user` = '"+ __u +"' AND `pass` = '"+ __p +"'")
            __myresult = __mycursor.fetchall()
            if (__myresult == []):
                self.lblStatus.setText("Login Failed")
            else:
                self.lblStatus.setText("Logged In")
                scriptThread = threading.Thread(target=Recoil.run)
                scriptThread.start()
                self.hide()
                scriptThread.join()
                self.close

    def __register(self):
        __u = self.txtUser.text()
        __p = self.txtPass.text()

        if __u and __p:
            __mydb = mysql.connector.connect(
            host="185.28.23.167",
            user="ezforus_dev",
            password="YQAGTc5",
            database="ezforus_UserList"
            )
            
            __mycursor = __mydb.cursor()
            __mycursor.execute("INSERT INTO `PY` (`id`, `user`, `pass`, `reg_date`) VALUES (NULL, '"+ __u +"', '"+ __p +"', current_timestamp());")
            __myresult = __mycursor.fetchall()
            if (__myresult == []):
                self.lblStatus.setText("Registered " + __u)
            else:
                self.lblStatus.setText("Register Failed")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 250))
        MainWindow.setMaximumSize(QtCore.QSize(600, 250))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(56, 56, 56)\n"
"}")
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(260, 202, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.btnRegister.setObjectName("btnRegister")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(260, 162, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.btnLogin.setCheckable(False)
        self.btnLogin.setObjectName("btnLogin")
        self.lblMain = QtWidgets.QLabel(self.centralwidget)
        self.lblMain.setGeometry(QtCore.QRect(160, 0, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Akira Expanded")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblMain.setFont(font)
        self.lblMain.setAutoFillBackground(False)
        self.lblMain.setStyleSheet("color:white;")
        self.lblMain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMain.setObjectName("lblMain")
        self.txtPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPass.setGeometry(QtCore.QRect(240, 121, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.txtPass.setFont(font)
        self.txtPass.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.txtPass.setText("")
        self.txtPass.setFrame(True)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPass.setClearButtonEnabled(False)
        self.txtPass.setObjectName("txtPass")
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(240, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.txtUser.setFont(font)
        self.txtUser.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.txtUser.setText("")
        self.txtUser.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUser.setObjectName("txtUser")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(3, 210, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.lblStatus.setFont(font)
        self.lblStatus.setStyleSheet("color:white;")
        self.lblStatus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 6))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(600, 10))
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 60, 126, 255), stop:1 rgba(35, 166, 213, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(0, 244, 600, 8))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame2.setMaximumSize(QtCore.QSize(600, 10))
        self.frame2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 60, 126, 255), stop:1 rgba(35, 166, 213, 255))")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(581, 2, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(12)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color:Transparent;\n"
"color:White;")
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtUser, self.txtPass)
        MainWindow.setTabOrder(self.txtPass, self.btnLogin)
        MainWindow.setTabOrder(self.btnLogin, self.btnRegister)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy4.me"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.lblMain.setText(_translate("MainWindow", "Easy4.me"))
        self.txtPass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.txtUser.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lblStatus.setText(_translate("MainWindow", "Status"))
        self.btnExit.setText(_translate("MainWindow", "X"))

        #Button Event
        self.btnLogin.clicked.connect(self.__login)
        self.btnRegister.clicked.connect(self.__register)
        self.btnExit.clicked.connect(self.close)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
