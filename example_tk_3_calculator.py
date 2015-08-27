__author__ = 'John'
import tkinter as tk
import tkinter.ttk as ttk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.v = tk.StringVar()
        self.entry_data = ''

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, columnspan=4, sticky=tk.W + tk.E)
        cls = ttk.Button(self, text="Cls", command=lambda: self.clicked_pb('Cls'))
        cls.grid(row=1, column=0)
        bck = ttk.Button(self, text="Back", command=lambda: self.clicked_pb('Back'))
        bck.grid(row=1, column=1)
        chi = ttk.Button(self, text="Int", command=lambda: self.clicked_pb('Int'))
        chi.grid(row=1, column=2)
        clo = ttk.Button(self, text="Close", command=lambda: self.clicked_pb('Close'))
        clo.grid(row=1, column=3)
        pb_7 = ttk.Button(self, text="7", command=lambda: self.clicked_pb(7))
        pb_7.grid(row=2, column=0)
        pb_8 = ttk.Button(self, text="8", command=lambda: self.clicked_pb(8))
        pb_8.grid(row=2, column=1)
        pb_9 = ttk.Button(self, text="9", command=lambda: self.clicked_pb(9))
        pb_9.grid(row=2, column=2)
        div = ttk.Button(self, text="/", command=lambda: self.clicked_pb('/'))
        div.grid(row=2, column=3)

        pb_4 = ttk.Button(self, text="4", command=lambda: self.clicked_pb(4))
        pb_4.grid(row=3, column=0)
        pb_5 = ttk.Button(self, text="5", command=lambda: self.clicked_pb(5))
        pb_5.grid(row=3, column=1)
        pb_6 = ttk.Button(self, text="6", command=lambda: self.clicked_pb(6))
        pb_6.grid(row=3, column=2)
        mul = ttk.Button(self, text="*", command=lambda: self.clicked_pb('*'))
        mul.grid(row=3, column=3)

        pb_1 = ttk.Button(self, text="1", command=lambda: self.clicked_pb(1))
        pb_1.grid(row=4, column=0)
        pb_2 = ttk.Button(self, text="2", command=lambda: self.clicked_pb(2))
        pb_2.grid(row=4, column=1)
        pb_3 = ttk.Button(self, text="3", command=lambda: self.clicked_pb(3))
        pb_3.grid(row=4, column=2)
        mns = ttk.Button(self, text="-", command=lambda: self.clicked_pb('-'))
        mns.grid(row=4, column=3)

        pb_0 = ttk.Button(self, text="0", command=lambda: self.clicked_pb(0))
        pb_0.grid(row=5, column=0)
        dot = ttk.Button(self, text=".", command=lambda: self.clicked_pb('.'))
        dot.grid(row=5, column=1)

        equ = ttk.Button(self, text="=", command=lambda: self.clicked_pb('='))
        equ.grid(row=5, column=2)
        pls = ttk.Button(self, text="+", command=lambda: self.clicked_pb('+'))
        pls.grid(row=5, column=3)

        self.pack()

    def clicked_pb(self, data):
        if data == '=':
            try:
                self.entry_data = eval(self.entry_data)
                self.entry_data = str(self.entry_data)
            except ZeroDivisionError:
                self.entry_data = self.entry_data[:1]
            except:
                self.entry_data = ''

        elif data == 'Cls':
            self.entry_data = ''

        elif data == 'Back':
            self.entry_data = self.entry_data[:1]

        elif data == 'Close':
            exit()

        elif data == 'Int':
            try:
                self.entry_data = '{0:.0f}'.format(float(self.entry_data))
            except:
                pass
        else:
            self.entry_data += str(data)

        self.v.set(self.entry_data)
        self.entry.config(textvariable=self.v)


def main():
    root = tk.Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
