from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for r in range(6):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0, sticky=ALL)
        self.rowconfigure(6, weight=0)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=6, column=c, sticky=E+W)
        f1 = Frame(self, bg="red")
        f1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)
        f2 = Frame(self, bg="green")
        f2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=ALL)
        f3 = Frame(self, bg="blue")
        f3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=ALL)
root = Tk()
app = Application(master=root)                
app.mainloop()