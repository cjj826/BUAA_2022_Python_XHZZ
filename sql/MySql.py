import pymysql


class MySql():
    def __init__(self, init = False):
        """
        create a MySqlHelper
        :param init: True means initializing the database
        """
        try:
            self.con = pymysql.connect(host='localhost',
                                      user='root',
                                      password='888718')
            self.con.autocommit(1)
            self.cursor = self.con.cursor()
        except:
            print("DataBase connect error,please check the db config.")

        if init:
            self.cursor.execute('create DATABASE if not exists scheduler')
            self.con.select_db('scheduler')
            self.cursor.execute('''create table if not exists sc_user(
                id INT PRIMARY KEY auto_increment,
                username VARCHAR (255),
                password VARCHAR (255)
                )''')
        else :
            self.con.select_db('scheduler')

    def insert(self, table, params):
        """
        insert data into the table
        :param table: the name of table
        :param params: a diction including (column name, property)
        :return: void
        """
        key = []
        value = []
        for k, v in params.items():
            key.append(k)
            value.append('\''+v+'\'')
        sql = 'insert into %s' % table
        sql += '(' + ','.join(key) + ')' + ' values(' + ','.join(value) + ')'
        print('insert:' + sql)
        self.executeCommit(sql)

    def select(self, table, listnames = None, all = False):
        """
        query something
        :param table: name of table
        :param listnames: a list contains column names queried
        :param all: True means query all columns
        :return: query results
        """
        if all:
            sql = 'select * from ' + table
        else :
            sql = 'select (' + ','.join(listnames) + ') from '+table
        return self.executeSql(sql)

    def executeSql(self, sql):
        """
        Executes a sql statement that queries something like *SELECT*
        :param sql: a sql statement
        :return: a result set for a read operation
        """
        try:
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except pymysql.Error as e:
            error = '执行sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print(error)

    def executeCommit(self, sql):
        """
        执行sql语句，针对更新，删除等。操作失败时回滚
        :param sql: sql语句
        :return: void
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except pymysql.Error as e:
            self.con.rollback()
            error = '执行数据库sql语句失败(%s): %s' % (e.args[0], e.args[1])
            print("error:", error)
            return error

    def closeDataBase(self):
        """
        关闭数据库连接
        :return: void
        """
        if self.con:
            self.con.close()
        else :
            print("DataBase doesn't connect,close connectiong error;please check the db config.")

if __name__ == '__main__':
    mysql = MySql(init=True)
    mysql.closeDataBase()