import re

from PyQt5.QtCore import QDateTime
from datetime import  datetime

now = datetime.today().hour * 60 + datetime.today().minute

print(now)