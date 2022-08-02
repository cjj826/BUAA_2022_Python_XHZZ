# -*- coding: utf-8 -*-#
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ComboBox(QComboBox):
    wheeled = pyqtSignal()

    def __init__(self, parent = None):
        super(ComboBox, self).__init__(parent)
        self.setEditable(True)
        self.setView(QListView())
        self.setFixedHeight(44)
        self.setStyleSheet("QComboBox {font: 30px} "
                           "QComboBox QAbstractItemView::item {min-height: 40px; min-width: 100px; }")
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def wheelEvent(self, event):
        index = self.currentIndex()
        super().wheelEvent(event)
        if event.isAccepted() and (index == 0 or index == self.count() - 1):
            self.wheeled.emit()
