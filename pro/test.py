# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

import matplotlib.pyplot as plt
import numpy as np

# y = np.array([35, 25, 25, 15])
#
# plt.pie(y,
#         labels=['未开始','正在进行','已完成','过期'], # 设置饼图标签
#         colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
#         explode=(0, 0, 0, 0.1), # 第二部分突出显示，值越大，距离中心越远
#         autopct='%.2f%%', # 格式化输出百分比
#        )
# plt.title("任务完成情况")
# plt.show()

# name_list = ['运动','学习','娱乐','生活']
# num_list = [1.5,10.0,7.8,6]
# color = ['red', 'green', 'blue', 'purple']
# plt.barh(range(len(num_list)), num_list, tick_label = name_list, color=color)
# plt.show()

# plt.figure(figsize=(20, 10), dpi=100)
# game = ["8-1", "8-2", "8-3", "8-4", "8-5", "8-6", "8-7"]
# scores = [7, 5, 6, 4, 8, 10, 5]
# plt.plot(game, scores, c='blue')
# plt.scatter(game, scores, c='blue', marker="*")
# y_ticks = range(12)
# plt.yticks(y_ticks[::2])
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.xlabel("日期", fontdict={'size': 16})
# plt.ylabel("工作时间", fontdict={'size': 16})
# plt.title("个人日工作时间变化趋势", fontdict={'size': 20})
# for a, b in zip(game, scores):
#     plt.text(a, b, b, ha = "center", va = "bottom", fontsize="16", color="green")
# plt.show()

# plt.figure(figsize=(20, 10), dpi=100)
# game = ["8-1", "8-2", "8-3", "8-4", "8-5", "8-6", "8-7"]
# scores = [2, 4, 5, 6, 2, 4, 3]
# plt.plot(game, scores, c='blue')
# plt.scatter(game, scores, c='blue', marker=".")
# y_ticks = range(12)
# plt.yticks(y_ticks[::2])
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.xlabel("日期", fontdict={'size': 16})
# plt.ylabel("工作时间", fontdict={'size': 16})
# plt.title("个人日工作量变化趋势", fontdict={'size': 20})
# for a, b in zip(game, scores):
#     plt.text(a, b, b, ha = "center", va = "bottom", fontsize="16", color="green")
# plt.show()

import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import matplotlib.dates as mdate
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

DAYS = 7 #过去7天
max_work_time = 12 #设定最长工作时间为12小时
import time

def Init(): #构造数据，x/y坐标
    timedelta = datetime.timedelta(days=1)
    startdate = datetime.date.today() - 7 * timedelta
    xdate = [startdate + i * timedelta for i in range(DAYS)]
    ydata = [7, 5, 6, 4, 8, 10, 5]
    return xdate, ydata

xdate, ydata = Init()

xlims = mdate.date2num([xdate[0], xdate[-1]])

_, yv = np.meshgrid(np.linspace(0, 1, 210), np.linspace(0, 1, 90))
fig, ax = plt.subplots(figsize=(21, 9))
ax.plot(xdate, ydata, 'go-', label='日工作时间', linewidth=2)
extent = [xlims[0], xlims[1], 0, max_work_time]
ax.imshow(yv, cmap=mpl.cm.Greens, origin='lower', alpha=0.5, aspect='auto',
          extent=extent)

ax.fill_between(xdate, ydata, max_work_time, color='white')

plt.yticks(color='gray')
plt.xticks(color='gray', rotation=15)

plt.title("个人工作时间趋势", fontdict={'size': 16})
plt.xlabel("日期", fontdict={'size': 16})
plt.ylabel("时间（小时）", fontdict={'size': 16})
# 去掉边框 top left right bottom
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
# 设置 x 轴颜色
ax.spines['bottom'].set_color('lightgray')
# 设置时间标签显示格式
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.tick_params(left='off')
plt.tick_params(which='major', direction='out', width=0.2, length=5)  # in, out or inout
plt.grid(axis='y', color='lightgray', linestyle='-', linewidth=0.5)
plt.legend(loc='best', fontsize=12, frameon=False, ncol=1)
plt.show()
