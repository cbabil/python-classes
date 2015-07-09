from tkinter import *

class Application(Frame):
    ''' Application Main window class '''
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        ''' Add all widgets to main frame '''
        top_frame = Frame(self)
        self.text_in1 = Entry(top_frame)
        self.text_in2 = Entry(top_frame)
        self.text_in1.pack()
        self.text_in2.pack()
        
        self.handleb = Button(top_frame, text="Sum", command=self.handle)
        self.handleb.pack(side=LEFT)
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.label = Label(bottom_frame, text="Output Sum")
        self.label.pack()
        
    def handle(self):
        ''' Handle a click of the button '''
        try:
            float1 = float(self.text_in1.get())
            float2 = float(self.text_in2.get())
            output = float1 + float2
        except:
            output = "***ERROR***"
        self.label.config(text=output)    
    
root = Tk()
app = Application(master=root)
app.mainloop()