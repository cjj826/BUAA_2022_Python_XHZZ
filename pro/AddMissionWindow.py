# -*- coding: utf-8 -*-#
import sys

import Defines
from MissionList import MissionList
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DateLabel import DateLabel
from MainWindow.customItem import CustomListWidgetItem
from addDialog import AddDialog
from inputDialog import InputDialog
from mytask import Mytask
from PerpetualCalendar import *


class AddMissionWindow(QWidget):
    def __init__(self, username, calendar, label, cellDateLabel: DateLabel, cellMissionList: MissionList):
        super(AddMissionWindow, self).__init__()
        self.initWindow(username, calendar, label, cellDateLabel, cellMissionList)

    def getYearMonthDay(self, calendar, label):
        year, month = getYearMonth(calendar)
        day = int(re.findall(r'(\d+)</font>', label.text())[0])
        if re.search(r"<font style='font-size:%dpx; text-align:center; color:gray"%(Defines.LABEL_SIZE), label.text()):
            if day > 20:
                month = month - 1
            else:
                month = month + 1
        month = month + 1
        if month <= 0:
            year -= 1
            month = 12
        if month > 12:
            month = 1
            year += 1
        return year, month, day

    def initWindow(self, username, calendar, label, cellDateLabel: DateLabel, cellMissionList: MissionList):
        layout_main = QVBoxLayout()
        self.userName = username
        self.dateLabel = DateLabel()
        self.year, self.month, self.day = self.getYearMonthDay(calendar, label)

        # self.dateLabel.setText(str(self.year) + "-" + str(self.month) + "-" + str(self.day))
        self.dateLabel.setText("%04d-%02d-%02d"%(self.year, self.month, self.day))
        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                    "font-family:微软雅黑")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("添加任务，按回车创建")
        self.lineEdit.returnPressed.connect(self.addAssignment)

        self.listWidget = QListWidget()
        layout_main.addWidget(self.dateLabel)
        layout_main.addWidget(self.lineEdit)
        layout_main.addWidget(self.listWidget)
        self.updateListWidget()
        self.setLayout(layout_main)

    def addAssignment(self):
        # print(self.lineEdit.text())
        # self.INPUT = InputDialog()
        # self.INPUT.setTitleAuto(self.lineEdit.text())
        # self.INPUT.setUserName(self.userName)
        # self.INPUT.exec_()
        #
        # if self.INPUT.set == True:
        #     l = [self.INPUT.titleLable.text(), self.INPUT.contentLable.text(),
        #          self.INPUT.dateLable.text(), self.INPUT.importanceLable.text()]
        #     print(l)
        #     self.updateListWidget()
        self.INPUT = AddDialog()
        self.INPUT.setTitleAuto(self.lineEdit.text())
        self.INPUT.setUserName(self.userName)
        self.INPUT.exec_()

        if self.INPUT.set == True:
            l = [self.INPUT.title.text(), self.INPUT.type.currentText(),
                 self.INPUT.start.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.time.time().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.content.toPlainText(), self.INPUT.importance.currentText()]
            print(l)
            self.updateListWidget()

    def updateListWidget(self):
        # tasks = Mytask.getAllTasks(self.userName)#只会获取到今日任务
        # count = self.listWidget.count()
        # for i in range(count):
        #     item = self.listWidget.takeItem(0)
        #     del item
        # if tasks is None:
        #     return
        # if len(tasks) == 0:
        #     return
        # for task in tasks:
        #     if str(task.getDeadline()).split(' ')[0] != self.dateLabel.text():
        #         continue
        #     item = CustomListWidgetItem(task, self)
        #     self.listWidget.addItem(item)
        #     self.listWidget.setItemWidget(item,item.widget)
        tasksNeed, tasksFinished, tasksOvertime = Mytask.getAllTasks(self.userName, self.dateLabel.text())  # 只会获取到今日任务
        print("hhh")
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.takeItem(0)
            del item

        for i, task in enumerate(tasksNeed):
            if i == 0:
                item = CustomListWidgetItem(task, self, mode=0, firstItem=True)
            else:
                item = CustomListWidgetItem(task, self, mode=0, firstItem=False)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)

        if len(tasksFinished) != 0:
            item = CustomListWidgetItem(None, self, mode=1, firstItem=True)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)
        for task in tasksFinished:
            item = CustomListWidgetItem(task, self, mode=1)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)

        if len(tasksOvertime) != 0:
            item = CustomListWidgetItem(None, self, mode=2, firstItem=True)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)
        for task in tasksOvertime:
            item = CustomListWidgetItem(task, self, mode=2)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddMissionWindow('Zhangkg', None, None)
    ex.show()
    sys.exit(app.exec_())


