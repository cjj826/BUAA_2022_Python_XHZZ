from datetime import datetime
import functools

from mysql.MySql import MySql


class Mytask:
    def __init__(self, userName=None, taskName=None, content=None,
                 deadline=None, importance=None):
        self.userName = userName
        self.taskName = taskName
        self.content = content
        self.startline =
        self.deadline = deadline#总的deadline
        self.importance = importance
        self.isChanged = False
        self.oldtaskName = taskName
        self.oldcontent = content
        self.olddeadline = deadline
        self.oldimportance = importance

        self.startTime = None
        self.endTime = None
        self.runTime = None
        self.sc_startTime = None
        self.sc_endTime = None
    def updateTask(self, typeName, text):
        print(text)
        if typeName == "taskName":
            self.taskName = text
        elif typeName == "content":
            self.content = text
        elif typeName == "deadline":
            self.deadline = text
        elif typeName == "importance":
            self.importance = text
        self.isChanged = True

    def updateSql(self):
        print("updateHas")
        if self.isChanged:
            mysql = MySql()
            mysql.update("user_" + self.userName,
                         {"taskName": self.taskName, "content": self.content,
                          "deadline": self.deadline, "importance": self.importance},
                         {"taskName": self.oldtaskName, "content": self.oldcontent,
                          "deadline": self.olddeadline, "importance": self.oldimportance}
                         )
            mysql.closeDataBase()
            print(123123)

    def delete(self):
        mysql = MySql()
        if self.isChanged:
            mysql.delete("user_" + self.userName, {"taskName": self.oldtaskName, "content": self.oldcontent,
                                               "deadline": self.olddeadline, "importance": self.oldimportance})
        else:
            mysql.delete("user_" + self.userName, {"taskName": self.taskName, "content": self.content,
                                               "deadline": self.deadline, "importance": self.importance})
        mysql.closeDataBase()
        self.isChanged = False

    def getDeadline(self):
        return self.deadline

    def getTaskName(self):
        return self.taskName

    @staticmethod
    def getTasks(userName, isToday=True, isSort=True, isScheduled = False):
        mysql = MySql()
        results = mysql.select('user_' + userName, all=True)
        if results == ():
            return None
        print(results)
        tasks = []
        for a in results:
            if isToday:
                date = list(a[3].split(" "))[0]
                today = str(datetime.today())
                if date != today:
                    continue
            task = Mytask(userName=userName,
                          taskName=a[1], content=a[2],
                          deadline=a[3], importance=a[4])
            tasks.append(task)
        if len(tasks) == 0:
            return None
        if isToday and isSort:
            tasks.sort(key=functools.cmp_to_key(sortTaskInStartTime))
        if isScheduled:
            tasks = autoSchedule(tasks)
        print("get tasks:", end="")
        for task in tasks:
            print(task.taskName, end="")
        print()
        return tasks

    def save(self):
        """保存到数据库
        """
        mysql = MySql()
        dic = {'taskName': self.taskName, 'content': self.content,
               'deadline': self.deadline, 'importance': self.importance}
        mysql.insert('user_' + self.userName, dic)
        mysql.closeDataBase()

    @staticmethod
    def getAttr(columnNames=None):
        attrs = ["taskName", "content", "deadline", "importance"]
        dic = {}
        # 创建用户数据库时需要
        if columnNames is None:
            for a in attrs:
                dic[a] = "VARCHAR (255)"
            return dic

def runTime2freeTime(runTime, free_rate):
    return int(round(runTime/60))*10*free_rate

DAYTIME = 60 * 24
def autoSchedule(tasks):
    """实现自动调度
    前提条件：所有任务都没有结束或者过期，午休任务已经加进去了，所有任务开始时间在6点之后
    :param tasks: 今日task的list，task属性有startTime, endTime, runTime , importance
                   例如, task.startTime为开始的分钟数，为int类型
    :return: scheduled tasks
    """
    now = int(datetime.today().hour)*60+ int(datetime.today().minute)
    for free_rate in range(3, -1, -1):
        res = scheduleTask(tasks, free_rate)
        if res == False:
            continue
    if res == False:
        print("schedule failed")
    return res

def scheduleTask(tasks, free_rate):
    canBeginTasks = []#可以开始的任务，按绝对截止时间排序
    scheduledTasks = []#已经被调度的任务
    startTime = tasks[0].startTime
    beginIndex = 0
    while beginIndex < len(tasks):
        for i in range(beginIndex, len(tasks)):
            if tasks[i].startTime <= startTime:
                canBeginTasks.append(tasks[i])
            else:
                beginIndex = i
                break
        else :
            beginIndex = len(tasks)
        canBeginTasks.sort(key=functools.cmp_to_key(sortTaskInEndTime))
        nowTask = canBeginTasks.pop(0)
        nowTask.sc_startTime = startTime
        nowTask.sc_endTime = nowTask.sc_startTime + nowTask.runTime
        nowTask.sc_freeEndTime = runTime2freeTime(nowTask.runTime, free_rate) + nowTask.sc_endTime
        if nowTask.sc_freeEndTime > nowTask.endTime and free_rate != 0:
            return False
        scheduledTasks.append(nowTask)
        startTime = nowTask.sc_freeEndTime
    lens = len(canBeginTasks)
    for i in range(lens):
        nowTask = canBeginTasks.pop(0)
        nowTask.sc_startTime = startTime
        nowTask.sc_endTime = nowTask.sc_startTime + nowTask.runTime
        nowTask.sc_freeEndTime = runTime2freeTime(nowTask.runTime, free_rate) + nowTask.sc_endTime
        if nowTask.sc_freeEndTime > nowTask.endTime and free_rate != 0:
            return False
        scheduledTasks.append(nowTask)
        startTime = nowTask.sc_freeEndTime
    return scheduledTasks

def sortTaskInEndTime(self, other):
    selfTime = self.endTime - self.startTime
    otherTime = other.endTime - other.startTime
    if selfTime > otherTime:
        return 1
    elif selfTime < otherTime:
        return -1
    else:
        if self.importance == '重要':
            return -1
        else:
            return 1

def sortTaskInDeadline(self, other):
    selfTime = self.deadline.split(" ")[1]
    otherTime = other.deadline.split(" ")[1]
    if selfTime > otherTime:
        return 1
    elif selfTime < otherTime:
        return -1
    else:
        if self.importance == '重要':
            return -1
        else:
            return 1

def sortTaskInStartTime(self, other):
    selfTime = self.startTime
    otherTime = other.startTime
    if selfTime > otherTime:
        return 1
    elif selfTime  < otherTime:
        return -1
    else :
        if self.importance == '重要':
            return -1
        else :
            return 1

if __name__ == "__main__":
    for i in range(10, -1, -1):
        print(i)
