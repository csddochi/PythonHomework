__author__ = 'John'
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class DBHandler:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def make_new_bookdb(self):
        query = "DROP TABLE IF EXISTS book"
        self.cursor.execute(query)
        self.conn.commit()

    def select_table(self):
        query = "select * from book"
        self.cursor.execute(query)

    def select_table_by_isbn(self, _isbn):
        query = "select * from book WHERE isbn={0}".format(_isbn)
        self.cursor.execute(query)

    def fetch_all(self):
        for i in self.cursor:
            print(i)

    def get_all(self):
        return self.cursor

    def create_table(self):
        query = "CREATE TABLE book (bookname VARCHAR(256), author VARCHAR(256), price INT(16), isbn INT(5))"
        self.cursor.execute(query)

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def insert_init_data(self):
        data_list = [
            {'bookname': 'Jump to Python', 'author': 'pahkey', 'price': 14000, 'isbn': 89001},
            {'bookname': 'Operating System Concept', 'author': 'Abraham', 'price': 21000, 'isbn': 89002},
            {'bookname': 'Computer Networking', 'author': 'James', 'price': 6000, 'isbn': 89003},
            {'bookname': 'File Structure', 'author': 'Sukho', 'price': 8000, 'isbn': 89003},
            {'bookname': 'Open GL', 'author': 'Woosuk', 'price': 34000, 'isbn': 89004},
            {'bookname': 'Computer Vision', 'author': 'Junghyuck', 'price': 91000, 'isbn': 89005}
        ]

        query_list = []
        for data in data_list:
            # data = ast.literal_eval(data)     # str to dic
            query = "INSERT INTO book VALUES ('{bookname}', '{author}', {price}, {isbn});".format_map(data)
            query_list.append(query)
        query = '\n'.join(query_list)
        self.conn.executescript(query)
        # print(query)

    def insert_record(self, bookname, author, price, isbn):
        data = {'bookname': bookname, 'author': author, 'price': price, 'isbn': isbn}
        query = "INSERT INTO book VALUES ('{bookname}', '{author}', {price}, {isbn});".format_map(data)
        # print(query)
        self.conn.execute(query)

    def delect_record(self, bookname, author, isbn):
        query = "DELETE FROM book WHERE bookname=\'{0}\' AND author=\'{1}\' AND isbn=\'{2}\';".format(bookname, author, isbn)
        # print(query)
        self.conn.execute(query)

    # incompleted method
    # def update_record(self, bookname, author, price, isbn):
    #     query = "".format()
    #     self.conn.execute(query)


class SimpleView(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.db = DBHandler("book.db")
        self.db.make_new_bookdb()
        self.db.create_table()
        self.db.insert_init_data()
        self.db.select_table()
        self.db.cursor = self.db.get_all()
        self.initUI()

    def initUI(self):
        self.parent.title("Book Manager")
        self.style = ttk.Style()
        self.style.theme_use("default")

        # make labels
        tk.Label(self, text="bookname").grid(row=1)
        tk.Label(self, text="author").grid(row=2)
        tk.Label(self, text="price").grid(row=3)
        tk.Label(self, text="ISBN").grid(row=4)

        # generate variables
        self.v_bookname = tk.StringVar()
        self.v_author = tk.StringVar()
        self.v_price = tk.IntVar()
        self.v_isbn = tk.IntVar()

        # initiate entry variables
        self.entry_data_bookname = ''
        self.entry_data_author = ''
        self.entry_data_price = 0
        self.entry_data_isbn = 0

        self.entry_bookname = ttk.Entry(self)
        self.entry_bookname.grid(row=1, column=1, columnspan=4, sticky=tk.W + tk.E, pady=3)
        self.entry_author = ttk.Entry(self)
        self.entry_author.grid(row=2, column=1, columnspan=4, sticky=tk.W + tk.E, pady=3)
        self.entry_price = ttk.Entry(self)
        self.entry_price.grid(row=3, column=1, columnspan=4, sticky=tk.W + tk.E, pady=3)
        self.entry_isbn = ttk.Entry(self)
        self.entry_isbn.grid(row=4, column=1, columnspan=4, sticky=tk.W + tk.E, pady=3)

        # create buttons
        ins = ttk.Button(self, text="Insert", command=lambda: self.clicked_pb('Insert'))
        ins.grid(row=5, column=0)
        dlt = ttk.Button(self, text="Delete", command=lambda: self.clicked_pb('Delete'))
        dlt.grid(row=5, column=1)
        mod = ttk.Button(self, text="Modify", command=lambda: self.clicked_pb('Modify'))
        mod.grid(row=5, column=2)

        # make listbox
        self.lb = tk.Listbox(self)

        for row in self.db.cursor:
            self.lb.insert(tk.END, row)

        self.lb.place(x=10, y=50)
        self.lb.grid(column=0, columnspan=3)

        self.pack()

    def clicked_pb(self, command):
        # type check
        try:
            if type(self.entry_bookname.get()) != str or \
                   type(self.entry_author.get()) != str or \
                   type(int(self.entry_price.get())) != int or \
                   type(int(self.entry_isbn.get())) != int:
                pass

        except ValueError:
                # warnning!
            return

        # insert command process
        if command == 'Insert':
            self.db.insert_record(self.entry_bookname.get(), self.entry_author.get(),
                                  int(self.entry_price.get()), int(self.entry_isbn.get()))
            self.db.select_table_by_isbn(self.entry_isbn.get())
            for row in self.db.cursor:
                self.lb.insert(tk.END, row)

        # delete command process
        elif command == 'Delete':
            self.db.delect_record(self.entry_bookname.get(), self.entry_author.get(), self.entry_isbn.get())
            self.lb.delete(0, tk.END)
            self.db.select_table()
            for row in self.db.cursor:
                self.lb.insert(tk.END, row)
            pass

        # modify is incompleted command
        elif command == 'Modify':
            pass

        # this part for etc
        else:
            pass


def main():
    root = tk.Tk()
    SimpleView(root)
    root.geometry("300x250+300+300")
    root.mainloop()

if __name__ == "__main__":
    main()