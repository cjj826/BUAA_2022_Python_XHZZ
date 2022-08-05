from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyQwidget(QWidget):
    clicked = pyqtSignal()
    def __init__(self, parent = None):
        super(MyQwidget, self).__init__(parent)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.clicked.emit()