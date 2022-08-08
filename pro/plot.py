from dataSee import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtCore import QTimer
import sys, time
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.cbook as cbook

from test import Init
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import matplotlib.dates as mdate
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

DAYS = 7 #过去7天
max_work_time = 12 #设定最长工作时间为12小时

class ImgDisp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImgDisp, self).__init__(parent)
        self.setupUi(self)
        self.Init_Widgets()

    def Init_Widgets(self):
        self.PrepareSamples()
        self.PrepareLineCanvas()
        # self.PrepareBarCanvas()
        self.PrepareImgCanvas()
        self.PrepareSurfaceCanvas()

    def PrepareSamples(self): #准备一些数据
        self.x = np.arange(-4, 4, 0.02) #从-4到4隔0.02一个坐标
        self.y = np.arange(-4, 4, 0.02)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.z = np.sin(self.x)
        self.R = np.sqrt(self.X ** 2 + self.Y ** 2)
        self.Z = np.sin(self.R)

    def PrepareLineCanvas(self): #先实例一个我们刚才定义的画板类
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.groupBox) #在相应的QGroupBox中添加一个栅格布局
        self.LineFigureLayout.addWidget(self.LineFigure) #将画板添加到布局
        # self.LineFigure.ax.set_xlim(-4, 4) #设置坐标轴的显示范围
        # self.LineFigure.ax.set_ylim(-1, 1)

        # self.line = Line2D(self.x, self.z)
        # self.LineFigure.ax.add_line(self.line)
        # self.LineFigure.ax.plot(self.x, self.z)
        xdate, ydata = Init()

        xlims = mdate.date2num([xdate[0], xdate[-1]])

        self.LineFigure.ax.plot(xdate, ydata, 'go-', label='日工作时间', linewidth=2)
        extent = [xlims[0], xlims[1], 0, max(ydata) + 1]
        _, yv = np.meshgrid(np.linspace(0, 1, 210), np.linspace(0, 1, 90))
        self.LineFigure.ax.imshow(yv, cmap=mpl.cm.Greens, origin='lower', alpha=0.5, aspect='auto',
                  extent=extent)

        self.LineFigure.ax.fill_between(xdate, ydata, max(ydata) + 1, color='white')

        self.LineFigure.ax.set_title("个人工作时间趋势", fontdict={'size': 16})
        self.LineFigure.ax.set_xlabel("日期", fontdict={'size': 16})
        self.LineFigure.ax.set_ylabel("时间（小时）", fontdict={'size': 16})
        # 去掉边框 top left right bottom
        self.LineFigure.ax.spines['top'].set_visible(False)
        self.LineFigure.ax.spines['left'].set_visible(False)
        self.LineFigure.ax.spines['right'].set_visible(False)
        # 设置 x 轴颜色
        self.LineFigure.ax.spines['bottom'].set_color('lightgray')
        self.LineFigure.ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
        self.LineFigure.ax.tick_params(left='off')
        self.LineFigure.ax.tick_params(which='major', direction='out', width=0.2, length=5)  # in, out or inout
        self.LineFigure.ax.grid(axis='y', color='lightgray', linestyle='-', linewidth=0.5)
        self.LineFigure.ax.legend(loc='best', fontsize=12, frameon=False, ncol=1)

    # def PrepareBarCanvas(self):
    #     self.BarFigure = Figure_Canvas()
    #     self.BarFigureLayout = QGridLayout(self.groupBox_2)
    #     self.BarFigureLayout.addWidget(self.BarFigure)
    #
    #     self.BarFigure.ax.set_xlim(-4, 4)
    #     self.BarFigure.ax.set_ylim(-1, 1)
    #     #np.arange(-4, 4, 0.5)定义了16个x坐标，np.sin(np.arange(-4, 4, 0.5))为对应的数据柱的高度，width=0.4定义数据柱的宽度
    #     self.bar = self.BarFigure.ax.bar(np.arange(-4, 4, 0.5), np.sin(np.arange(-4, 4, 0.5)), width=0.4)
    #     self.patches = self.bar.patches
    #     #需要注意的是，这里我们需要记录下bar函数的返回值，然后通过代码self.patches = self.bar.patches获取柱形图的patches
    #     #，用于对其数据进行更新。柱形图的patches是一个矩阵的列表，记录了组成柱形图的每一个矩形的参数。

    def PrepareImgCanvas(self):
        self.ImgFigure = Figure_Canvas()
        self.ImgFigureLayout = QGridLayout(self.groupBox_3)
        self.ImgFigureLayout.addWidget(self.ImgFigure)
        #使用imshow函数即可，同样地，我们也需要保留它的返回值，其中，cmap定义使用的colormap，set_clim函数定义显示的Z的大小范围。
        self.ImgFig = self.ImgFigure.ax.imshow(self.Z, cmap='bone')
        self.ImgFig.set_clim(-0.8, 0.8)

    def PrepareSurfaceCanvas(self):
        self.SurfFigure = Figure_Canvas()
        self.SurfFigureLayout = QGridLayout(self.groupBox_4)
        self.SurfFigureLayout.addWidget(self.SurfFigure)
        #对于三维图，我们需要重新定义一个三维的轴，因此需要先删除原来的轴
        self.SurfFigure.ax.remove()
        self.ax3d = self.SurfFigure.fig.gca(projection='3d')
        self.Surf = self.ax3d.plot_surface(self.X, self.Y, self.Z, cmap='rainbow')

class Figure_Canvas(FigureCanvas):
    def __init__(self,parent=None,width=3.9,height=2.7,dpi=100): #画板，单位是100像素
        self.fig=Figure(figsize=(width,height),dpi=100)
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111) #在轴上绘图


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ImgDisp()
    ui.show()
    sys.exit(app.exec_())