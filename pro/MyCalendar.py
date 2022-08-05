# -*- coding: utf-8 -*-#
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CalendarCell import CalendarCell
from ComboBox import ComboBox
from Defines import *
from DateLabel import DateLabel
from PerpetualCalendar import displayDate, yearItems, jumpYear, jumpMonth, lastMonth, nextMonth, lastYear, nextYear


class MyCalendar(QWidget):
    def __init__(self, userName):
        super().__init__()
        # self.wnlWidget = QWidget()
        self.userName = userName
        self.setupUI()


    def setupUI(self):
        pe = QPalette()
        pe.setColor(QPalette.Window, QColor(250, 255, 255))
        self.setPalette(pe)
        # self.setFixedSize(2500, 1800)
        self.setWindowTitle("万年历")
        # self.setCentralWidget(self.wnlWidget)

        self.calendarUI()
        displayDate(self)
        # self.show()

    def calendarUI(self):
        self.gridWNL = QGridLayout()
        self.setLayout(self.gridWNL)
        # self.wnlWidget.setLayout(self.gridWNL)
        self.gridWNL.setSpacing(0)
        self.hlayWNL = QHBoxLayout()
        self.hlayWNL.setContentsMargins(3, 0, 5, 0)
        # 添加一条水平的展示条
        self.gridWNL.addLayout(self.hlayWNL, 0, 0, 1, 7)

        ### Century Combo Box
        self.comboBoxCentury = ComboBox()
        # self.comboBoxCentury.setMaximumWidth(160)  # set size
        for i in range(startCentury, endCentury + 1):
            if i < 0:
                self.comboBoxCentury.addItem('BC' + str(abs(i)) + '世纪')
            elif i == 0: continue
            else:
                self.comboBoxCentury.addItem(str(i) + '世纪')
        self.comboBoxCentury.currentIndexChanged.connect(lambda : yearItems(self))
        self.comboBoxCentury.activated.connect(lambda : displayDate(self))
        self.hlayWNL.addWidget(self.comboBoxCentury)

        ### Year Combo Box && Last|Next Year Button
        self.comboBoxYear = ComboBox()
        # self.comboBoxYear.setFixedWidth(164)        # set size
        self.comboBoxYear.activated.connect(lambda : displayDate(self))
        self.comboBoxYear.wheeled.connect(lambda : jumpYear(self))

        self.buttonLastYear = QPushButton('<')
        self.buttonNextYear = QPushButton('>')
        # self.buttonNextYear.setMaximumSize(32, 44)  # set size
        # self.buttonLastYear.setMaximumSize(32, 44)  # set size
        self.buttonNextYear.clicked.connect(self.thisJumpMonth)
        self.buttonLastYear.clicked.connect(self.thisJumpMonth)

        self.hlayWNL.addStretch(1)
        self.hlayWNL.addWidget(self.buttonLastYear)
        self.hlayWNL.addWidget(self.comboBoxYear)
        self.hlayWNL.addWidget(self.buttonNextYear)

        ### Month Combo Box && Last|Next Month Button
        self.comboBoxMonth = ComboBox()
        # initial inside months
        for month in range(1, 12 + 1, 1):
            self.comboBoxMonth.addItem(str(month) + '月')
        self.comboBoxMonth.setMaxVisibleItems(12)
        self.comboBoxMonth.setFocusPolicy(False)
        self.comboBoxMonth.setFocusPolicy(Qt.NoFocus)
        # self.comboBoxMonth.setMaximumWidth(120)

        self.comboBoxMonth.activated.connect(lambda : displayDate(self))
        self.comboBoxMonth.wheeled.connect(lambda : jumpMonth(self))

        # Last|Next Month Button
        self.buttonLastMonth = QPushButton('<')
        self.buttonNextMonth = QPushButton('>')
        # self.buttonLastMonth.setMaximumSize(32, 44)
        # self.buttonNextMonth.setMaximumSize(32, 44)

        self.buttonLastMonth.clicked.connect(self.thisJumpMonth)
        self.buttonNextMonth.clicked.connect(self.thisJumpMonth)

        self.hlayWNL.addStretch(1)
        self.hlayWNL.addWidget(self.buttonLastMonth)
        self.hlayWNL.addWidget(self.comboBoxMonth)
        self.hlayWNL.addWidget(self.buttonNextMonth)
        self.hlayWNL.addStretch(1)

        ### Today Button
        self.buttonToday = QPushButton()
        # self.buttonToday.setMaximumWidth(72)

        self.buttonToday.clicked.connect(lambda : displayDate(self))

        self.hlayWNL.addWidget(self.buttonToday)

        ### Main Calendar Title
        self.labelMonday    = DateLabel("一")
        self.labelTuesday   = DateLabel("二")
        self.labelWednesDay = DateLabel("三")
        self.labelThursDay  = DateLabel("四")
        self.labelFriday    = DateLabel("五")
        self.labelSaturday  = DateLabel("六")
        self.labelSunday    = DateLabel("日")
        labelWeeks = [self.labelMonday, self.labelTuesday, self.labelWednesDay, self.labelThursDay, self.labelFriday, self.labelSaturday, self.labelSunday]

        for i in range(7):
            self.gridWNL.addWidget(labelWeeks[i], 1, i)
            # labelWeeks[i].setMaximumHeight(80)

        ### Main Calendar Content
        self.labs = []
        for i in range(6):
            for j in range(7):
                if j == 0:
                    self.labs.append([CalendarCell(self.userName, self)])
                else:
                    self.labs[i].append(CalendarCell(self.userName, self))
                # self.labs[i][j].setFixedSize(350, 300)
                self.labs[i][j].getLabel().clicked.connect(lambda : displayDate(self))
                # self.labs[i][j].getMissionList().clicked.connect(lambda : ) TODO
                self.gridWNL.addWidget(self.labs[i][j], i + 2, j)
        ## make it tighter
        for i in range(6):
            self.gridWNL.setRowStretch(i + 2, 1)
        for j in range(7):
            self.gridWNL.setColumnStretch(j, 1)
        self.gridWNL.setContentsMargins(20, 0, 20, 0)
        self.gridWNL.setSpacing(0)

        ### Find Festival Combo Box
        self.comboBoxFindFestival = QComboBox()
        self.comboBoxFindFestival.addItem('查找农历节日')

        for festival in LUNAR_FRSTIVALS:
            self.comboBoxFindFestival.addItem(festival[-1])

        self.comboBoxFindFestival.activated.connect(self.thisJumpFestival)
        self.comboBoxFindFestival.setStyleSheet("QComboBox { leftPadding: 1px}")
        # self.comboBoxFindFestival.setMaximumWidth(250)

        self.hlayGL = QHBoxLayout()
        self.hlayGL.addWidget(self.comboBoxFindFestival)

        ### Calendar information
        self.labInfo = QLabel()
        self.labInfo.setStyleSheet("QLabel{ font:14px;}")
        self.labInfo.setAlignment(Qt.AlignHCenter)
        self.labInfo.setContentsMargins(0, 6, 5, 6)
        self.labInfo.setWordWrap(True)
        # self.labInfo.setFixedWidth(250)
        self.gridWNL.addLayout(self.hlayGL, 0, 7, 1, 1)
        self.gridWNL.addWidget(self.labInfo, 1, 7, 7, 1)

    def thisJumpMonth(self):
        if self.sender() == self.buttonLastMonth:
            lastMonth(self)
            print("last month")
        elif self.sender() == self.buttonNextMonth:
            nextMonth(self)
            print("next month")
        elif self.sender() == self.buttonLastYear:
            lastYear(self)
            print("last year")
        elif self.sender() == self.buttonNextYear:
            nextYear(self)
            print("next year")
        displayDate(self)

    def thisJumpFestival(self):
        if self.comboBoxFindFestival.currentText() != '查找农历节日':
            print("find festival")
            displayDate(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cell = MyCalendar('15978757317')
    cell.show()
    sys.exit(app.exec_())