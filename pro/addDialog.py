import sys

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QDialog, QApplication, QDateTimeEdit

import addAssignment
from mytask import Mytask
import datetime
#title, type, start, end, time, importance, content

class AddDialog(addAssignment.Ui_dialog, QDialog):
    def __init__(self):
        super(AddDialog, self).__init__()
        self.setupUi(self)
        self.set = False
        self.start.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.end.setDisplayFormat('yyyy-MM-dd HH:mm')
        self.start.setCalendarPopup(True)
        self.start.setDateTime(QDateTime.currentDateTime())
        self.end.setCalendarPopup(True)
        self.end.setDateTime(QDateTime.currentDateTime())

        self.confirmButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.exit__)
        self.checkBox.stateChanged.connect(self.setDailyTask)
        self.dailyTask = False
    def setDailyTask(self):
        if self.checkBox.isChecked():
            self.dailyTask = True
        else:
            self.dailyTask = False
    def setUserName(self, string):
        self.userName = string

    def setTitleAuto(self, string):
        """通过回车栏内容自动设置标题
        :param string: 标题
        """
        self.title.setText(string)

    def exit__(self):
        self.set = False
        self.close()

    def confirm(self):
        self.set = True
        stime = list(map(int, self.time.dateTime().toString("HH:mm").split(":")))
        stime = stime[0] * 60 + stime[1]
        if not self.dailyTask:
            task = Mytask(userName=self.userName,
                          taskName=self.title.text(),
                          taskType=self.type.currentText(),
                          startline=self.start.dateTime().toString("yyyy-MM-dd HH:mm"),
                          deadline=self.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                          duration= stime,
                          importance=self.importance.currentText(),
                          content=self.content.toPlainText())
            task.save()
        else :
            start = self.start.dateTime().toString("yyyy-MM-dd")
            end = self.end.dateTime().toString("yyyy-MM-dd")
            start = datetime.datetime.strptime(start, "%Y-%m-%d")
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
            days = (end - start).days + 1
            for i in range(days):
                delta = datetime.timedelta(days=i)
                day = start + delta
                task = Mytask(userName=self.userName,
                          taskName=self.title.text(),
                          taskType=self.type.currentText(),
                          startline=day.strftime("%Y-%m-%d") + " " + self.start.dateTime().toString("HH:mm"),
                          deadline=day.strftime("%Y-%m-%d") + " " +self.end.dateTime().toString("HH:mm"),
                          duration= stime,
                          importance=self.importance.currentText(),
                          content=self.content.toPlainText())
                task.save()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    addDialog = AddDialog()
    addDialog.show()
    print(addDialog.start.dateTime().toString("yyyy-MM-dd HH:mm"))
    sys.exit(app.exec_())