# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 840)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(100, 100))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"D:\zhang_kg\BUAA_undergraduate\2Sophomore\BUAA_Python\731work\missionlist_py\res\logo-1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 60, 30))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../res/13_icon.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        self.label_8.setGeometry(QtCore.QRect(80, 0, 60, 30))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../res/多云.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setGeometry(QtCore.QRect(150, 0, 60, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(r"..\res\晴（夜间）.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 60, 30))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(r"..\res\日历-title.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(80, 48, 300, 15))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.frame_10)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(80, 100))
        self.label_6.setMouseTracking(False)
        self.label_6.setToolTipDuration(-1)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(r"..\res\胡歌2.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"..\res\窗口最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/窗口最大化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}")
        self.pushButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8.addWidget(self.frame_11)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 40)
        self.horizontalLayout_9.setStretch(3, 1)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(100, 0))
        self.frame.setMaximumSize(QtCore.QSize(125, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font-family:微软雅黑;\n"
                                      "    background-color: rgb(248, 248, 248);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    font-family:微软雅黑;\n"
                                      "    background-color: rgb(233, 237, 238);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    font-family:微软雅黑;\n"
                                      "    background-color: rgb(233, 237, 238);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../res/sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../res/日历.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../res/搜索类目-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../res/历史数据.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(248, 248, 248);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    font-family:微软雅黑;\n"
                                        "    background-color: rgb(233, 237, 238);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../res/更多.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2.addWidget(self.frame_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                    "font-family:微软雅黑")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout_6.setStretch(0, 6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.page)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget = QtWidgets.QListWidget(self.frame_5)
        self.listWidget.setStyleSheet("border:none")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_7.addWidget(self.listWidget)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_5)
        self.page_5.setLayout(self.verticalLayout_9)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.frame_7)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_4.addWidget(self.listWidget_3)
        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.listWidget_4 = QtWidgets.QListWidget(self.frame_8)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_6.addWidget(self.listWidget_4)
        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.listWidget_5 = QtWidgets.QListWidget(self.frame_9)
        self.listWidget_5.setObjectName("listWidget_5")
        self.verticalLayout_7.addWidget(self.listWidget_5)
        self.gridLayout.addWidget(self.frame_9, 1, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_6)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_5.addWidget(self.listWidget_2)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(MainWindow.showMinimized)
        self.pushButton_7.clicked.connect(MainWindow.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.listWidget_5)
        MainWindow.setTabOrder(self.listWidget_5, self.listWidget_2)
        MainWindow.setTabOrder(self.listWidget_2, self.listWidget_4)
        MainWindow.setTabOrder(self.listWidget_4, self.listWidget_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "2022-07-30 16:55:40 星期日"))
        self.pushButton.setText(_translate("MainWindow", "今日任务"))
        self.pushButton_2.setText(_translate("MainWindow", "日程安排"))
        self.pushButton_3.setText(_translate("MainWindow", "任务检索"))
        self.pushButton_4.setText(_translate("MainWindow", "历史数据"))
        self.pushButton_5.setText(_translate("MainWindow", "更多功能"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "重要不紧急"))
        self.label_3.setText(_translate("MainWindow", "紧急不重要"))
        self.label_4.setText(_translate("MainWindow", "不重要不紧急"))
        self.label.setText(_translate("MainWindow", "重要紧急"))
