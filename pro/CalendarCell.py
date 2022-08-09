# -*- coding: utf-8 -*-#
import re
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Defines
from AddMissionWindow import AddMissionWindow
from DateLabel import DateLabel
from MissionList import MissionList
from PerpetualCalendar import getYearMonth
from MainWindow.customItem import CustomListWidgetItem
from mytask import Mytask


class CalendarCell(QWidget):
    def __init__(self, userName, calendar, mainWindow=None):
        super(CalendarCell, self).__init__()
        self.userName = userName
        self.initUI()
        self.calendar = calendar
        self.mainWindow=mainWindow
    def initUI(self):
        layout_main = QVBoxLayout()

        self.dateLabel = DateLabel()
        # self.dateLabel.setMaximumHeight(20)
        self.missionList = MissionList()
        self.missionList.clicked.connect(lambda : self.showAddMissionWindow(self.calendar, self.dateLabel))
        # data = {'Name':"ddafadfadf"}
        # self.missionList.addMissionItem(data)
        layout_main.addWidget(self.dateLabel)
        layout_main.addWidget(self.missionList)

        layout_main.setStretch(0, 1)
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)


        self.setLayout(layout_main)
        #self.setFixedSize(250, 200)
        self.setStyleSheet("QWidget{border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);}")
        # self.show()

    def getLabel(self):
        return self.dateLabel

    def getMissionList(self):
        return self.missionList

    def showAddMissionWindow(self, calendar, label):
        self.addMissionWindow = AddMissionWindow(self.userName, calendar, label, None, None, mainWindow=self.mainWindow)
        self.addMissionWindow.show()

    def updateMissionsInMissionList(self):
        year, month, day = self.getYearMonthDay(self.calendar, self.dateLabel)
        curDay = "%04d-%02d-%02d" % (year, month, day)
        print(curDay)
        tasksNeed, tasksFinished, tasksOvertime = Mytask.getAllTasks(self.userName, curDay)  # 只会获取到今日任务
        count = self.missionList.count()
        for i in range(count):
            item = self.missionList.takeItem(0)
            del item
        tasks = []
        for task in tasksNeed:
            tasks.append(task)
        for task in tasksFinished:
            tasks.append(task)
        for task in tasksOvertime:
            tasks.append(task)
        if tasks is None:
            return
        if len(tasks) == 0:
            return
        data = {'Name':""}
        for task in tasks:
            if str(task.getDeadline()).split(' ')[0] != curDay:
                continue
            data['Name'] = task.getTaskName()
            self.missionList.addMissionItem(data)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cell = CalendarCell()
    sys.exit(app.exec_())
