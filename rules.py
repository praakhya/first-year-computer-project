from tkinter import *
class Rules():
    def __init__(self,play):
        self.play=play
        self.master=Tk()
        self.master.title('Rules')
        #self.master.geometry('200x100')
        self.master.configure(bg='black')
        self.ruleTxt="""In this game you can make you own
        story. All you have to do is read each prompt and make a choice.
        Enjoy!"""
        self.lblRule=Label(self.master, text=self.ruleTxt, fg='white', bg='black', wraplength=160)
        self.btnClose=Button(self.master, text='Close', fg='white', bg='black',highlightbackground='black', highlightthickness=0.5, wraplength=80, command=self.closeRules)
    def run(self):
        self.lblRule.pack(side='top',fill=BOTH, expand=True)
        self.btnClose.pack(side='bottom',expand=True)
        self.master.mainloop()    
    def closeRules(self):
        self.master.destroy()
        #self.play.render
