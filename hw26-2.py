__author__ = 'John'
# this file for make one file merging dummy data
import glob
L = list(glob.glob("*DATA"))

data = ''

for i in range(0, len(L)):
    with open(L[i], 'r+') as f:
        data += f.read() + '\n'

with open('alldat', 'w') as f:
    f.write(data)
