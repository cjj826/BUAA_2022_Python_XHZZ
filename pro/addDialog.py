import sys

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QDialog, QApplication, QDateTimeEdit

import addAssignment
from mytask import Mytask

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
        print("add Assign!")
        #LineEdit用text
        #textEdit用toPlainText
        #time用dataTime().toString
        #combox用currentText
        stime = list(map(int, self.time.dateTime().toString("HH:mm").split(":")))
        stime = stime[0] * 60 + stime[1]
        task = Mytask(userName=self.userName,
                      taskName=self.title.text(),
                      taskType=self.type.currentText(),
                      startline=self.start.dateTime().toString("yyyy-MM-dd HH:mm"),
                      deadline=self.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                      duration= stime,
                      importance=self.importance.currentText(),
                      content=self.content.toPlainText())
        task.save()
        print("saved")
        self.close()
        print("closed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    addDialog = AddDialog()
    addDialog.show()
    print(addDialog.start.dateTime().toString("yyyy-MM-dd HH:mm"))
    sys.exit(app.exec_())