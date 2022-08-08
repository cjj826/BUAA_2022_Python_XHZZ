# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAssignment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(694, 568)
        dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_3.setContentsMargins(50, 50, 80, 60)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setStyleSheet("font-family:微软雅黑")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.title = QtWidgets.QLineEdit(dialog)
        self.title.setMinimumSize(QtCore.QSize(170, 0))
        self.title.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_2 = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.type = QtWidgets.QComboBox(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        self.type.setMinimumSize(QtCore.QSize(170, 0))
        self.type.setMaximumSize(QtCore.QSize(150, 16777215))
        self.type.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.horizontalLayout.addWidget(self.type)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.start = QtWidgets.QDateTimeEdit(dialog)
        self.start.setMinimumSize(QtCore.QSize(170, 0))
        self.start.setMaximumSize(QtCore.QSize(170, 16777215))
        self.start.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.label_11 = QtWidgets.QLabel(dialog)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_4 = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.end = QtWidgets.QDateTimeEdit(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end.sizePolicy().hasHeightForWidth())
        self.end.setSizePolicy(sizePolicy)
        self.end.setMinimumSize(QtCore.QSize(170, 0))
        self.end.setMaximumSize(QtCore.QSize(170, 16777215))
        self.end.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.end.setObjectName("end")
        self.horizontalLayout_2.addWidget(self.end)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 3)
        self.horizontalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.time = QtWidgets.QTimeEdit(dialog)
        self.time.setMinimumSize(QtCore.QSize(170, 0))
        self.time.setMaximumSize(QtCore.QSize(170, 16777215))
        self.time.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.time.setObjectName("time")
        self.horizontalLayout_3.addWidget(self.time)
        self.label_12 = QtWidgets.QLabel(dialog)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.importance = QtWidgets.QComboBox(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importance.sizePolicy().hasHeightForWidth())
        self.importance.setSizePolicy(sizePolicy)
        self.importance.setMinimumSize(QtCore.QSize(170, 22))
        self.importance.setMaximumSize(QtCore.QSize(150, 16777215))
        self.importance.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.importance.setObjectName("importance")
        self.importance.addItem("")
        self.importance.addItem("")
        self.horizontalLayout_3.addWidget(self.importance)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setStyleSheet("\n"
"font-family:微软雅黑")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.content = QtWidgets.QTextEdit(dialog)
        self.content.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"font-family:微软雅黑")
        self.content.setObjectName("content")
        self.horizontalLayout_4.addWidget(self.content)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.confirmButton = QtWidgets.QPushButton(dialog)
        self.confirmButton.setMinimumSize(QtCore.QSize(0, 40))
        self.confirmButton.setStyleSheet("QPushButton{\n"
"    font-family:微软雅黑;\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    font-family:微软雅黑;\n"
"    color:white;\n"
"    background-color: rgb(0, 171, 214);\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-family:微软雅黑;\n"
"    background-color: rgb(233, 237, 238);\n"
"    border: none;\n"
"}\n"
"")
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_5.addWidget(self.confirmButton)
        self.label_10 = QtWidgets.QLabel(dialog)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.cancelButton = QtWidgets.QPushButton(dialog)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancelButton.setStyleSheet("QPushButton{\n"
"    font-family:微软雅黑;\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    font-family:微软雅黑;    \n"
"    color:white;\n"
"    background-color: rgb(0, 171, 214);\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    font-family:微软雅黑;\n"
"    background-color: rgb(233, 237, 238);\n"
"    border: none;\n"
"}\n"
"")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_5.addWidget(self.cancelButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "添加任务"))
        self.label.setText(_translate("dialog", "任务标题"))
        self.label_2.setText(_translate("dialog", "任务种类"))
        self.type.setItemText(0, _translate("dialog", "运动"))
        self.type.setItemText(1, _translate("dialog", "学习"))
        self.type.setItemText(2, _translate("dialog", "娱乐"))
        self.type.setItemText(3, _translate("dialog", "生活"))
        self.label_3.setText(_translate("dialog", "开始时间"))
        self.label_4.setText(_translate("dialog", "结束时间"))
        self.label_5.setText(_translate("dialog", "预估时间"))
        self.label_6.setText(_translate("dialog", "重要性"))
        self.importance.setItemText(0, _translate("dialog", "重要"))
        self.importance.setItemText(1, _translate("dialog", "不重要"))
        self.label_7.setText(_translate("dialog", "任务内容"))
        self.confirmButton.setText(_translate("dialog", "确认"))
        self.cancelButton.setText(_translate("dialog", "取消"))
