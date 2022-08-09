from PyQt5.QtCore import QTimer, QDateTime


import sys
import re
import DateTime
import untitled
from MainWindow.customItem import CustomListWidgetItem
from MyCalendar import MyCalendar
from addDialog import AddDialog
from mytask import Mytask

DAYS = 7 #过去7天
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtCore import QTimer
import sys, time

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import matplotlib.dates as mdate
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None,width=3.9,height=2.7,dpi=100): #画板，单位是100像素
        self.fig = Figure(figsize=(width,height),dpi=100)
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111) #在轴上绘图

class masterWindow(untitled.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(masterWindow, self).__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        #进行信号与槽的链接按钮
        self.pushButton.clicked.connect(self.display_page1)
        self.pushButton_2.clicked.connect(self.display_page2)
        self.pushButton_3.clicked.connect(self.display_page3)
        self.pushButton_4.clicked.connect(self.display_page4)
        # self.pushButton_5.clicked.connect(self.display_page5)
        self.label_11.setText("2022-07-30 16:55:40 星期日")
        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)  # 这个通过调用槽函数来刷新时间
        self.timer.start(1000)  # 每隔一秒刷新一次，这里设置为1000ms
        self.lineEdit.setPlaceholderText("添加任务，按回车创建")
        self.lineEdit.returnPressed.connect(self.addAssignment)

        #设计侧边栏，侧边栏应该是mainWindow的一个属性，尝试对象是widget
        # self.button = QPushButton("Start", self)
        # self.button.clicked.connect(self.showSider)
        # self.button.move(0, 800)

        self.pushButton_10.clicked.connect(self.hideSider)
        self.pushButton_11.clicked.connect(self.deleteTask)
        #侧边栏
        self.start.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.end.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.start.setCalendarPopup(True)
        self.end.setCalendarPopup(True)

        self.widget.hide()
        self.title.editingFinished.connect(self.update_taskName)
        self.type.currentIndexChanged.connect(self.update_taskType)
        self.start.dateTimeChanged.connect(self.update_taskStartLine)
        self.end.dateTimeChanged.connect(self.update_taskDeadline)
        self.time.dateTimeChanged.connect(self.update_taskDeadline)#not sure
        self.importance.currentIndexChanged.connect(self.update_taskImportance)#update importance
        self.content.textChanged.connect(self.update_taskContent) #content
        self.showingTask = None

    def update_taskName(self):
        self.showingTask.updateTask("taskName", self.title.text())
    def update_taskType(self):
        self.showingTask.updateTask("taskType", self.type.currentText())

    def update_taskStartLine(self):
        self.showingTask.updateTask("startline", self.start.dateTime().toString("yyyy-MM-dd HH:mm"))

    def update_taskDuration(self):
        t = self.time.dateTime().time()
        t = t.hour() * 60 + t.minute()
        self.showingTask.updateTask("duration", t)

    def update_taskContent(self):
        self.showingTask.updateTask("content", self.content.toPlainText())

    def update_taskDeadline(self):
        self.showingTask.updateTask("deadline", self.end.dateTime().toString("yyyy-MM-dd HH:mm"))

    def update_taskImportance(self):
        self.showingTask.updateTask("importance", self.importance.currentText())


    def showSider(self, task:Mytask):
        """展示侧边栏
        """
        self.showingTask = task
        self.widget.show()
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.title.setText(task.taskName)

        self.type.setCurrentText(task.taskType)
        self.start.setDateTime(datetime.datetime.strptime(task.startline, "%Y-%m-%d %H:%M"))
        self.end.setDateTime(datetime.datetime.strptime(task.deadline, "%Y-%m-%d %H:%M"))
        hour = task.duration / 60
        minute = task.duration % 60
        self.time.setDateTime(QDateTime(1,1,1, hour, minute))
        self.importance.setCurrentText(task.importance)
        self.content.setPlainText(task.content)

    def deleteTask(self):
        """通过侧边栏删除任务；删除按钮的slot函数
        """
        # self.lineEdit_2.clear()
        # self.textEdit_2.clear()
        # self.textEdit_3.clear()
        # self.textEdit_4.clear()
        self.showingTask.delete()
        self.showingTask = None
        self.hideSider()

    def hideSider(self):
        """隐藏侧边栏
        """
        self.widget.hide()
        if self.showingTask is not None:
            self.showingTask.updateSql()
        self.updateListWidget()


    def addCalendar(self):
        self.calendar = MyCalendar(self.userName)
        self.calendarVerticalLayout.addWidget(self.calendar)
        # self.calendarVerticalLayout.addWidget(MyCalendar(self.userName))
        self.calendar.show()

    def addAssignment(self):
        """创建任务
        """
        self.INPUT = AddDialog()#新建一个对话框窗口，新建任务
        self.INPUT.setTitleAuto(self.lineEdit.text())
        self.INPUT.setUserName(self.userName)
        self.INPUT.exec_()

        if self.INPUT.set == True:
            l = [self.INPUT.title.text(), self.INPUT.type.currentText(),
                 self.INPUT.start.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                 self.INPUT.time.time().toString("HH:mm"),
                 self.INPUT.content.toPlainText(),self.INPUT.importance.currentText()]
            print(l)
            self.updateListWidget()

    def showtime(self):
        time=QDateTime.currentDateTime()#获取当前时间
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下时间
        self.label_11.setText(timedisplay)

    def display_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_page3(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_page4(self):
        self.stackedWidget.setCurrentIndex(3)
        self.printLine()
        self.printCircle()
        self.printBar()

    def display_page5(self):
        self.stackedWidget.setCurrentIndex(4)

    def setUser(self, username):
        self.userName = username
        print(self.userName)
        self.updateListWidget()

    def updateListWidget(self):
        tasksNeed, tasksFinished, tasksOvertime = Mytask.getTasks(self.userName)#只会获取到今日任务
        print("hhh")
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.takeItem(0)
            del item

        for i, task in enumerate(tasksNeed):
            if i == 0:
                item = CustomListWidgetItem(task, self, mode=0, firstItem=True)
            else :
                item = CustomListWidgetItem(task, self, mode=0, firstItem=False)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,item.widget)

        if len(tasksFinished) != 0:
            item = CustomListWidgetItem(None, self, mode=1, firstItem=True)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)
        for task in tasksFinished:
            item = CustomListWidgetItem(task, self, mode=1)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)

        if len(tasksOvertime) != 0:
            item = CustomListWidgetItem(None, self, mode=2, firstItem=True)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)
        for task in tasksOvertime:
            item = CustomListWidgetItem(task, self, mode=2)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)

    #历史数据分析，任务类别
    def getData3(self):
        tasks = Mytask.getTasksForDate(self.userName, timeSpan)
        dic = {"运动":0, "学习":0, "娱乐":0, "生活":0}
        for task in tasks:
            #一个任务的开始时间在foredate之后，在nowdate之前，即算进来
                dic[task.taskType] += 1
        num = [dic["运动"], dic["学习"], dic["娱乐"], dic["生活"]]
        return num

    def printBar(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox_3)  # 在相应的QGroupBox中添加一个栅格布局
        self.LineFigureLayout.addWidget(self.LineFigure)  # 将画板添加到布局

        num_list = self.getData3()

        self.LineFigure.ax.set_title("任务类别统计")
        self.LineFigure.ax.barh(range(len(num_list)), num_list, tick_label = ['运动','学习','娱乐','生活'], color=['red', 'green', 'blue', 'purple'])

    def getData2(self):
        tasks = Mytask.getTasksForDate(self.userName, timeSpan)
        dic = {"已完成":0, "未完成":0}
        for task in tasks:
            if task.duration <= 0:
                dic["已完成"] += 1
            else :
                dic["未完成"] += 1
        data = np.array([dic["已完成"], dic["未完成"]])
        return data

    def printCircle(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox_2)  # 在相应的QGroupBox中添加一个栅格布局
        self.LineFigureLayout.addWidget(self.LineFigure)  # 将画板添加到布局

        ydata = self.getData2()
        self.LineFigure.ax.pie(ydata, labels=['已完成','未完成'],
                               colors=["#65a479", "#d5695d"],  # 设置饼图颜色
                                explode=(0, 0.1), # 第二部分突出显示，值越大，距离中心越远
                                autopct='%.2f%%', # 格式化输出百分比
                               )
        self.LineFigure.ax.set_title("任务完成情况", fontdict={'size': 16})

    def getData1(self):
        timedelta = datetime.timedelta(days=1)
        today = datetime.datetime.today()
        startdate = today - 7 * timedelta #过去一周，不包括今天
        xdate = [startdate + i * timedelta for i in range(DAYS)]
        tasks = Mytask.getTasksForDate(self.userName, timeSpan)
        ydata = [0 for i in range(timeSpan)]
        for task in tasks:
            deadline = task.deadline.split(" ")[0]
            deaddate = datetime.datetime.strptime(deadline, "%Y-%m-%d")
            day = (today - deaddate).days
            if day < 0:
                continue
            ydata[timeSpan - day - 1] += 1
        return xdate, ydata

    def printLine(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox)  # 在相应的QGroupBox中添加一个栅格布局
        self.LineFigureLayout.addWidget(self.LineFigure)  # 将画板添加到布局

        xdate, ydata = self.getData1()

        xlims = mdate.date2num([xdate[0], xdate[-1]])

        self.LineFigure.ax.plot(xdate, ydata, 'go-', label='日工作量', linewidth=2)
        extent = [xlims[0], xlims[1], 0, max(ydata) + 1]
        _, yv = np.meshgrid(np.linspace(0, 1, 210), np.linspace(0, 1, 90))
        self.LineFigure.ax.imshow(yv, cmap=mpl.cm.Greens, origin='lower', alpha=0.5, aspect='auto',
                                  extent=extent)
        self.LineFigure.ax.fill_between(xdate, ydata, max(ydata) + 1, color='white')
        self.LineFigure.ax.set_title("个人工作量趋势", fontdict={'size': 16})
        # self.LineFigure.ax.set_xlabel("日期", fontdict={'size': 12})
        self.LineFigure.ax.set_ylabel("任务数（个）", fontdict={'size': 12})

        self.LineFigure.ax.spines['top'].set_visible(False)
        self.LineFigure.ax.spines['left'].set_visible(False)
        self.LineFigure.ax.spines['right'].set_visible(False)

        self.LineFigure.ax.spines['bottom'].set_color('lightgray')
        self.LineFigure.ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
        self.LineFigure.ax.tick_params(left='off')
        self.LineFigure.ax.tick_params(which='major', direction='out', width=0.2, length=5)  # in, out or inout
        self.LineFigure.ax.grid(axis='y', color='lightgray', linestyle='-', linewidth=0.5)
        self.LineFigure.ax.legend(loc='best', fontsize=12, frameon=False, ncol=1)


timeSpan = 7
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = masterWindow()
    main_window.setUser("18839173859")
    main_window.show()
    sys.exit(app.exec_())
