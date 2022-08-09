from datetime import datetime
from datetime import timedelta
import functools

from mysql.MySql import MySql


class Mytask:
    reserve_freeTime = 0
    def __init__(self, userName, taskName, taskType, startline:str,
                 deadline:str, duration:int, importance, content, id = None, finishToday = "False"):
        #创建任务时指定
        self.userName = userName
        self.taskName = taskName
        self.content = content
        self.startline = startline
        self.deadline = deadline#总的deadline
        self.duration =  duration#总的用时，总分钟数， 可以改变，根据今日是否完成
        self.taskType = taskType
        self.importance = importance
        self.id = id
        #用于修改任务
        #self.isChanged = False
        # self.oldtaskName = taskName
        # self.oldcontent = content
        # self.olddeadline = deadline
        # self.oldimportance = importance
        #任务调度所用
        self.startTime = None
        self.endTime = None
        self.runTime = None
        self.sc_startTime = None
        self.sc_endTime = None
        self.sc_freeEndTime = None

        #任务是否过期、完成
        #任务是否总的完成了， 看duration是否为0即可
        self.finishToday = finishToday#今天的任务是否完成

    #任务完成
    def setFinished(self, mode = 0):#0为正常，2为过期完成（多天任务不会过期）
        if mode == 0:
            #当天任务
            if self.deadline.split(" ")[0] == str(datetime.now().strftime("%Y-%m-%d")):
                self.duration = 0
                print("duration is 0")
            else :#多天任务
                self.duration = self.duration - (self.sc_endTime - self.sc_startTime)
                if self.duration < 0:
                    self.duration = 0
                self.finishToday = str(datetime.now().date())
            self.reserve_freeTime = self.sc_freeEndTime - self.sc_endTime
        else :
            self.duration = 0
        self.updateSql()

    def updateTask(self, typeName, text):
        if typeName == "taskName":
            self.taskName = text
        elif typeName == "taskType":
            self.taskType = text
        elif typeName == "startline":
            self.startline = text
        elif typeName == "duration":
            self.duration = text
        elif typeName == "content":
            self.content = text
        elif typeName == "deadline":
            self.deadline = text
        elif typeName == "importance":
            self.importance = text

    def updateSql(self):
        print("updateHas")
        mysql = MySql()
        dic = {'taskName': self.taskName, 'content': self.content, 'startline': self.startline,
               'deadline': self.deadline, 'duration': str(int(self.duration)), 'taskType': self.taskType,
               'importance': self.importance, 'finishToday': self.finishToday}
        mysql.update("user_" + self.userName, dic, {"id" : self.id})
        mysql.closeDataBase()

    def delete(self):
        mysql = MySql()
        mysql.delete("user_" + self.userName, {"id": self.id})
        mysql.closeDataBase()

    def getDeadline(self):
        return self.deadline

    def getTaskName(self):
        return self.taskName

    @staticmethod
    def getTasksForDate(userName, timeSpan = None):
        """
        获取所有任务

        :param timeSpan: 时间期限，获取今日到今日之前多少天的数据
        """
        mysql = MySql()
        results = mysql.select('user_' + userName, all=True)
        mysql.closeDataBase()
        if results == ():
            return None
        tasks = []
        if timeSpan is not None:
            nowdate = datetime.now().date()
            delta = timedelta(days=timeSpan)
            foredate = nowdate - delta
        for line in results:
            if timeSpan is not None:
                start = line[3].split(" ")[0]
                if not (start > str(foredate) and start <= str(nowdate)):
                    continue
            task = Mytask(userName=userName, taskName=line[1],
                          taskType=line[6], startline=line[3], deadline=line[4],
                          duration=int(line[5]), importance=line[7], content=line[2],
                          id=line[0], finishToday=line[8])
            tasks.append(task)
        return tasks

    @staticmethod
    def getAllTasks(userName, dateText):
        mysql = MySql()
        results = mysql.select('user_' + userName, all=True)
        mysql.closeDataBase()
        tasksNeed = []
        tasksOvertime = []
        tasksFinished = []
        if results == ():
            return tasksNeed, tasksFinished, tasksOvertime
        print("getResults:", results)
        # 获取任务
        for line in results:
            start = list(line[3].split(" "))
            ddl = list(line[4].split(" "))  # a task ddl, [0] is date, [1] is time
            today = dateText
            time = "00:00"
            if ddl[0] == today or (start[0] <= today and ddl[0] > today):
                task = Mytask(userName=userName, taskName=line[1],
                              taskType=line[6], startline=line[3], deadline=line[4],
                              duration=int(line[5]), importance=line[7], content=line[2],
                              id=line[0], finishToday=line[8])
                if task.finishToday == today or task.duration == 0:
                    tasksFinished.append(task)
                elif ddl[0] <= today and ddl[1] <= time:
                    tasksOvertime.append(task)
                else:
                    print("tasksNeed append")
                    tasksNeed.append(task)
        # 添加任务调度参数
        today = str(datetime.now().date())
        tmpStart = today + " 11:30"
        tmpEnd = today + " 2:00"
        tmp = Mytask(userName, "午休tmp", "娱乐", tmpStart, tmpEnd, 60, "不重要", None, id=-1)
        tasksNeed.append(tmp)
        for task in tasksNeed:
            # 任务的开始时间，start[0]为日期，start[1]为时刻
            start = list(task.startline.split(" "))
            ddl = list(task.deadline.split(" "))
            start_time = list(map(int, start[1].split(":")))
            ddl_time = list(map(int, ddl[1].split(":")))
            # startTime为任务的可以开始时间，endTime为可以结束时间
            if start[0] != today:
                task.startTime = 6 * 60
            else:
                task.startTime = start_time[0] * 60 + start_time[1]
            if ddl[0] == today:
                task.endTime = ddl_time[0] * 60 + ddl_time[1]
                task.runTime = task.duration
            else:  # 跨度多天的任务
                ddlDate = datetime.strptime(ddl[0], "%Y-%m-%d").date()
                nowDate = datetime.now().date()
                days = (ddlDate - nowDate).days + 1
                task.runTime = task.duration // days
                task.endTime = ENDOFDAY
        tasksNeed.sort(key=functools.cmp_to_key(sortTaskInStartTime))
        # tasksFinished.sort(key=functools.cmp_to_key(sortTaskInDeadline))
        tasksOvertime.sort(key=functools.cmp_to_key(sortTaskInDeadline))
        if len(tasksNeed) != 0:
            tasksNeed = autoSchedule(tasksNeed)
        tasksNeed.remove(tmp)
        print("get tasks:", end="")
        for task in tasksNeed:
            print(task.taskName, end="")
        print()
        return tasksNeed, tasksFinished, tasksOvertime


    @staticmethod
    def getTasks(userName):
        mysql = MySql()
        results = mysql.select('user_' + userName, all=True)
        mysql.closeDataBase()
        tasksNeed = []
        tasksOvertime = []
        tasksFinished = []
        if results == ():
            return tasksNeed, tasksFinished, tasksOvertime
        print("getResults:", results)
        #获取任务
        for line in results:
            start = list(line[3].split(" "))
            ddl = list(line[4].split(" "))#a task ddl, [0] is date, [1] is time
            today = str(datetime.now().strftime("%Y-%m-%d"))
            time = str(datetime.now().strftime("%H:%M"))
            if ddl[0] == today or (start[0] <= today and ddl[0] > today):
                task = Mytask(userName=userName, taskName=line[1],
                              taskType=line[6], startline=line[3], deadline=line[4],
                              duration=int(line[5]), importance=line[7], content=line[2],
                              id = line[0], finishToday = line[8])
                if task.finishToday == today or task.duration == 0:
                    tasksFinished.append(task)
                elif ddl[0] <= today and ddl[1] <= time :
                    tasksOvertime.append(task)
                else :
                    print("tasksNeed append")
                    tasksNeed.append(task)
        #添加任务调度参数
        today = str(datetime.now().date())
        tmpStart = today + " 11:30"
        tmpEnd = today + " 2:00"
        tmp = Mytask(userName, "午休tmp", "娱乐", tmpStart, tmpEnd, 60, "不重要", None, id = -1)
        tasksNeed.append(tmp)
        for task in tasksNeed:
            #任务的开始时间，start[0]为日期，start[1]为时刻
            start = list(task.startline.split(" "))
            ddl = list(task.deadline.split(" "))
            start_time = list(map(int, start[1].split(":")))
            ddl_time = list(map(int, ddl[1].split(":")))
            #startTime为任务的可以开始时间，endTime为可以结束时间
            if start[0] != today:
                task.startTime = 6 * 60
            else:
                task.startTime = start_time[0] * 60 + start_time[1]
            if ddl[0] == today:
                task.endTime = ddl_time[0]*60 + ddl_time[1]
                task.runTime = task.duration
            else :#跨度多天的任务
                ddlDate = datetime.strptime(ddl[0], "%Y-%m-%d").date()
                nowDate = datetime.now().date()
                days = (ddlDate - nowDate).days + 1
                task.runTime = task.duration // days
                task.endTime = ENDOFDAY
        tasksNeed.sort(key=functools.cmp_to_key(sortTaskInStartTime))
        #tasksFinished.sort(key=functools.cmp_to_key(sortTaskInDeadline))
        tasksOvertime.sort(key=functools.cmp_to_key(sortTaskInDeadline))
        if len(tasksNeed) != 0:
            tasksNeed = autoSchedule(tasksNeed)
        tasksNeed.remove(tmp)
        print("get tasks:", end="")
        for task in tasksNeed:
            print(task.taskName, end="")
        print()
        return tasksNeed, tasksFinished, tasksOvertime

    def save(self):
        """将任务保存到数据库
        """
        mysql = MySql()
        dic = {'taskName': self.taskName, 'content': self.content, 'startline':self.startline,
               'deadline': self.deadline, 'duration':str(int(self.duration)), 'taskType':self.taskType,
               'importance': self.importance, 'finishToday':self.finishToday}
        mysql.insert('user_' + self.userName, dic)
        mysql.closeDataBase()

    @staticmethod
    def getAttr(columnNames=None):
        attrs = ["taskName", "content", "startline","deadline", "duration", "taskType", "importance", "finishToday"]
        dic = {}
        # 创建用户数据库时需要
        if columnNames is None:
            for a in attrs:
                dic[a] = "VARCHAR (255)"
            return dic

