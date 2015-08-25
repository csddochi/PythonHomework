__author__ = 'John'
# generate lottery numbers
import random


def lottery():
    s = set()

    while s.__len__() < 6:
        num = random.randint(1, 46)
        s.add(num)

    return s


con = 'yes'
while con == 'yes' or con == 'y':
    print(lottery())
    print('Do you want to continue? (yes or no)')
    con = input()
