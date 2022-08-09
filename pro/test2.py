import re

from PyQt5.QtCore import QDateTime
import datetime

nowdate = datetime.datetime.now().date()
delta = datetime.timedelta(days=7)
foredate = nowdate - delta
print(nowdate - foredate)