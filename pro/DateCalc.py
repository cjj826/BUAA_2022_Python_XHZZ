# -*- coding: utf-8 -*-#
import math
import ephem
from Defines import *

"""JDN means the Julian Date Number, UTC means the Universal Time Coordinated"""
def JDN2PyEphemDate(JDN, UTC=0):
	"""This Function will change the Julian Date Number to Date type in PyEphem"""
	return ephem.Date(JDN + UTC / 24 - 2415020)

def StandardEquinoxSolsticeInJDN(yearAsDate, angle):
	"""According to the introduced year and angle,
	find the appropriate vernal equinox, autumnal equinox,
	summer solstice and winter solstice
	as the reference point for solar terms"""
	angle %= 360
	if 0 <= angle < 90:
		standardEquinoxSolsticeDate = ephem.next_vernal_equinox(yearAsDate)
	elif 90 <= angle < 180:
		standardEquinoxSolsticeDate = ephem.next_summer_solstice(yearAsDate)
	elif 180 <= angle < 270:
		standardEquinoxSolsticeDate = ephem.next_autumn_equinox(yearAsDate)
	else:
		standardEquinoxSolsticeDate = ephem.next_winter_solstice(yearAsDate)
	"""turn to Julian Date"""
	JDN = ephem.julian_date(standardEquinoxSolsticeDate)
	return JDN


# 计算二十四节气
def SolarLongitudeForSunAtTargetJDN(JDN):
	"""Calculate the ecliptic longitude of the sun
	on the specified Julian day, expressed in radian system"""
	ephemDateAtTargetJDN = JDN2PyEphemDate(JDN)
	sunAtTargetEphemDate = ephem.Sun(ephemDateAtTargetJDN)  # date应为UT时间
	sunInRightAscensionAndDeclination = \
		ephem.Equatorial(sunAtTargetEphemDate.ra, sunAtTargetEphemDate.dec, epoch=ephemDateAtTargetJDN)
	sunInEcliptic = ephem.Ecliptic(sunInRightAscensionAndDeclination)
	logitube = sunInEcliptic.lon / ephem.degree / 180 * math.pi
	return logitube

def GetSolarTermInJDN(year, angle, targetYear=''):
	"""Gets the solar term date of the specific angle,
	expressed in Julian Date Number"""
	if angle > 270: year -= 1
	standardSolarTermJDN = StandardEquinoxSolsticeInJDN(str(year), angle)  # 初值
	standardSolarTermDate = JDN2PyEphemDate(standardSolarTermJDN, 8)
	standardSolarTermYear = standardSolarTermDate.triple()[0]
	if targetYear != '' and standardSolarTermYear != targetYear:
		"""standardSolarTermYear != targetYear, change the standard Solar Term
		if target year == '' then JDN may not in this year"""
		standardSolarTermJDN = StandardEquinoxSolsticeInJDN(str(year + 1), (angle + 90) % 360)
	JDN1 = standardSolarTermJDN
	while True:
		JDN2 = JDN1
		L = SolarLongitudeForSunAtTargetJDN(JDN2)
		JDN1 += math.sin(angle * math.pi / 180 - L) / math.pi * 180 # this is a random iteration function
		if abs(JDN1 - JDN2) < 0.00001: # Accuracy less than 1 second
			break
	return JDN1  # UT


def JDNDifferValueAtUTC8(JDN1, JDN2):
	"""Compare the difference between two Julian Dates
	(jdn1 and jdn2) in UTC + 8 time zone, return the different day(int)"""
	return math.floor(JDN1 + 8 / 24 + 0.5) - math.floor(JDN2 + 8 / 24 + 0.5)


def JDN1GEJDN2(JDN1, JDN2):
	"""Compare whether jdn1 is greater than or equal to jdn2, return bool"""
	if JDNDifferValueAtUTC8(JDN1, JDN2) >= 0: return True  # JDN1 >= JDN2
	else: return False


def FindLunarMonthIndexOfTargetJDN(JDN, lunarMonthFirstDayTableInJDN):
	"""Find the lunar month of the target JDN, return index"""
	for i in range(len(lunarMonthFirstDayTableInJDN)):
		if not JDN1GEJDN2(JDN, lunarMonthFirstDayTableInJDN[i]):
			return i - 1


