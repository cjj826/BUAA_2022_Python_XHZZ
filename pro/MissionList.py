# -*- coding: utf-8 -*-#
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MissionList(QListWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super(MissionList, self).__init__()
        self.setFlow(QListView.Flow(1))
        # self.setMaximumWidth(80)
        # self.setStyleSheet("QListWidget{border:0px}")
    def addMissionItem(self, data):
        item = QListWidgetItem()
        widget = QLabel(data['Name'])
        widget.setStyleSheet("QWidget{border-width: 0px;}")
        self.addItem(item)
        self.setItemWidget(item, widget)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.clicked.emit()