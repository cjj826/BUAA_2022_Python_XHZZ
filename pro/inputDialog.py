from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QGridLayout, QLabel, QPushButton, QFrame, \
    QDateTimeEdit, QDialog
from PyQt5.uic.properties import QtCore

from DateTime import DateTimeEditDemo
from mysql.MySql import MySql
from mytask import Mytask

class InputDialog(QDialog):
    def __init__(self):
        super(InputDialog,self).__init__()
        self.initUi()

    def initUi(self):
        self.set = False
        self.setWindowTitle("添加任务")
        self.setGeometry(400,400,300,260)

        self.DATE = DateTimeEditDemo()

        label1=QLabel("任务标题:")
        label2=QLabel("内容描述:")
        label3=QLabel("截止日期:")
        label4=QLabel("重要性:")

        self.titleLable = QLabel()
        self.titleLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.contentLable = QLabel()
        self.contentLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.dateLable = QLabel(" "*len('yyyy-MM-dd HH:mm'))
        self.dateLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.importanceLable = QLabel()
        self.importanceLable.setFrameStyle(QFrame.Panel|QFrame.Sunken)

        titleButton=QPushButton("编辑")
        titleButton.clicked.connect(self.setTitle)
        contentButton=QPushButton("编辑")
        contentButton.clicked.connect(self.setContent)
        dateButton=QPushButton("编辑")
        dateButton.clicked.connect(self.setDate)
        importanceButton=QPushButton("编辑")
        importanceButton.clicked.connect(self.setImportance)

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        mainLayout.addWidget(self.titleLable,0,1)
        mainLayout.addWidget(titleButton,0,2)
        mainLayout.addWidget(label2,1,0)
        mainLayout.addWidget(self.contentLable,1,1)
        mainLayout.addWidget(contentButton,1,2)
        mainLayout.addWidget(label3,2,0)
        mainLayout.addWidget(self.dateLable,2,1)
        mainLayout.addWidget(dateButton,2,2)
        mainLayout.addWidget(label4,3,0)
        mainLayout.addWidget(self.importanceLable,3,1)
        mainLayout.addWidget(importanceButton,3,2)

        # 创建按钮并绑定一个自定义槽函数
        self.confirmButton = QPushButton('确定')
        self.confirmButton.clicked.connect(self.confirm)
        mainLayout.addWidget(self.confirmButton, 4, 0)

        self.cancelButton = QPushButton('取消')
        self.cancelButton.clicked.connect(self.exit__)
        mainLayout.addWidget(self.cancelButton, 4, 2)

        self.setLayout(mainLayout)

    def setUserName(self, string):
        self.userName = string

    def setTitleAuto(self, string):
        self.titleLable.setText(string)

    def exit__(self):
        self.set = False
        self.close()

    def confirm(self):
        self.set = True
        task = Mytask(userName=self.userName,
                      taskName = self.titleLable.text(),
                      content= self.contentLable.text(),
                      deadline=self.dateLable.text(),
                      importance=self.importanceLable.text())
        task.save()
        self.close()


    def setTitle(self):
        title,ok = QInputDialog.getText(self,"任务标题","输入任务标题:",
                                       QLineEdit.Normal,self.titleLable.text())
        if ok and (len(title)!=0):
            self.titleLable.setText(title)

    def setDate(self):
        self.DATE.exec_()
        if self.DATE.set == True:
            date = self.DATE.dateEdit.dateTime().toString("yyyy-MM-dd HH:mm")
            self.dateLable.setText(date)

    def setImportance(self):
        list = ["重要","不重要"]

        style,ok = QInputDialog.getItem(self,"重要性","请选择任务重要性：",list)
        if ok :
            self.importanceLable.setText(style)

    def setContent(self):
        content,ok = QInputDialog.getMultiLineText(self,"内容描述","请输入内容描述：")
        if ok :
            self.contentLable.setText(content)



if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())