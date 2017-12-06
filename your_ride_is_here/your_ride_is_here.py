"""
ID: duweira1
LANG: PYTHON2
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
finalString = ''

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('ride.in') as fin:
    inputList = fin.read().splitlines()

firstNumberList = []
secondNumberList = []


for char in inputList[0]:
	for position in range(0,25):
		if char == letter[position]:
			firstNumberList.append(position+1)

for char in inputList[1]:
	for position in range(0,25):
		if char == letter[position]:
			secondNumberList.append(position+1)


print(firstNumberList)
print(secondNumberList)


firstProduct = 1
secondProduct = 1

for num in firstNumberList:
	firstProduct *= num

for num in secondNumberList:
	secondProduct *= num



if firstProduct % 47 == secondProduct % 47:
	finalString = 'GO'
else:
	finalString = 'STAY'


fout.write(finalString + '\n')
fout.close()
