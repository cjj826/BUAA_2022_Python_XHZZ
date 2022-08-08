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

name_list = ['运动','学习','娱乐','生活']
num_list = [1.5,10.0,7.8,6]
color = ['red', 'green', 'blue', 'purple']
plt.barh(range(len(num_list)), num_list, tick_label = name_list, color=color)
plt.show()

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
