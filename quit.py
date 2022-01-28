from tkinter import *
class Quit():
    def __init__(self,play):
        self.master=Tk()
        self.master.title('Quit')
        self.msg=Label(self.master, text='Are you sure you want to quit?')
        self.yes=Button(self.master, text='Yes', command=self.quit)
        self.no=Button(self.master, text='No', command=self.delSelf)
        self.play=play
    def show(self):
        self.msg.grid(row=0)
        self.yes.grid(row=1, column=0)
        self.no.grid(row=1,column=1)
        self.master.mainloop()
    def quit(self):
        self.play.master.destroy()
        self.delSelf()
    def delSelf(self):
        self.master.destroy()