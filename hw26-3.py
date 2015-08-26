__author__ = 'John'
# myclient.py for client
import random
import time
# -*- coding: utf-8 -*-
from socket import *
for x in range(1, 22):
    svrSock = socket(AF_INET, SOCK_STREAM)
    svrSock.connect(('127.0.0.1', 12000))
    s = '{0:04d}'.format(random.randrange(0, 9999))
    svrSock.send(s.encode())
    time.sleep(random.randint(5, 10) * 0.1)
