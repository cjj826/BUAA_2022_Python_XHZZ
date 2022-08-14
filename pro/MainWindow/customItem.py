from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QCheckBox, QLabel, QHBoxLayout

from MainWindow.myQwidget import MyQwidget
from datetime import datetime

from mytask import Mytask


class CustomListWidgetItem(QListWidgetItem):
    count = 0
    clicked = pyqtSignal()
    def __init__(self, task : Mytask, window, mode = 0, firstItem = False):#0 is taskNeed, 1 is finished, 2 is overtime
        """创建任务列表项

        :param task: 任务
        :param mode: 0 is taskNeed, 1 is taskFinished, 2 is taskOvertime
        :param firstItem: 对于mode == 0来说，第一个任务将canStart赋值为True
        """
        super(CustomListWidgetItem, self).__init__()
        self.window = window
        self.widget = MyQwidget()
        self.widget.setObjectName("customwidget" + str(self.count))
        self.count += 1
        self.widget.setStyleSheet("#"+str(self.widget.objectName())+"{border-bottom: 1px solid black;}")
        self.task = task
        self.mode = mode
        self.checkBox = QCheckBox()
        self.titleLabel = QLabel()
        self.time = QLabel()
        self.state = QLabel()
        self.taskType = QLabel()
        self.layout_main = QHBoxLayout()
        if mode == 0:
            self.titleLabel.setText(task.taskName)
            timeshow = minutes2ShowTime(task.sc_startTime)
            timeshow += " - " + minutes2ShowTime(task.sc_endTime)
            self.time.setText(timeshow)
            now = int(datetime.today().hour)*60+ int(datetime.today().minute)
            if firstItem and task.sc_startTime <= now:
                self.state.setText("正在进行")
            else :
                self.state.setText(" 未开始")
            self.taskType.setText(task.taskType)
            self.layout_main.addWidget(self.checkBox)
            self.layout_main.addWidget(self.titleLabel)
            self.layout_main.addWidget(self.time)
            self.layout_main.addWidget(self.state)
            self.layout_main.addWidget(self.taskType)
            self.layout_main.setStretch(1, 2)#(index, value)
        elif mode == 1:#finished
            if firstItem:
                self.widget.setStyleSheet("border-bottom:1px solid grey;")
                self.tipLabel = QLabel("已完成任务")
                self.layout_main.addWidget(self.tipLabel)
            else :
                self.widget.setStyleSheet("color:grey")
                self.titleLabel.setText(task.taskName)
                self.checkBox.setChecked(True)
                self.state.setText("已完成")
                self.taskType.setText(task.taskType)
                self.layout_main.addWidget(self.checkBox)
                self.layout_main.addWidget(self.titleLabel)
                self.layout_main.addWidget(self.state)
                self.layout_main.addWidget(self.taskType)
                self.layout_main.setStretch(1, 2)#(index, value)
        elif mode == 2 :#overtime
            if firstItem:
                self.widget.setStyleSheet("border-bottom:1px solid grey;")
                self.tipLabel = QLabel("已过期任务")
                self.layout_main.addWidget(self.tipLabel)
            else:
                #self.widget.setStyleSheet("color:red;")
                #self.widget.setStyleSheet("text-decoration:line-through;")
                self.titleLabel.setText(task.taskName)
                self.timetip = QLabel("截止时间: ")
                self.time.setText(task.deadline.split(" ")[1])
                self.state.setText("已过期")
                self.taskType.setText(task.taskType)
                self.timetip.setStyleSheet("color:red;")
                self.time.setStyleSheet("color:red;")
                self.state.setStyleSheet("color:red;")
                self.taskType.setStyleSheet("color:red;")
                self.layout_main.addWidget(self.checkBox)
                self.layout_main.addWidget(self.titleLabel)
                self.layout_main.addWidget(self.timetip)
                self.layout_main.addWidget(self.time)
                self.layout_main.addWidget(self.state)
                self.layout_main.addWidget(self.taskType)
                self.layout_main.setStretch(1, 2)
        self.widget.setLayout(self.layout_main)
        self.setSizeHint(self.widget.sizeHint())
        if mode != 0 and firstItem == True:
            return
        self.widget.clicked.connect(self.showSideBar)
        self.checkBox.stateChanged.connect(self.changeState)
    # @staticmethod
    # def restore():
    #     CustomListWidgetItem.needFirstItem = True
    #
    # def cached_select(self, task:Mytask, mode):
    #     if task is None:
    #         return mode
    #     if mode == 1:
    #         return 1
    #     tmp = str(datetime.now().time()).split(":")
    #     time = int(tmp[0]) * 60 + int(tmp[1])
    #     if task.sc_endTime <= time:
    #         return 2
    #     else:
    #         return 0

    def changeState(self):
        if self.checkBox.isChecked():#以前可能是过期或者未开始或者正在进行
            #任务完成的唯一通道，指今日任务的完成
            self.task.setFinished(mode=self.mode)
            self.window.updateListWidget()
        else : #已完成的任务变成原来的，暂不实现，有些复杂
            pass

    def showSideBar(self):
        self.window.showSider(self.task)

def minutes2ShowTime(minutes):
    """将分钟数转化为 时:分
    """
    hour = str(int(minutes // 60))
    minutes = int(minutes % 60)
    if minutes < 10:
        minutes = "0" + str(minutes)
    else :
        minutes = str(minutes)
    return  hour + ":" + minutes

if __name__ == "__main__":
    print(minutes2ShowTime(60))