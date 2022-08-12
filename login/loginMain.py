from PyQt5.QtCore import QTimer
from pro.window1 import masterWindow
from mysql.MySql import MySql
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from login.loginMainWindow import Ui_MainWindow
from mytask import Mytask
from MyCalendar import MyCalendar


class loginWorkStation(Ui_MainWindow):
    def __init__(self, window):
        super(loginWorkStation, self).__init__()
        super().setupUi(window)
        self.loginwindow = window
        self.widget_2.hide()
        self.loginWork()

    def loginWork(self):
        self.pushButton.clicked.connect(self.change2register)
        self.pushButton_2.clicked.connect(self.change2login)
        self.pushButton_6.clicked.connect(self.tryRegister)
        self.pushButton_5.clicked.connect(self.tryLogin)
        self.label_10.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_9.hide()
        self.label_11.hide()
        MySql(init=True).closeDataBase()

    def loginsuccess(self):
        print("login success")
        self.main_window = masterWindow()
        self.main_window.setUser(self.userName)
        self.main_window.addCalendar()
        self.main_window.show()
        self.loginwindow.close()

    def tryLogin(self):
        username = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())
        self.userName = username
        if self.isEmpty(username):
            self.showLabel(self.label_5)
            self.lineEdit.clear()
            return
        if self.isEmpty(password):
            self.showLabel(self.label_6)
            self.lineEdit_2.clear()
            return
        mysql = MySql()
        results = mysql.select('sc_user', all=True)
        for row in results:
            name = row[1]
            key = row[2]
            if name == username:
                if key == password:
                    self.loginsuccess()
                else:
                    self.showLabel(self.label_6)
                    self.lineEdit_5.clear()
                return
        self.showLabel(self.label_9)
        self.lineEdit.clear()
        mysql.closeDataBase()

    def tryRegister(self):
        username = str(self.lineEdit_5.text())
        password = str(self.lineEdit_6.text())
        if self.isEmpty(username):
            self.showLabel(self.label_5)
            self.lineEdit_5.clear()
            return
        if self.isEmpty(password):
            self.showLabel(self.label_6)
            self.lineEdit_6.clear()
            return
        mysql = MySql()
        results = mysql.select('sc_user', listnames=['username'])
        for name in results:
            # 检查是否重复注册
            if name[0] == username:
                self.showLabel(self.label_5)
                self.lineEdit_5.clear()
                return
        dic = {"username":username, "password":password}
        mysql.insert("sc_user", dic)
        #创建该用户的数据库
        dic = Mytask.getAttr()
        mysql.createTable(tableName = 'user_'+username, attrdict= dic)
        # here
        self.showLabel(self.label_11)
        self.change2login()
        mysql.closeDataBase()


    def isEmpty(self, string):
        return string is None or string.strip() == ''

    def showLabel(self, label):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeoutEvent)
        label.show()
        self.timer.start(2000)

    def timeoutEvent(self):
        self.label_10.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_9.hide()
        self.label_11.hide()
        self.timer.stop()

    def change2register(self):
        self.widget.hide()
        self.widget_2.show()

    def change2login(self):
        self.widget_2.hide()
        self.widget.show()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    win.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    loginUi = loginWorkStation(win)
    win.show()
    sys.exit(app.exec_())