def runTime2freeTime(runTime, free_rate):
    print(runTime)
    print("freeTime", int(round(runTime/60))*10*free_rate)
    return int(round(runTime/60))*10*free_rate


def autoSchedule(tasks):
    """实现自动调度
    前提条件：所有任务都没有结束或者过期，午休任务已经加进去了，所有任务开始时间在6点之后
    :param tasks: 今日task的list，task属性有startTime, endTime, runTime , importance
                   例如, task.startTime为开始的分钟数，为int类型
    :return: scheduled tasks
    """
    res = False
    for free_rate in range(MAX_FREE_RATE, -1, -1):
        res = scheduleTask(tasks, free_rate)
        if res == False:
            continue
        else :
            break
    if res == False:
        print("schedule failed")
    return res

def scheduleTask(tasks, free_rate):
    nowTime = datetime.today().hour * 60+ datetime.today().minute
    canBeginTasks = []#可以开始的任务，按绝对截止时间排序
    scheduledTasks = []#已经被调度的任务
    beginIndex = 0
    startTime = tasks[0].startTime + Mytask.reserve_freeTime
    print("len is", len(tasks))
    while beginIndex < len(tasks):
        startTime = max(startTime, tasks[beginIndex].startTime)
        #寻找可以开始的任务，之前找过的任务不再去找，任务已经按startTime排序了
        for i in range(beginIndex, len(tasks)):
            if tasks[i].startTime <= startTime:
                print("i is", i)
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
        if nowTask.sc_endTime > nowTask.endTime:
            if free_rate != 0 and nowTask.id != -1:#id为-1则为午睡，午睡不要影响调度
                return False
            else :
                #如果实在不满足，则调度截止时间仍未结束时间
                nowTask.sc_endTime = nowTask.endTime
                nowTask.sc_freeEndTime = nowTask.endTime
        scheduledTasks.append(nowTask)
        startTime = nowTask.sc_freeEndTime
    lens = len(canBeginTasks)
    for i in range(lens):
        nowTask = canBeginTasks.pop(0)
        nowTask.sc_startTime = startTime
        nowTask.sc_endTime = nowTask.sc_startTime + nowTask.runTime
        nowTask.sc_freeEndTime = runTime2freeTime(nowTask.runTime, free_rate) + nowTask.sc_endTime
        if nowTask.sc_endTime > nowTask.endTime:
            if free_rate != 0 and nowTask.id != -1:
                return False
            else :
                nowTask.sc_endTime = nowTask.endTime
                nowTask.sc_freeEndTime = nowTask.endTime
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
MAX_FREE_RATE = 3
ENDOFDAY = 60 * 23 + 59#23:59
if __name__ == "__main__":
    task = Mytask("1234", "123", "运动", "2022-8-8 11:20", "2022-8-10 13:20",
                  840, "重要","123", id=1)

    task.setFinished(mode=0)
