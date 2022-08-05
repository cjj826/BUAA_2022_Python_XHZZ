import datetime
import functools

from mysql.MySql import MySql


class Mytask:
    def __init__(self, userName=None, taskName=None, content=None,
                 deadline=None, importance=None):
        self.userName = userName
        self.taskName = taskName
        self.content = content
        self.deadline = deadline
        self.importance = importance
        self.isChanged = False
        self.oldtaskName = taskName
        self.oldcontent = content
        self.olddeadline = deadline
        self.oldimportance = importance

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
    def getTasks(userName, isToday=True, isSort=True):
        mysql = MySql()
        results = mysql.select('user_' + userName, all=True)
        if results == ():
            return None
        print(results)
        tasks = []
        for a in results:
            if isToday:
                date = list(a[3].split(" "))[0]
                today = str(datetime.date.today())
                if date != today:
                    continue
            task = Mytask(userName=userName,
                          taskName=a[1], content=a[2],
                          deadline=a[3], importance=a[4])
            tasks.append(task)
        if isToday and isSort:
            tasks.sort(key=functools.cmp_to_key(sortTaskInTime))

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


def sortTaskInTime(self, other):
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


if __name__ == "__main__":
    Mytask.getTasks("123")
