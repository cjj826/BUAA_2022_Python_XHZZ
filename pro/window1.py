from typing import Union

from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QListWidgetItem, QCheckBox, QLabel, QSizePolicy,
                             QPushButton)
from PyQt5.QtCore import QObject, Qt, pyqtSignal, QTimer, QDateTime, QSize, QPropertyAnimation, QRect
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

import sys

from pyqt5_plugins.examplebutton import QtWidgets

import untitled
from MyCalendar import MyCalendar
from customItem import CustomListWidgetItem
from inputDialog import InputDialog
from mytask import Mytask

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

        #设计侧边栏，侧边栏应该是mainWindow的一个属性，尝试对象是widget
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.showSider)
        self.button.move(0, 800)

        self.pushButton_10.clicked.connect(self.hideSider)

        #侧边栏编辑提示文本
        self.lineEdit_2.setPlaceholderText("任务标题")
        self.textEdit_2.setPlaceholderText("内容描述")
        self.textEdit_3.setPlaceholderText("截止日期")
        self.textEdit_4.setPlaceholderText("重要性")

    def showSider(self):
        self.widget.show()
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

    def hideSider(self):
        self.widget.hide()


    def addCalendar(self):
        pass
        # self.calendar = MyCalendar(self.userName)
        # self.verticalLayout_9.addWidget(self.calendar)
        # self.verticalLayout_9.addWidget(MyCalendar(self.userName))
        # self.calendar.show()
<<<<<<< HEAD
        pass
=======

>>>>>>> 3a3b95f70ddaf9fc99baee3e289d704ef82c31d6
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
            self.updateListWidget()

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
        self.updateListWidget()

    def updateListWidget(self):
        tasks = Mytask.getTasks(self.userName)#只会获取到今日任务
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.takeItem(0)
            del item
        if tasks is None:
            return
        for task in tasks:
            item = CustomListWidgetItem(task)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,item.widget)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = masterWindow()
    main_window.setUser("15978757317")
    main_window.show()
    sys.exit(app.exec_())
