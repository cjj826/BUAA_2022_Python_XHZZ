from datetime import datetime
s = str(datetime.now().time()).split(":")
print(int(s[0])*60+int(s[1]))