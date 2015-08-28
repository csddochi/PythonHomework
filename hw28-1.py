__author__ = 'John'
import sqlite3
import random
import datetime

dt_now = datetime.datetime.now()
dt_delta = datetime.timedelta(minutes=1)
file_name = dt_now.strftime("%Y%m%d_DATA")

while True:
    dt_now = dt_now + dt_delta
    file_name = dt_now.strftime("%Y%m%d_DATA")
    data_time = dt_now.strftime("%Y%m%d %H:%M")

    if file_name != "20150828_DATA":    # for a day
        break

    d1 = random.randrange(0, 9999)
    d2 = random.randrange(0, 9999)
    d3 = random.randrange(0, 9999)

    data = "'data_date': '{0}', 'temp': {1:4d}, 'humi': {2:4d}, 'asto': {3:4d}".format(data_time, d1, d2, d3)
    data = '{' + data + '}\n'
    with open(file_name, "a") as f:
        f.write(data)


class DBHandler:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.db_file = db_file
        query = "DROP TABLE IF EXISTS " + db_file
        self.cursor.execute(query)
        self.conn.commit()

    def create_table(self):
        query = "CREATE TABLE " + self.db_file + "(data_date DATE,temp VARCHAR(4),humi VARCHAR(4),asto VARCHAR(4))"
        self.cursor.execute(query)

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def read_data(self):
        data_list = [
            # {'data_date': '2015-08-28 13:01', 'temp': '2001', 'humi': '2002', 'asto': '2003'},
            # {'data_date': '2015-08-28 13:02', 'temp': '2004', 'humi': '2005', 'asto': '2006'},
            # {'data_date': '2015-08-28 13:03', 'temp': '2007', 'humi': '2008', 'asto': '2009'},
            # {'data_date': '2015-08-28 13:04', 'temp': '2010', 'humi': '2011', 'asto': '2012'}
        ]

        with open(file_name, 'r') as f:
            for line in f.readlines():
                data_list.append(line) # delete for \n -> line[:1]

        query_list = []
        for data in data_list:
            query = "INSERT INTO " + self.db_file +" VALUES ('{data_date}', {temp}, {humi}, {asto});".format_map(data)
            query_list.append(query)
        query = '\n'.join(query_list)
        print(query)


a = DBHandler("a.db")
a.create_table()


