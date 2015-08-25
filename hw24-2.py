# 20133246 Soryung Lee
# draw diamond shape and I/O

try:
	f = open('diamond.txt', 'r')
	data = f.read()
	print(data)
	f.close()
except IOError:
	print('There is not any files.')

f = open('diamond.txt', 'w')
diamond = ''

print('Please, input one natural number.')
integer = input('number> ')
dNumber = 2 * int(integer) + 1

integer = int(integer)

for x in range(0, integer):
	for y in range(0, integer + 1):
		if (x + y) >= integer:
			print('*', sep='', end='')
			diamond +='*'
		else:
			print(' ', sep='', end='')
			diamond +=' '

	for y in range(integer, dNumber):
		if (y - x) < integer:
			print('*', sep='', end='')
			diamond +='*'
		else:
			print(' ', sep='', end='')
			diamond +=' '
	print()
	diamond += '\n'

for x in range(0, dNumber):
	print('*', sep='', end='')
	diamond +='*'
print()
diamond += '\n'

for x in range(integer + 1, dNumber):
	for y in range(0, integer):
		if (x - y) > integer:
			print(' ', sep='', end='')
			diamond +=' '
		else:
			print('*', sep='', end='')
			diamond +='*'

	for y in range(integer, dNumber):
		if (x + y) < (dNumber + integer):
			print('*', sep='', end='')
			diamond +='*'
		else:
			print(' ', sep='', end='')
			diamond +=' '
	print()
	diamond += '\n'

f.write(diamond)
f.close()