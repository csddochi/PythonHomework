__author__ = 'John'
# this file for dummy data YYYYmmdd data, data, data
import random
import datetime
import time

dt_now = datetime.datetime.now()
dt_delta = datetime.timedelta(minutes=1)

while True:
    dt_now = dt_now + dt_delta
    file_name = dt_now.strftime("%Y%m%d_DATA")
    data_time = dt_now.strftime("%Y%m%d%H%M")

    d1 = random.randrange(0, 9999)
    d2 = random.randrange(0, 9999)
    d3 = random.randrange(0, 9999)

    data = "{0}, {1:04d}, {2:04d}, {3:04d}\n".format(data_time, d1, d2, d3)

    with open(file_name, 'a') as f:
        f.write(data)
    time.sleep(1/1000)
