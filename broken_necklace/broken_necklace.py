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

nl = dataList[1]

def calculate(necklace,double):
	nr = 0 

	for c in necklace:
		if c == 'w':
			nr += 1
	if nr >= len(necklace):
		return nr
	else:

		lnl = necklace
		rnl = necklace
		if double == True:
			newnl = lnl + rnl
		else:
			newnl = necklace

		largest = 0
		for index in range(0,len(newnl)-1):
			curr = 0
			left = newnl[index]
			right = newnl[index + 1]
			p = index
			a = index + 1

			if left == 'w':
				while p >= 0 and newnl[p] == 'w':
					p -= 1

			left = newnl[p]

			if right == 'w':
				while a < len(newnl) -1 and newnl[a] == 'w':
					a += 1

			right = newnl[a]
			prev = index
			after = index + 1
			while prev >= 0 and (newnl[prev] == left or newnl[prev] == 'w'):
				curr += 1
				prev -= 1

			if index == 76:
				print(curr)

			while after <= len(newnl) - 1 and (newnl[after] == right or newnl[after] == 'w'):
				curr += 1
				after += 1

			if index == 76:
				print(curr)
			if curr >= largest:
				largest = curr

		if largest <= len(necklace):
			print('islargest')
			return largest
		else:
			return calculate(necklace,False)


fout.write(str(calculate(nl,True)) + '\n')
fout.close()
