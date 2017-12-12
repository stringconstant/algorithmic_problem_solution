"""
ID: duweira1
LANG: PYTHON2
TASK: milk2

"""

fin = open('milk2.in','r')
fout = open('milk2.out','w')


dataList = []

with open('milk2.in') as f:
	dataList = (f.read().splitlines())

num = int(dataList[0])

tlst = []

for i in range(1,len(dataList)):
	firstTriggered = False
	first = ""
	second = ""
	for s in dataList[i]:
		if firstTriggered == False:
			if s != " ":
				first += s
			else:
				firstTriggered = True
		elif firstTriggered == True:
			second += s

	tlst.append([int(first),int(second)])


def calculate(number,list):
	l = list
	start = []
	end = []
	maxVal = 0
	minVal = 1000001
	time = []
	noMilk = []
	yesMilk = []
	startCounting = False

	for item in l:
		start.append(item[0])
		end.append(item[1])

	for item in start:
		if item < minVal:
			minVal = item

	for item in end:
		if item > maxVal:
			maxVal = item

	for i in range(maxVal):
		time.append(0)

	for i in range(number):
		for j in range(start[i],end[i]):
			time[j] += 1

	prev = 0
	empCount = 0
	fullCount = 0
	for number in time:
		if startCounting == False:
			if number > 0:
				startCounting = True
				prev = number
				fullCount += 1
		elif startCounting == True:
			if (prev > 0 and number > 0):
				fullCount += 1
				prev = number
			elif (prev > 0 and number == 0):
				yesMilk.append(fullCount)
				fullCount = 0
				empCount += 1
				prev = number
			elif (prev == 0 and number == 0):
				empCount += 1
				prev = number
			elif (prev == 0 and number > 0):
				noMilk.append(empCount)
				empCount = 0
				fullCount += 1
				prev = number
	yesMilk.append(fullCount)
	noMilk.append(empCount)

	fout.write(str(max(yesMilk)) + " " + str(max(noMilk)) + "\n")
	fout.close()

calculate(num,tlst)


