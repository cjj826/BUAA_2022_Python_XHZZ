# -*- coding: utf-8 -*-#
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DateLabel import DateLabel
from MissionList import MissionList

class CalendarCell(QWidget):
    def __init__(self):
        super(CalendarCell, self).__init__()
        self.initUI()

    def initUI(self):
        layout_main = QVBoxLayout()

        self.dateLabel = DateLabel()
        # self.dateLabel.setMaximumHeight(20)
        self.missionList = MissionList()
        # data = {'Name':"ddafadfadf"}
        # self.missionList.addMissionItem(data)
        layout_main.addWidget(self.dateLabel)
        layout_main.addWidget(self.missionList)

        layout_main.setStretch(0, 1)
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)


        self.setLayout(layout_main)
        self.setFixedSize(250, 200)
        self.setStyleSheet("QWidget{border:0px}")
        # self.show()

    def getLabel(self):
        return self.dateLabel

    def getMissionList(self):
        return self.missionList


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cell = CalendarCell()
    sys.exit(app.exec_())