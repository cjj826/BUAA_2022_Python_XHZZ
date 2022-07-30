from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

import sys
import untitled

class masterWindow(untitled.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(masterWindow, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        #进行信号与槽的链接按钮
        self.pushButton.clicked.connect(self.display_page1)
        self.pushButton_2.clicked.connect(self.display_page2)
        self.pushButton_3.clicked.connect(self.display_page3)
        self.pushButton_4.clicked.connect(self.display_page4)
        # self.pushButton_5.clicked.connect(self.display_page5)

    def display_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_page3(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_page4(self):
        self.stackedWidget.setCurrentIndex(3)

    def display_page5(self):
        self.stackedWidget.setCurrentIndex(4)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = masterWindow()
    main_window.show()
    sys.exit(app.exec_())
