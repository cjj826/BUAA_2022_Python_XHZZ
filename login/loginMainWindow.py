from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 311, 391))
        self.label.setStyleSheet("border-image: url(:/images/images/loginback.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 0, 311, 391))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(340, 100, 261, 241))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 211, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 54, 12))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(104, 114, 130)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 54, 12))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(104, 114, 130)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"border:none;\n"
"color:rgb(0, 140, 142);\n"
"}\n"
"#pushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 160, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    background-color:rgb(0, 140, 142);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"}\n"
"#pushButton_5:hover{\n"
"    background-color: rgb(0,130,142);\n"
"}\n"
"#pushButton_5:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(340, 100, 261, 241))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 110, 211, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 54, 12))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(104, 114, 130)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 54, 12))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(104, 114, 130)")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"border:none;\n"
"color:rgb(0, 140, 142);\n"
"}\n"
"#pushButton_2:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 160, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    background-color:rgb(0, 140, 142);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"}\n"
"#pushButton_6:hover{\n"
"    background-color: rgb(0,130,142);\n"
"}\n"
"#pushButton_6:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 0, 21, 16))
        self.pushButton_3.setStyleSheet("border-image: url(:/icons/icons/close.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 370, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(229, 77, 66);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 370, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(229, 77, 66);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 370, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(229, 77, 66);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 370, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(229, 77, 66);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 370, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(22, 194, 194);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入你的账号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "输入你的密码"))
        self.label_3.setText(_translate("MainWindow", "账号"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "新用户注册"))
        self.pushButton_5.setText(_translate("MainWindow", "登录"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "输入你的注册账号"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "输入你的注册密码"))
        self.label_7.setText(_translate("MainWindow", "注册账号"))
        self.label_8.setText(_translate("MainWindow", "密码"))
        self.pushButton_2.setText(_translate("MainWindow", "返回登录"))
        self.pushButton_6.setText(_translate("MainWindow", "注册"))
        self.label_5.setText(_translate("MainWindow", "  账号有误，请重新输入"))
        self.label_6.setText(_translate("MainWindow", "  密码有误，请重新输入"))
        self.label_9.setText(_translate("MainWindow", "  账号尚未注册"))
        self.label_10.setText(_translate("MainWindow", "  密码错误"))
        self.label_11.setText(_translate("MainWindow", "  注册成功"))

    # def loginWork(self):
    #     self.pushButton.clicked.connect(self.change2register)
    #     self.pushButton_2.clicked.connect(self.change2login)
    #     self.pushButton_6.clicked.connect(self.tryRegister)
    #     self.pushButton_5.clicked.connect(self.tryLogin)
    #     self.label_10.hide()
    #     self.label_5.hide()
    #     self.label_6.hide()
    #     self.label_9.hide()
    #     self.label_11.hide()
    #     MySql(init=True).closeDataBase()
    #
    # def loginsuccess(self):
    #     print("success")
    #     pass
    #
    # def tryLogin(self):
    #     username = str(self.lineEdit.text())
    #     password = str(self.lineEdit_2.text())
    #     if self.isEmpty(username):
    #         self.showLabel(self.label_5)
    #         self.lineEdit.clear()
    #         return
    #     if self.isEmpty(password):
    #         self.showLabel(self.label_6)
    #         self.lineEdit_2.clear()
    #         return
    #     mysql = MySql()
    #     results = mysql.select('sc_user', all=True)
    #     for row in results:
    #         name = row[1]
    #         key = row[2]
    #         if name == username:
    #             if key == password:
    #                 self.loginsuccess()
    #             else:
    #                 self.showLabel(self.label_6)
    #                 self.lineEdit_5.clear()
    #             return
    #     self.showLabel(self.label_9)
    #     self.lineEdit.clear()
    #     mysql.closeDataBase()
    #
    # def tryRegister(self):
    #     username = str(self.lineEdit_5.text())
    #     password = str(self.lineEdit_6.text())
    #     if self.isEmpty(username):
    #         self.showLabel(self.label_5)
    #         self.lineEdit_5.clear()
    #         return
    #     if self.isEmpty(password):
    #         self.showLabel(self.label_6)
    #         self.lineEdit_6.clear()
    #         return
    #     mysql = MySql()
    #     results = mysql.select('sc_user', listnames=['username'])
    #     for name in results:
    #         # 重复注册
    #         if name[0] == username:
    #             self.showLabel(self.label_5)
    #             self.lineEdit_5.clear()
    #             return
    #     dic = {"username":username, "password":password}
    #     mysql.insert("sc_user", dic)
    #     mysql.closeDataBase()
    #     # here
    #     self.showLabel(self.label_11)
    #     self.change2login()
    #
    # def isEmpty(self, string):
    #     return string is None or string.strip() == ''
    #
    # def showLabel(self, label):
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.timeoutEvent)
    #     label.show()
    #     self.timer.start(2000)
    #
    # def timeoutEvent(self):
    #     self.label_10.hide()
    #     self.label_5.hide()
    #     self.label_6.hide()
    #     self.label_9.hide()
    #     self.label_11.hide()
    #     self.timer.stop()
    #
    # def change2register(self):
    #     self.widget.hide()
    #     self.widget_2.show()
    #
    # def change2login(self):
    #     self.widget_2.hide()
    #     self.widget.show()
import resources_rc
