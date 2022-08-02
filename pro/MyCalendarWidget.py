# -*- encoding=utf-8 -*-
import sys
from PyQt5.QtWidgets import QCalendarWidget, QWidget, QMainWindow, QApplication, QSizePolicy, \
    QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QStringListModel, QLocale
from PyQt5.QtGui import QTextCharFormat, QFont, QColor


class MyCalendarWidget(QCalendarWidget, QMainWindow):
    def __init__(self):
        super().__init__()
        # super().setNavigationBarVisible(False)
        # self.initTopWidget()
        self.initControl()

    def initControl(self):
        # self.setLocale(QLocale.Chinese)
        self.setNavigationBarVisible(False)
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.setSelectionMode(QCalendarWidget.SingleSelection)

        format = QTextCharFormat()
        format.setForeground(QColor(51, 51, 51))
        format.setBackground(QColor(247, 247, 247))
        format.setFontFamily("Microsoft YaHei")
        format.setFontPointSize(9)
        format.setFontWeight(QFont.Medium)
        self.setWeekdayTextFormat(Qt.Saturday, format)
        self.setWeekdayTextFormat(Qt.Sunday, format)

        self.initTopWidget()
        # QCalendarWidget.currentPageChanged.connect(lambda: self.setDateLabelTimeText(2022, 2))



    def initTopWidget(self):
        self.topWidget = QWidget()
        self.topWidget.setObjectName('CalendarTopWidget')
        self.topWidget.setFixedHeight(50)
        self.topWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(12, 0, 12, 0)
        hboxLayout.setSpacing(4)

        self.m_leftMonthBtn = QPushButton()
        self.m_leftMonthBtn.setText('<')
        self.m_rightMonthBtn = QPushButton()
        self.m_rightMonthBtn.setText('>')
        self.m_dataLabel = QLabel()

        self.m_leftMonthBtn.setObjectName('CalendarLeftMonthBtn')
        self.m_rightMonthBtn.setObjectName('CalendarRightMonthBtn')
        self.m_dataLabel.setObjectName('CalendarDataLabel')

        self.m_leftMonthBtn.setFixedSize(16, 16)
        self.m_rightMonthBtn.setFixedSize(16, 16)

        hboxLayout.addStretch()
        hboxLayout.addWidget(self.m_leftMonthBtn)
        hboxLayout.addWidget(self.m_dataLabel)
        hboxLayout.addWidget(self.m_rightMonthBtn)
        hboxLayout.addStretch()
        self.topWidget.setLayout(hboxLayout)

        vBodyLayout = QVBoxLayout()
        vBodyLayout.insertWidget(0, self.topWidget)
        # vBodyLayout.insertWidget(1, self)

        self.m_leftMonthBtn.clicked.connect(self.onbtnClicked)
        self.m_rightMonthBtn.clicked.connect(self.onbtnClicked)
        self.setDateLabelTimeText(self.selectedDate().year(), self.selectedDate().month())

    def onbtnClicked(self):
        sender = self.sender()
        if sender == self.m_leftMonthBtn:
            self.showPreviousMonth()
        elif sender == self.m_rightMonthBtn:
            self.showNextMonth()
    def setDateLabelTimeText(self, year, month):
        self.m_dataLabel.setText(str(year) + "nian" + str(month) + "yue")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyCalendarWidget()
    ex.initTopWidget()
    ex.show()
    sys.exit(app.exec_())