# 20133246 Soryung Lee
# book management system

print('Welcome to Book Management System')
print('First, read existing book lists.')

try:
	f = open('book.txt', 'r')
	data = f.read()
	print(data)
	f.close()
except IOError:
	print('There is not any files.')

f = open('book.txt', 'a')

con = 'yes'
print('And, then, write book information you want to add.')
while con == 'yes' or con == 'y':
	memo = "['"
	memo += input('book name> ')
	memo += "', '" + input('author> ') 
	memo += "', " + input('price> ')
	memo += ']' + '\n'
	f.write(memo)
	print('Do you want to continue? (yes or no)')
	con = input()

# memo = "['Jump to Python', 'pahkey', 14000]" + "\n"
# f.write(memo)

# memo = "['Operating System Concept', 'Abraham', 20000]" + "\n"
# f.write(memo)

# memo = "['Computer Networking', 'James', 34000]" + "\n"
# f.write(memo)

f.close()