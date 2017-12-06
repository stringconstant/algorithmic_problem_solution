"""
ID: duweira1
LANG: PYTHON2
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

numberOfPeople = 0
nameOfPeople = []

dataList = []

with open('gift1.in') as f:
	dataList = (f.read().splitlines())


print(dataList)

numberOfPeople = int(dataList[0])


for index in range (1,numberOfPeople+1):
	nameOfPeople.append({'name':str(dataList[index]),'amount':0})

print(nameOfPeople)

def getNameSequence(name):
	for names in range(0,numberOfPeople):
		if nameOfPeople[names]['name'] == name:
			return names
			break

def getTwoValues(number):
	spaceTriggered = False
	first = ''
	second = ''
	for s in number:
		if s != ' ':
			if spaceTriggered == True:
				second += s
			else:
				first += s
		elif s == ' ':
			spaceTriggered = True

	return [int(first),int(second)]


currentPos = numberOfPeople + 2
for index in range(0,numberOfPeople):
	print(currentPos)
	amount = getTwoValues(dataList[currentPos])[0]
	time = getTwoValues(dataList[currentPos])[1]
	if amount != 0 and time != 0:
		nameOfPeople[getNameSequence(dataList[currentPos-1])]['amount'] -= (amount - amount % time)
	if time > 0 and currentPos+1 < len(dataList) and amount > 0:
		for jndex in range(currentPos+1,currentPos+time+1):
			nameOfPeople[getNameSequence(dataList[jndex])]['amount'] += (amount//time)
	currentPos += time+2
	print(nameOfPeople)


for nms in nameOfPeople:
	fout.write(str(nms['name']) + ' ' + str(nms['amount']) + '\n')

fout.close()







