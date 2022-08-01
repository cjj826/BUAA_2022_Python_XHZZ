from mysql.MySql import MySql


class Mytask:
    def __init__(self, userName, taskName, content, deadline, importance):
        self.userName = userName
        self.taskName = taskName
        self.content = content
        self.deadline = deadline
        self.importance = importance

    """
        保存到数据库
    """
    def save(self):
        mysql = MySql()
        dic = {'taskName':self.taskName, 'content':self.content,
               'deadline':self.deadline, 'importance':self.importance}
        mysql.insert('user_'+self.userName, dic)

    @staticmethod
    def getAttr(columnNames = None):
        attrs = ["taskName", "content", "deadline", "importance"]
        dic = {}
        #创建用户数据库时需要
        if columnNames is None:
            for a in attrs:
               dic[a] = "VARCHAR (255)"
            return dic