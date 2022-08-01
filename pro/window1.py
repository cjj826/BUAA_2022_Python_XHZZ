from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QListWidgetItem)
from PyQt5.QtCore import QObject, Qt, pyqtSignal, QTimer, QDateTime
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

import sys
import untitled
from inputDialog import InputDialog

class masterWindow(untitled.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(masterWindow, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        #进行信号与槽的链接按钮
        self.pushButton.clicked.connect(self.display_page1)
        self.pushButton_2.clicked.connect(self.display_page2)
        self.pushButton_3.clicked.connect(self.display_page3)
        self.pushButton_4.clicked.connect(self.display_page4)
        # self.pushButton_5.clicked.connect(self.display_page5)
        self.label_11.setText("2022-07-30 16:55:40 星期日")
        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms
        self.lineEdit.setPlaceholderText("添加任务，按回车创建")
        self.lineEdit.returnPressed.connect(self.addAssignment)

    def addAssignment(self):
        #print(self.lineEdit.text())
        self.INPUT = InputDialog()
        self.INPUT.setTitleAuto(self.lineEdit.text())
        self.INPUT.setUserName(self.userName)
        self.INPUT.exec_()

        if self.INPUT.set == True:
            l = [self.INPUT.titleLable.text(), self.INPUT.contentLable.text(),
                 self.INPUT.dateLable.text(), self.INPUT.importanceLable.text()]
            print(l)

    def showtime(self):
        time=QDateTime.currentDateTime()#获取当前时间
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下时间
        self.label_11.setText(timedisplay)

    def display_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_page3(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_page4(self):
        self.stackedWidget.setCurrentIndex(3)

    def display_page5(self):
        self.stackedWidget.setCurrentIndex(4)

    def setUser(self, username):
        self.userName = username
        print(self.userName)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = masterWindow()
    main_window.show()
    sys.exit(app.exec_())
