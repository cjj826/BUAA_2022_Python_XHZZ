import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Activetime(QWidget):
    #初始化
    def __init__(self):
        super(Activetime, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("动态显示时间")
        self.resize(200,100)

        self.lable=QLabel()
        self.button1=QPushButton("开始时间")
        self.button2=QPushButton("结束")
        #设置网格布局
        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showtime)#这个通过调用槽函数来刷新时间
        layout.addWidget(self.lable,0,0,1,2)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,1,1)
        self.setLayout(layout)
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms


    def showtime(self):

        time=QDateTime.currentDateTime()#获取当前时间
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下时间
        print(timedisplay)
        self.lable.setText(timedisplay)

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Activetime()
    main.show()
    sys.exit(app.exec_())