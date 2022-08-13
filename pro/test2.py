# import requests
# r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
# r.encoding = 'utf-8'
# print(r.json())
# print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])
import os
import subprocess
result = subprocess.check_output("curl wttr.in/?format=%t+%l+%w", shell=True, encoding="utf-8")
l = list(map(str, result.split()))
temp = l[0][1:-1]
print(temp)
local = l[1][:-1]
print(local)
wind = l[3]
print(wind)
# temp = os.system("curl wttr.in/Jiaozuo?format=%t+%C")
# os.system("curl wttr.in")