def LastYearLunarMonthForWinterSolDate(year): # 寻找年前冬至月朔日
	"""Given a Gregorian year, find the lunar month
	corresponding to the winter solstice of the previous year"""
	if year == 1: # The winter solstice before the first year of A.D. is in the year 1 B.C
		year -= 1  # 公元元年前冬至在公元前1年
	winterSolsticeDate = ephem.next_solstice((year - 1, 12)) # 年前冬至
	winterSolsticeJDN = ephem.julian_date(winterSolsticeDate)
	# 可能的三种朔日
	date1 = ephem.next_new_moon(JDN2PyEphemDate(winterSolsticeJDN - 0))
	JDN1 = ephem.julian_date(date1)
	date2 = ephem.next_new_moon(JDN2PyEphemDate(winterSolsticeJDN - 29))
	JDN2 = ephem.julian_date(date2)
	date3 = ephem.next_new_moon(JDN2PyEphemDate(winterSolsticeJDN - 31))
	JDN3 = ephem.julian_date(date3)
	if JDN1GEJDN2(winterSolsticeJDN, JDN1): # 冬至合朔在同一日或下月
		return date1
	elif JDN1GEJDN2(winterSolsticeJDN, JDN2) and (not JDN1GEJDN2(winterSolsticeJDN, JDN1)):
		return date2
	elif JDN1GEJDN2(winterSolsticeJDN, JDN3): # 冬至在上月
		return date3


def LunarCalendar(year, type=1):   # type=1时截止到次年冬至朔，=0时截止到次年冬至朔次月
	"""Determine all solar terms and lunar months of the year (including leap)"""
	lastYearWinterSolsticeFirstMoonDate = LastYearLunarMonthForWinterSolDate(year)
	loopFirstMoonDate = lastYearWinterSolsticeFirstMoonDate  # 计算用朔，date格式
	LunarMonthFirstDayTableInJDN = [ephem.julian_date(lastYearWinterSolsticeFirstMoonDate)]  # 存储ut+8 JD，起冬至朔
	nextYearWinterSolsticeFirstMoonJDN = ephem.julian_date(LastYearLunarMonthForWinterSolDate(year + 1))  # 次年冬至朔
	i = -1  # 中气序，从0起计
	j = -1  # 计算连续两个冬至月中的合朔次数，从0起计
	lunarLeapMonthIndex = 0
	flag = False
	# 查找所在月及判断置闰
	while not JDN1GEJDN2(LunarMonthFirstDayTableInJDN[j + type], nextYearWinterSolsticeFirstMoonJDN):  # 从冬至月起查找，截止到次年冬至朔
		i += 1
		j += 1
		loopFirstMoonDate = ephem.next_new_moon(loopFirstMoonDate)  # 次月朔
		LunarMonthFirstDayTableInJDN.append(ephem.julian_date(loopFirstMoonDate))
		# 查找本月中气，若无则置闰
		if j == 0: continue  # 冬至月一定含中气，从次月开始查找
		angle = (-90 + 30 * i) % 360  # 本月应含中气，起冬至（不计）
		midSolarTermJDN = GetSolarTermInJDN(year, angle)
		# 不判断气在上月而后气在后月的情况，该月起的合朔次数不超过气数，可省去
		if JDN1GEJDN2(midSolarTermJDN, LunarMonthFirstDayTableInJDN[j + 1]) and flag == False:  # 中气在次月，则本月无中气
				lunarLeapMonthIndex = j  # 置闰月
				i -= 1
				flag = True  # 仅第一个无中气月置闰
	# 生成农历月序表
	lunarMonthNameTable = []
	for k in range(len(LunarMonthFirstDayTableInJDN)):
		lunarMonthNameTable.append(LUNAR_MONTH_TABLE[(k - 2) % 12])  # 默认月序
		if j + type == 13:  # 仅12次合朔不闰，有闰时修改月名
			if k == lunarLeapMonthIndex:
				lunarMonthNameTable[k] = '闰' + LUNAR_MONTH_TABLE[(k - 1 - 2) % 12]
			elif k > lunarLeapMonthIndex:
				lunarMonthNameTable[k] = LUNAR_MONTH_TABLE[(k - 1 - 2) % 12]
	return lunarMonthNameTable, LunarMonthFirstDayTableInJDN   # 月名表，合朔JD日期表
