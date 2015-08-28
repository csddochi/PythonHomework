__author__ = 'John'
import sqlite3
import random
import datetime
import ast

dt_now = datetime.datetime.now()
dt_delta = datetime.timedelta(minutes=1)
file_name = dt_now.strftime("%Y%m%d_DATA")
today = "20150828_DATA"

while True:
    dt_now = dt_now + dt_delta
    file_name = dt_now.strftime("%Y%m%d_DATA")
    data_time = dt_now.strftime("%Y%m%d %H:%M")

    if file_name != today:    # for a day
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

        query = "DROP TABLE IF EXISTS weather"
        self.cursor.execute(query)
        self.conn.commit()

    def select_table(self):
        query = "select * from weather" # where temp > 5000" 원하는 조건에 맞게 데이터를 가져옴
        self.cursor.execute(query)

    def fetch_all(self):
        for i in self.cursor:
            print(i)

    def create_table(self):
        query = "CREATE TABLE weather (data_date DATE, temp INT(4),humi VARCHAR(4),asto VARCHAR(4))"
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

        with open("20150828_DATA", 'r') as f:
            for line in f.readlines():
                data_list.append(line) # delete for \n -> line[:1]

        query_list = []
        for data in data_list:
            data = ast.literal_eval(data)
            # columns = ', '.join(data.keys())
            # placeholders = ', '.join('?' * len(data))
            # query = 'INSERT INTO weather ({}) VALUES ({})'.format(columns, placeholders)
            query = "INSERT INTO weather VALUES ('{data_date}', {temp}, {humi}, {asto});".format_map(data)
            query_list.append(query)
        query = '\n'.join(query_list)
        self.conn.executescript(query)
        #print(query)


if __name__ == "__main__":
    a = DBHandler("a.db")
    a.create_table()
    # query="insert into weather values ('2015-08-28 13:01', '2001', '2002', '2003')"
    # a.execute_query(query)
    a.read_data()
    a.select_table()
    a.fetch_all()

