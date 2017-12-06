"""
ID: duweira1
LANG: PYTHON2
TASK: friday
"""


fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

yr = 0

with open('friday.in') as f:
	yr = f.read().splitlines()

print(yr)

def isLeapYear(year):
	returnVal = False
	if year % 100 == 0:
		if year % 400 == 0:
			returnVal = True
	else:
		if year % 4 == 0:
			returnVal = True
	return returnVal


def dayToWeekday(day):
	if day % 7 == 0:
		return 1
	elif day % 7 == 1:
		return 2
	elif day % 7 == 2:
		return 3
	elif day % 7 == 3:
		return 4
	elif day % 7 == 4:
		return 5
	elif day % 7 == 5:
		return 6
	elif day % 7 == 6:
		return 7

def dayInMonth(month,year):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31
	elif month == 2:
		if isLeapYear(year) == True:
			return 29
		else:
			return 28
	elif month == 4 or month == 6 or month == 9 or month == 11:
		return 30



def calculate(year):
	tableValue = [0,0,0,0,0,0,0]
	firstThirteen = 12
	for years in range(1900,1900+year):
		for months in range(1,13):
			tableValue[dayToWeekday(firstThirteen)-1] += 1
			firstThirteen += dayInMonth(months,years)
	return [tableValue[5],tableValue[6],tableValue[0],tableValue[1],tableValue[2],tableValue[3],tableValue[4]]
		


tbl = calculate(int(yr[0]))
fout.write(str(tbl[0])+ ' ' + str(tbl[1]) + ' ' + str(tbl[2]) + ' ' + str(tbl[3]) + ' ' + str(tbl[4]) + ' ' + str(tbl[5]) + ' ' + str(tbl[6]) + '\n')
fout.close()

