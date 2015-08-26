# 20133246 Soryung Lee
# 3 by 3 multiplication table program

L = range(1, 10)

for x in L[1::3]:
	for y in L:
		for z in range(0, 2):
			print('{0} X {1} = {2}'.format(x, y, x*y), end='\t')
			x = x + 1
		
		if x < 10:
			print('{0} X {1} = {2}'.format(x, y, x*y))
		else:
			print()
		x = x - 2
	print()
	


