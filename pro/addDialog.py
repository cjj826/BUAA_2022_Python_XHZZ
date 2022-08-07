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
        task = Mytask(userName=self.userName,
                      taskName=self.title.text(),
                      content=self.content.toPlainText(),
                      deadline=self.end.dateTime().toString("yyyy-MM-dd HH:mm"),
                      importance=self.importance.currentText())
        task.save()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    addDialog = AddDialog()
    addDialog.show()
    sys.exit(app.exec_())