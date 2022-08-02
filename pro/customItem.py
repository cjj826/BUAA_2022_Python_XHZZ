from PyQt5.QtWidgets import QListWidgetItem, QWidget, QCheckBox, QLabel, QHBoxLayout

class CustomListWidgetItem(QListWidgetItem):
    count = 0
    def __init__(self, task):
        super(CustomListWidgetItem, self).__init__()
        self.widget = QWidget()
        self.widget.setObjectName("customwidget" + str(self.count))
        self.count += 1
        self.widget.setStyleSheet("#"+str(self.widget.objectName())+"{border-bottom: 1px solid black;}")
        taskName = task.taskName
        deadTime = task.deadline.split(" ")[1]
        self.checkBox = QCheckBox()
        self.titleLabel = QLabel()
        self.titleLabel.setText(taskName)
        self.stateLabel = QLabel()
        self.stateLabel.setText("未开始")
        self.timeLabel = QLabel()
        self.timeLabel.setText(deadTime)
        self.layout_main = QHBoxLayout()
        self.layout_main.addWidget(self.checkBox)
        self.layout_main.addWidget(self.titleLabel)
        self.layout_main.addWidget(self.stateLabel)
        self.layout_main.addWidget(self.timeLabel)
        self.layout_main.setStretch(1,2)
        #self.layout_main.setStretch()
        self.widget.setLayout(self.layout_main)
        self.setSizeHint(self.widget.sizeHint())

if __name__ == "__main__":
    s = CustomListWidgetItem(None)