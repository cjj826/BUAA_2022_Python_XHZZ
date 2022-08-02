from PyQt5.QtWidgets import QListWidget


class MyListWidget(QListWidget):
    def __init__(self, QListWidget):
        super(MyListWidget, self).__init__()