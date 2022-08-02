# -*- coding: utf-8 -*-#
import sys

from MissionList import MissionList
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DateLabel import DateLabel
from inputDialog import InputDialog

class AddMissionWindow(QWidget):
    def __init__(self, cellDateLabel: DateLabel, cellMissionList: MissionList):
        super(AddMissionWindow, self).__init__()
        self.initWindow(cellDateLabel, cellMissionList)

    def initWindow(self, cellDateLabel: DateLabel, cellMissionList: MissionList):
        layout_main = QVBoxLayout()

        self.dateLabel = DateLabel()

        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                    "font-family:微软雅黑")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("添加任务，按回车创建")
        self.lineEdit.returnPressed.connect(self.addAssignment)

    def addAssignment(self):
        # print(self.lineEdit.text())
        self.INPUT = InputDialog()
        self.INPUT.setTitleAuto(self.lineEdit.text())
        self.INPUT.setUserName(self.userName)
        self.INPUT.exec_()

        if self.INPUT.set == True:
            l = [self.INPUT.titleLable.text(), self.INPUT.contentLable.text(),
                 self.INPUT.dateLable.text(), self.INPUT.importanceLable.text()]
            print(l)
            self.updateListWidget()



