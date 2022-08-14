# -*- coding: utf-8 -*-#
from DateCalc import *
import re
import time


def borderTargetDateLabel(calendar, month, day):
	"""Add a border to a target Date Label"""
	firstDayNumber = int(re.findall(r'(\d+)</font>', calendar.labs[0][0].getLabel().text())[0])
	if firstDayNumber == 1:
		targetDateIndex = - firstDayNumber + day
	else:
		targetDateIndex = MAX_DAYSinMONTH_TABLE[month - 1] - firstDayNumber + day
	global selected
	selected = calendar.labs[targetDateIndex // 7][targetDateIndex % 7].getLabel()
	selected.setStyleSheet("QWidget{border:1px solid; border-radius: 5px; border-color:#1E90FF}")


def updateYearItems(calendar):
	"""update the year items in comboBoxYear"""
	century = calendar.comboBoxCentury.currentIndex() + start_century + 1
	calendar.comboBoxYear.clear()
	for i in range(100):
		if century == 1 and i == 0: continue
		if century <= 0:
			calendar.comboBoxYear.addItem('BC' + str(abs(century) * 100 + 100 - i) + '年')
		else:
			calendar.comboBoxYear.addItem(str((century - 1) * 100 + i) + '年')
	calendar.comboBoxYear.setCurrentIndex(0)


def lastYear(calendar):
	"""set comboBox year to last year"""
	comboBoxYearIndex = calendar.comboBoxYear.currentIndex()
	if comboBoxYearIndex == 0:
		century = calendar.comboBoxCentury.currentIndex()
		calendar.comboBoxCentury.setCurrentIndex(century - 1)
		calendar.comboBoxYear.setCurrentIndex(calendar.comboBoxYear.count() - 1)
	elif comboBoxYearIndex == -1:
		getYearMonth(calendar, wheel=-1)
	else:
		calendar.comboBoxYear.setCurrentIndex(comboBoxYearIndex - 1)


def nextYear(calendar):
	"""set comboBox year to next year"""
	comboBoxYearIndex = calendar.comboBoxYear.currentIndex()
	century = calendar.comboBoxCentury.currentIndex()
	if comboBoxYearIndex == -1 or century == endCentury - start_century - 1:
		getYearMonth(calendar, wheel=1)
	elif calendar.comboBoxYear.count() > 0 and comboBoxYearIndex == calendar.comboBoxYear.count() - 1:
		calendar.comboBoxCentury.setCurrentIndex(century + 1)
	else:
		calendar.comboBoxYear.setCurrentIndex(comboBoxYearIndex + 1)


def jumpYear(calendar):  # 本世纪首年或末年时跳转上世纪或下世纪
	"""special function for wheel event emitted from comboBoxYear,
	set new century"""
	comboBoxYearIndex = calendar.comboBoxYear.currentIndex()
	comboBoxCenturyIndex = calendar.comboBoxCentury.currentIndex()
	if comboBoxYearIndex == 0:
		if comboBoxCenturyIndex == 0: pass
		else:
			calendar.comboBoxCentury.setCurrentIndex(comboBoxCenturyIndex - 1)
			calendar.comboBoxYear.setCurrentIndex(calendar.comboBoxYear.count() - 1)
	elif comboBoxYearIndex != -1 and comboBoxYearIndex == calendar.comboBoxYear.count() - 1:
		if comboBoxCenturyIndex == endCentury - start_century - 1: pass
		else: calendar.comboBoxCentury.setCurrentIndex(comboBoxCenturyIndex + 1)
	displayDate(calendar)


def lastMonth(calendar):
	"""set comboBoxMonth to last month"""
	comboBoxMonthIndex = calendar.comboBoxMonth.currentIndex()
	if comboBoxMonthIndex == 0:
		lastYear(calendar)
		calendar.comboBoxMonth.setCurrentIndex(11)
	else:
		calendar.comboBoxMonth.setCurrentIndex(comboBoxMonthIndex - 1)


def nextMonth(calendar):
	"""set comboBoxMonth to next month"""
	comboBoxMonthIndex = calendar.comboBoxMonth.currentIndex()
	if comboBoxMonthIndex == 11:
		nextYear(calendar)
		calendar.comboBoxMonth.setCurrentIndex(0)
	else:
		calendar.comboBoxMonth.setCurrentIndex(comboBoxMonthIndex + 1)


def jumpMonth(calendar):
	"""special function for wheel event emitted from comboBoxMonth,
	set new Year"""
	comboBoxMonthIndex = calendar.comboBoxMonth.currentIndex()
	if comboBoxMonthIndex == 0:
		lastYear(calendar)
		calendar.comboBoxMonth.setCurrentIndex(11)
	elif comboBoxMonthIndex == 11:
		nextYear(calendar)
		calendar.comboBoxMonth.setCurrentIndex(0)
	displayDate(calendar)


def getSolorTerms(year):
	"""Obtain the dates of all lunar terms in the Gregorian calendar year"""
	solarTermsTable = [[i] for i in range(12)]
	for i in range(24):
		solarTermDate = JDN2PyEphemDate(GetSolarTermInJDN(year, i * 15, year), 8)
		solarTermYear, solarTermMonth, solarTermDay = solarTermDate.triple()
		if solarTermYear != year:
			solarTermDate = JDN2PyEphemDate(GetSolarTermInJDN(year + (year - solarTermYear), i * 15, year), 8)
			solarTermYear, solarTermMonth, solarTermDay = solarTermDate.triple()
		if solarTermYear == year:  # 部分年无某节气，如BC1243年无冬至
			solarTermsTable[solarTermMonth-1].append([int(solarTermDay), (i + 6) % 24])  # 按月存储
	for j in range(len(solarTermsTable)): solarTermsTable[j].pop(0)
	"""
	solarTermsTable: [
						[ # for Jan
							[day1, solarTermIndex1], [day2, solarTermIndex2], ...
						], [# for Feb], ... ,[# for Dec]
					 ]
	"""
	return solarTermsTable


def resetNewYearEve(festival, lunarMonthNameTable, LunarMonthFirstDayTableInJDN):  # 重设节日日期
	"""reset the New Year Eve according to the 12th lunar month"""
	lunarMonthIndex = lunarMonthNameTable.index(festival[0])
	if JDNDifferValueAtUTC8(LunarMonthFirstDayTableInJDN[lunarMonthIndex + 1],
							LunarMonthFirstDayTableInJDN[lunarMonthIndex]) == 29:
		"""calc the len of lunar month in lunar month index"""
		festival[1] = '廿九'
	else:
		festival[1] = '三十'
	return festival


def changeLunarFestivalToGregCalendar(currentFes, lunarMonthNameTable, LunarMonthFirstDayTableInJDN):
	"""Convert festivals from the lunar calendar to the Gregorian calendar"""
	# 节日农历月转公历月
	for festival in LUNAR_FRSTIVALS:
		if currentFes == festival[2]:
			if festival[2] == '除夕':
				festival = resetNewYearEve(festival, lunarMonthNameTable, LunarMonthFirstDayTableInJDN)
			month2 = lunarMonthNameTable.index(festival[0])
			shuo = LunarMonthFirstDayTableInJDN[month2]
			month, day = JDN2PyEphemDate(shuo, 8).triple()[1:]
			if int(day) + LUNAR_DAY_TABLE.index(festival[1]) <= MAX_DAYSinMONTH_TABLE[month - 1]: month -= 1
			if month > 11: month -= 12
			return month


def getYearMonth(calendar, wheel=0): # 根据输入重设年月
	"""Reset the month and year according to the input of combobox,
	or it can be used as an interface to obtain the month and year of the current year"""
	comboBoxYearEdit = calendar.comboBoxYear.currentText()
	try:
		year = int(re.search(r'-?\d+', comboBoxYearEdit).group())
	except:
		return 0, 0  # 异常输入
	if year == 0: return 0, 0
	if 'BC' in calendar.comboBoxYear.currentText() or 'bc' in comboBoxYearEdit:
		year = -year
	year += wheel
	century = year // 100
	if start_century * 100 <= year < endCentury * 100:
		calendar.comboBoxCentury.setCurrentIndex(century - start_century)
		if century == 0: calendar.comboBoxYear.setCurrentIndex(year % 100 - 1)
		else: calendar.comboBoxYear.setCurrentIndex(year % 100)
	else:
		calendar.comboBoxCentury.setCurrentIndex(-1)
		calendar.comboBoxYear.clear()
		if wheel == 0: calendar.comboBoxYear.setCurrentText(comboBoxYearEdit)
		else: calendar.comboBoxYear.setCurrentText(str(year))
	if calendar.sender() == calendar.comboBoxFindFestival: month = -1
	else: month = calendar.comboBoxMonth.currentIndex()
	global currentYear
	if year != currentYear or currentYear == '':
		currentYear = year
		updateYearInformation()
	return year, month


def updateYearInformation():
	"""Correctly update the lunar month name table, lunar new moon date table and
	solar term table corresponding to the Gregorian date of the current year"""
	global currentLunarMonthNameTable, currentLunarMonthFirstDayTableInJDN, \
		currentSolarTermsTable, currentYear
	currentLunarMonthNameTable, currentLunarMonthFirstDayTableInJDN = LunarCalendar(currentYear, 0)
	currentSolarTermsTable = getSolorTerms(currentYear)

# from MyCalendar import MyCalendar
# def displayMonth(calendar:MyCalendar):
def displayMonth(calendar):
	year, month = getYearMonth(calendar)
	if year == 0: return 0, 0, 0
	lunarMonthNameTable, lunarMonthFirstDateTableInJDN, solarTermsTable = currentLunarMonthNameTable, \
															  currentLunarMonthFirstDayTableInJDN, \
															  currentSolarTermsTable
	if JDN1GEJDN2(ephem.julian_date((year, 12, 31)), lunarMonthFirstDateTableInJDN[-2] + 29):
		# Judge the relationship between the end of the Gregorian calendar and the winter solstice
		lunarMonthNameTable1, lunarMOnthFirstDateTableInJDN1 = LunarCalendar(year + 1)
		lunarMonthNameTable = lunarMonthNameTable[:-2] + lunarMonthNameTable1[:2]
		lunarMonthFirstDateTableInJDN = lunarMonthFirstDateTableInJDN[:-2] + lunarMOnthFirstDateTableInJDN1[:3]
	currentFestival, festivalDay = '', 0
	if calendar.sender() == calendar.comboBoxFindFestival:
		currentFestival = calendar.comboBoxFindFestival.currentText()
		month = changeLunarFestivalToGregCalendar(currentFestival, lunarMonthNameTable, lunarMonthFirstDateTableInJDN)
		calendar.comboBoxMonth.setCurrentIndex(month)
	MAX_DAYSinMONTH_TABLE[1] = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
	if year < 1582 and year % 4 == 0: MAX_DAYSinMONTH_TABLE[1] = 29
	i = month
	firstJDOfGregMonth = ephem.julian_date((year, i + 1))
	lunarMonthIndex_FirstDayOfGregMonth = FindLunarMonthIndexOfTargetJDN(firstJDOfGregMonth,
																	lunarMonthFirstDateTableInJDN)  # 本月1日对应的农历月Index
	diff_GregMonthAndLunarMonth = JDNDifferValueAtUTC8(firstJDOfGregMonth, lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth])  # 本月1日的农历日期
	curLunarMonthLen_GregMonth = JDNDifferValueAtUTC8(lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth + 1],
								lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth])
	nextLunarMonthLen_GregMonth = JDNDifferValueAtUTC8(lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth + 2],
								lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth + 1])
	offsetOfCurrentCalendarCell = int((firstJDOfGregMonth + 0.5) % 7)
	for j in range(6):
		for k in range(7):
			# day - 公历第一天的日期
			day = j * 7 + k - offsetOfCurrentCalendarCell + 1
			# lunarDay - 农历本月第一天
			lunarDay = diff_GregMonthAndLunarMonth + j * 7 + k - offsetOfCurrentCalendarCell
			if lunarDay < 0:  # 月首日所在农历月上月
				lunarMonthLen = JDNDifferValueAtUTC8(lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth],
										   lunarMonthFirstDateTableInJDN[lunarMonthIndex_FirstDayOfGregMonth - 1])
				lunarMonthDay_Cell = LUNAR_DAY_TABLE[lunarDay % lunarMonthLen]
				lunarMonthIndex_Cell = lunarMonthIndex_FirstDayOfGregMonth - 1
			elif 0 <= lunarDay < curLunarMonthLen_GregMonth:
				lunarMonthDay_Cell = LUNAR_DAY_TABLE[lunarDay]
				lunarMonthIndex_Cell = lunarMonthIndex_FirstDayOfGregMonth
			elif curLunarMonthLen_GregMonth <= lunarDay < curLunarMonthLen_GregMonth + nextLunarMonthLen_GregMonth:
				lunarMonthDay_Cell = LUNAR_DAY_TABLE[lunarDay - curLunarMonthLen_GregMonth]
				lunarMonthIndex_Cell = lunarMonthIndex_FirstDayOfGregMonth + 1
			elif lunarDay >= curLunarMonthLen_GregMonth + nextLunarMonthLen_GregMonth:
				lunarMonthDay_Cell = LUNAR_DAY_TABLE[lunarDay - curLunarMonthLen_GregMonth - nextLunarMonthLen_GregMonth]
				lunarMonthIndex_Cell = lunarMonthIndex_FirstDayOfGregMonth + 2
			if day == 1:
				lunarMonthIndex1_Cell = lunarMonthIndex_Cell
				lunarMonthDay1_Cell = lunarMonthDay_Cell
			if day == MAX_DAYSinMONTH_TABLE[i]:
				lunarMonthIndex2_Cell = lunarMonthIndex_Cell
				lunarMonthDay2_Cell = lunarMonthDay_Cell
			dateInfo[j * 7 + k] = [day, lunarMonthNameTable[lunarMonthIndex_Cell], lunarMonthDay_Cell, firstJDOfGregMonth+day-1, solarTermsTable[i]]
			if year == 1582 and i == 9: dateInfo[j * 7 + k][-1] = [solarTermsTable[i][0], solarTermsTable[i-1][1]]  # 该月无节气，月干支序从上月获取
			if lunarMonthDay_Cell == '初一': lunarMonthDay_Cell = lunarMonthNameTable[lunarMonthIndex_Cell]
			# 显示月历
			if j == 0 and k < offsetOfCurrentCalendarCell:  # 上月
				calendar.labs[j][k].getLabel().setText(font(MAX_DAYSinMONTH_TABLE[i - 1] - offsetOfCurrentCalendarCell + k + 1, LABEL_SIZE) + font(lunarMonthDay_Cell))
			else:  # 本月
				if day <= MAX_DAYSinMONTH_TABLE[i]:
					if year == 1582 and i == 9 and day > 4:
						if day < 15: continue
						else: calendar.labs[j + (k - 10) // 7][k - 3].getLabel().setText(font(day, LABEL_SIZE, "black", 800) + font(lunarMonthDay_Cell))
					else:
						calendar.labs[j][k].getLabel().setText(font(day, LABEL_SIZE, "black", 800) + font(lunarMonthDay_Cell))  # "500;font-family:微软雅黑"
				else:  # 次月
					if year == 1582 and i == 9:
						calendar.labs[j + (k - 10) // 7][k - 3].getLabel().setText(font(day - MAX_DAYSinMONTH_TABLE[i], LABEL_SIZE) + font(lunarMonthDay_Cell))
						if day - MAX_DAYSinMONTH_TABLE[i] == 11:
							for m in range(10): calendar.labs[j - 1 + (m + k - 2) // 7][(m + k - 2) % 7].getLabel().setText("")
					else: calendar.labs[j][k].getLabel().setText(font(day - MAX_DAYSinMONTH_TABLE[i], LABEL_SIZE) + font(lunarMonthDay_Cell))
	# 显示节日
	QingMingDay = 0 # QingMing festival is not only a solar term, but also is a festival
	for solarTerm in solarTermsTable[i]:  # 节气
		solarTermDay = solarTerm[0] + offsetOfCurrentCalendarCell - 1
		if year == 1582 and i == 9: solarTermDay -= 10
		calendar.labs[solarTermDay // 7][solarTermDay % 7].getLabel().setText(font(solarTerm[0], LABEL_SIZE, "black", 800) +
																			  font(SOLAR_TERMS_TABLE[solarTerm[1]], 8, "red"))
		if solarTerm[1] == 7: QingMingDay = solarTerm[0]
	if year >= 1949:  # 公历节日起始年
		if QingMingDay:
			calendar.labs[(QingMingDay + offsetOfCurrentCalendarCell - 1) // 7][(QingMingDay + offsetOfCurrentCalendarCell - 1) % 7].\
				getLabel().setText(font(QingMingDay, LABEL_SIZE, "red", 800) + font("清明", 8, "red"))
		for festival in GREGORIAN_FESTIVALS:
			if festival[0] == month + 1:
				solarTermDay = festival[1] + offsetOfCurrentCalendarCell - 1
				calendar.labs[solarTermDay // 7][solarTermDay % 7].getLabel().setText(font(festival[1], LABEL_SIZE, "red", 800) +
																					  font(festival[2], 8, "red"))
	if year > 1911:  # 农历节日起始年
		lunarMonthDayIndex_Cell = LUNAR_DAY_TABLE.index(lunarMonthDay1_Cell)
		for festival in LUNAR_FRSTIVALS:
			if festival[2] == '除夕': festival = resetNewYearEve(festival, lunarMonthNameTable, lunarMonthFirstDateTableInJDN)
			solarTermDay = LUNAR_DAY_TABLE.index(festival[1])
			if festival[0] == lunarMonthNameTable[lunarMonthIndex1_Cell] and solarTermDay >= lunarMonthDayIndex_Cell:  # 该月农历首日
				solarTermDay += -lunarMonthDayIndex_Cell + offsetOfCurrentCalendarCell
				calendar.labs[solarTermDay // 7][solarTermDay % 7].getLabel().setText(font(solarTermDay - offsetOfCurrentCalendarCell + 1, LABEL_SIZE, "red", 800) +
																					  font(festival[2], 8, "red"))
			elif festival[0] == lunarMonthNameTable[lunarMonthIndex1_Cell+1] and solarTermDay <= LUNAR_DAY_TABLE.index(lunarMonthDay2_Cell):  # 该月农历末日
				solarTermDay += JDNDifferValueAtUTC8(lunarMonthFirstDateTableInJDN[lunarMonthIndex1_Cell + 1], lunarMonthFirstDateTableInJDN[lunarMonthIndex1_Cell]) - lunarMonthDayIndex_Cell + offsetOfCurrentCalendarCell
				calendar.labs[solarTermDay // 7][solarTermDay % 7].getLabel().setText(font(solarTermDay - offsetOfCurrentCalendarCell + 1, LABEL_SIZE, "red", 800) +
																					  font(festival[2], 8, "red"))
			elif lunarMonthIndex2_Cell - lunarMonthIndex1_Cell == 2 and festival[0] == lunarMonthNameTable[lunarMonthIndex2_Cell]:  # 跨2月
				solarTermDay += JDNDifferValueAtUTC8(lunarMonthFirstDateTableInJDN[lunarMonthIndex1_Cell + 2], lunarMonthFirstDateTableInJDN[lunarMonthIndex1_Cell]) - lunarMonthDayIndex_Cell + offsetOfCurrentCalendarCell
				if 0 < solarTermDay <= MAX_DAYSinMONTH_TABLE[i] + offsetOfCurrentCalendarCell:
					calendar.labs[solarTermDay // 7][solarTermDay % 7].getLabel().\
						setText(font(solarTermDay - offsetOfCurrentCalendarCell + 1, LABEL_SIZE, "red", 800) + font(festival[2], 8, "red"))
			if festival[2] == currentFestival:
				festivalDay = solarTermDay - offsetOfCurrentCalendarCell + 1

	for i in range(6):
		for j in range(7):
			calendar.labs[i][j].updateMissionsInMissionList()
	return year, month, festivalDay

def displayDate(calendar, init = 0):
	global selected
	try:
		selected.setStyleSheet("")
	except:
		pass
	if calendar.sender() in [None, calendar.buttonToday] or init == 1:  # 设为今日
		year, month, day = time.localtime(time.time())[0:3]
		month -= 1
		calendar.comboBoxCentury.setCurrentIndex(-start_century + year // 100)
		calendar.comboBoxYear.setCurrentIndex(year % 100)
		calendar.comboBoxMonth.setCurrentIndex(month % 12)
		displayMonth(calendar)
		borderTargetDateLabel(calendar, month, day)
	else:
		if calendar.sender() in [calendar.comboBoxCentury, calendar.comboBoxYear, calendar.comboBoxMonth,
								 calendar.buttonLastMonth, calendar.buttonNextMonth, calendar.buttonLastYear,
								 calendar.buttonNextYear, calendar.comboBoxFindFestival]:  # 设为原公历日
			year, month, day = displayMonth(calendar)
			if year == 0: return 0
			if calendar.sender() != calendar.comboBoxFindFestival: day = int(re.findall(r'(\d+)</font>', calendar.labInfo.text())[0])  # 公历日期
			if day > MAX_DAYSinMONTH_TABLE[month]: day = MAX_DAYSinMONTH_TABLE[month]  # 跳到上月底
			borderTargetDateLabel(calendar, month, day)
		else:  # 点击日期跳转
			year, month = getYearMonth(calendar)
			if year == 0:
				return 0
			selected = calendar.sender()
			if selected.text() == "":
				return 0  # 1582年被删除的日期
			day = int(re.findall(r'(\d+)</font>', selected.text())[0])  # 公历日期
			if not re.search("<font style='font-size:%dpx; text-align:center; color:gray"%(LABEL_SIZE), selected.text()):  # 本月内
				calendar.sender().setStyleSheet("QLabel{border:3px solid; border-radius: 5px; border-color:#1E90FF}")  # 1E90FF 9400D3
			else:   # 跳转前后月
				if day > 20:
					lastMonth(calendar)
				else:
					nextMonth(calendar)
				year, month = displayMonth(calendar)[:2]  # 更新月历
				borderTargetDateLabel(calendar, month, day)
	# 日期相关显示信息
	targetDayJDN = math.floor(ephem.julian_date((year, month + 1, day)) + 8/24 + 0.5)
	todayJDN = math.floor(ephem.julian_date(time.localtime(time.time())[0:3]) + 8 / 24 + 0.5)
	difference = targetDayJDN - todayJDN
	if difference > 0: difference = '距今：' + str(abs(difference)) + '天后'
	elif difference == 0: difference = '今天'
	else: difference = '距今：' + str(abs(difference)) + '天前'
	week = GREGORIAN_WEEKDAY[math.floor(targetDayJDN % 7)]
	lunarMonthName, lunarMonthDay, JDN, solarTermsSet = dateInfo[day-dateInfo[0][0]][1:]
	yearNumber = year
	# count1 = count2 = len(solarTermsSet)
	# for i in range(count1):
	# 	if solarTermsSet[i][1] < 3: count1 -= 1
	# 	if solarTermsSet[i][1] == 3 and day < solarTermsSet[i][0]: count2 -= 1
	# if count1 == 0: yearNumber -= 1  # 该月所有节气在立春前
	# elif count2 != len(solarTermsSet): yearNumber -= 1  # 立春所在月
	if month < 3 and LUNAR_MONTH_TABLE.index(lunarMonthName.split('闰')[-1]) >= 10:
		yearNumber -= 1
	if yearNumber < 0:
		# 干支
		sexagenaryCycleName_Year = SEXAGENARY_CYCLE_TABLE[(yearNumber - 3) % 60]
	else:
		sexagenaryCycleName_Year = SEXAGENARY_CYCLE_TABLE[(yearNumber - 4) % 60]
	yearNameStr = yearChangeToAD(year)
	zodiacName = ZODIAC_TABLE[(yearNumber - 4) % 12]
	if year < 0: year += 1
	solarTermDay = 99
	for i in range(len(solarTermsSet)):
		if solarTermsSet[i][1] % 2 == 1:
			solarTermDay = solarTermsSet[i][0]
	if day >= solarTermDay:
		sexagenaryCycleName_Month = SEXAGENARY_CYCLE_TABLE[(year * 12 + 13 + month) % 60]
	else:
		sexagenaryCycleName_Month = SEXAGENARY_CYCLE_TABLE[(year * 12 + 12 + month) % 60]
	sexgenaryCycleName_Day = SEXAGENARY_CYCLE_TABLE[math.floor(JDN + 8 / 24 + 0.5 + 49) % 60]
	# JDN、距今、年名、月、星期、日、农历月日、年干支、生肖名、月干支、日干支
	calendar.labInfo.setText("<br/>JDN {}<br/>{}<br/>{}<br/>{}月 星期{}<br/>{}{}{}年 〖{}〗<br/>{}月 {}日<br/><br/>".format(
		targetDayJDN,
		font(difference, 15, "black"),
		yearNameStr,
		month+1,
		week,
		font(day, 15, "black"),
		font(lunarMonthName+lunarMonthDay, 15, "black"),
		sexagenaryCycleName_Year,
		zodiacName,
		sexagenaryCycleName_Month,
		sexgenaryCycleName_Day))
