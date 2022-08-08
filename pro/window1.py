from datetime import datetime

from PyQt5.QtWidgets import (QApplication,
                             QMainWindow)
from PyQt5.QtCore import QTimer, QDateTime

import sys

import DateTime
import untitled
from MainWindow.customItem import CustomListWidgetItem
from MyCalendar import MyCalendar
from inputDialog import InputDialog
from addDialog import AddDialog
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
        # self.button = QPushButton("Start", self)
        # self.button.clicked.connect(self.showSider)
        # self.button.move(0, 800)

        self.pushButton_10.clicked.connect(self.hideSider)
        self.pushButton_11.clicked.connect(self.deleteTask)
        #侧边栏
        self.start.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.end.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.start.setCalendarPopup(True)
        self.end.setCalendarPopup(True)

        self.widget.hide()
        self.title.editingFinished.connect(self.update_taskName)
        self.content.textChanged.connect(self.update_taskContent) #content
        self.time.dateTimeChanged.connect(self.update_taskDeadline)#not sure
        self.importance.currentIndexChanged.connect(self.update_taskImportance)#update importance
        self.showingTask = None

    def update_taskName(self):
        self.showingTask.updateTask("taskName", self.title.text())

    def update_taskContent(self):
        self.showingTask.updateTask("content", self.content.toPlainText())

    def update_taskDeadline(self):
        self.showingTask.updateTask("deadline", self.end.dateTime().toString("yyyy-MM-dd HH:mm"))

    def update_taskImportance(self):
        self.showingTask.updateTask("importance", self.importance.currentText())


    def showSider(self, task):
        """展示侧边栏
        """
        self.showingTask = task
        self.widget.show()
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.title.setText(task.taskName)
        self.content.setPlainText(task.content)
        self.end.setDateTime(datetime.strptime(task.deadline, "%Y-%m-%d %H:%M"))
        self.importance.setCurrentText(task.importance)

    def deleteTask(self):
        """通过侧边栏删除任务；删除按钮的slot函数
        """
        # self.lineEdit_2.clear()
        # self.textEdit_2.clear()
        # self.textEdit_3.clear()
        # self.textEdit_4.clear()
        self.showingTask.delete()
        self.showingTask = None
        self.hideSider()

    def hideSider(self):
        """隐藏侧边栏
        """
        self.widget.hide()
        if self.showingTask is not None:
            self.showingTask.updateSql()
        self.updateListWidget()


    def addCalendar(self):
        self.calendar = MyCalendar(self.userName)
        self.calendarVerticalLayout.addWidget(self.calendar)
        # self.calendarVerticalLayout.addWidget(MyCalendar(self.userName))
        self.calendar.show()

    def addAssignment(self):
        #print(self.lineEdit.text())
        self.INPUT = AddDialog()
        self.INPUT.setTitleAuto(self.lineEdit.text())
        self.INPUT.setUserName(self.userName)
        self.INPUT.exec_()

        if self.INPUT.set == True:
            l = [self.INPUT.title.text(), self.INPUT.type.currentText(),
                 self.INPUT.start.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.time.time().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.content.toPlainText(),self.INPUT.importance.currentText()]
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
            item.addMasterWindow(self)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,item.widget)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = masterWindow()
    main_window.setUser("Zhangkg")
    main_window.show()
    sys.exit(app.exec_())
