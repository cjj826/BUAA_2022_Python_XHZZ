import sys
from PyQt5.QtCore import QDate,QDateTime,QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateTimeEditDemo(QDialog):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        #设置标题与初始大小
        self.setWindowTitle('截止日期选择')
        self.resize(300,90)
        self.set = False

        #垂直布局
        layout=QGridLayout()

        #创建日期时间空间，并把当前日期时间赋值，。并修改显示格式
        self.dateEdit=QDateTimeEdit(QDateTime.currentDateTime(),self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')

        #设置日历控件允许弹出
        self.dateEdit.setCalendarPopup(True)

        #创建按钮并绑定一个自定义槽函数
        # self.btn=QPushButton('确定')
        # self.btn.clicked.connect(self.onButtonClick)

        self.confirmButton = QPushButton('确定')
        self.confirmButton.clicked.connect(self.onButtonClick)

        self.cancelButton = QPushButton('取消')
        self.cancelButton.clicked.connect(self.exit__)

        #布局控件的加载与设置
        layout.addWidget(self.dateEdit, 0, 0, 1, 2)
        layout.addWidget(self.confirmButton, 1, 0)
        layout.addWidget(self.cancelButton, 1, 1)
        self.setLayout(layout)

    def exit__(self):
        self.set = False
        self.close()

    def onButtonClick(self):
        self.set = True
        self.close()

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=DateTimeEditDemo()
    myshow.show()
    sys.exit(app.exec_())