# -*- coding: utf-8 -*-#
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super(QLabel, self).__init__(parent)
        self.setFont(QFont("family", 8))
        self.setAlignment(Qt.AlignCenter)
        # self.setMaximumWidth(80)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.clicked.emit()



