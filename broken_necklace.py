"""
ID: duweira1
LANG: PYTHON2
TASK: beads

"""

fin = open('beads.in','r')
fout = open('beads.out','w')


dataList = []
with open('beads.in') as f:
	dataList = (f.read().splitlines())

def calculate(necklace):
	largest = 0
	for index in range(0,len(necklace)-1):
		curr = 0
		left = necklace[index]
		right = necklace[index + 1]
		prev = index
		after = index + 1
		while prev >= 0 and necklace[prev] == left:
			curr += 1
			prev -= 1

		while after <= len(necklace) - 1 and necklace[after] == right:
			curr += 1
			after += 1

		if curr >= largest:
			largest = curr

	return largest
