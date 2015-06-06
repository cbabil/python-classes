from tkinter import *

ALL = N + S + W + E


class Application(Frame):

    def __init__(self, master=None):
        def handler1(event):
            print("Frame 1 X: ", event.x, " Y: ", event.y)

        def handler2(event):
            print("Frame 2 X: ", event.x, " Y: ", event.y)

        def handler_open():
            fn = entry.get()
            f = open(fn, "r")
            filetext = f.read()
            text.insert(END, filetext)

        def handler_red():
            text.config(fg="red")

        def handler_blue():
            text.config(fg="blue")

        def handler_green():
            text.config(fg="green")

        def handler_black():
            text.config(fg="black")

        # Main Frame
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)

        # Frame 1
        f1 = Frame(self, bg="red")
        f1.grid(row=0, column=0, rowspan=3, columnspan=4, sticky=ALL)
        f1.bind("<Button-1>", handler1)

        # Frame 2
        f2 = Frame(self, bg="green")
        f2.grid(row=3, column=0, rowspan=3, columnspan=4, sticky=ALL)
        f2.bind("<Button-1>", handler2)

        # Frame 3
        f3 = Frame(self, bg="blue")
        f3.grid(row=0, column=4, rowspan=6, columnspan=6, sticky=ALL)
        entry = Entry(f3, bg="blue")
        entry.insert(0, "Enter filename:")
        entry.pack(fill=BOTH)

        # Textbox
        text = Text(f3, bg="blue", height=10, width=15)
        text.pack(fill=BOTH)

        # Buttons
        self.columnconfigure(0, weight=1)
        Button(self, text="Red", command=handler_red).grid(
            row=6, column=0, sticky=E + W)
        self.columnconfigure(2, weight=1)
        Button(self, text="Blue", command=handler_blue).grid(
            row=6, column=2, sticky=E + W)
        self.columnconfigure(4, weight=1)
        Button(self, text="Green", command=handler_green).grid(
            row=6, column=4, sticky=E + W)
        self.columnconfigure(6, weight=1)
        Button(self, text="Black", command=handler_black).grid(
            row=6, column=6, sticky=E + W)
        self.columnconfigure(8, weight=1)
        Button(self, text="Open", command=handler_open).grid(
            row=6, column=8, sticky=E + W)

root = Tk()
app = Application(master=root)
app.mainloop()
