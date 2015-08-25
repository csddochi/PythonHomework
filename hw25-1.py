__author__ = 'John'
# generate lottery numbers
import random


def gen_numbers():
    num = list(range(1, 46))
    return random.sample(num, 6)

con = 'yes'
while con == 'yes' or con == 'y':
    print(gen_numbers())
    print('Do you want to continue? (yes or no)')
    con = input()
