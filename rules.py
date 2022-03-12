from tkinter import *
from gameStyle import GameStyle as gs
class Rules():
    def __init__(self,play):
        self.play=play
        self.master=Tk()
        self.master.title('Rules')
        self.master.configure(bg='black')
        self.master.geometry('200x300')
        self.ruleTxt="""
        In this game you can make you own
        story. All you have to do is read each prompt and make a choice.
        Enjoy!
        """
        self.scrTxt="""
Score Calculation:-
score after each prompt = time left after selecting an option x 15
        """
        self.lblRule=Label(self.master, text=self.ruleTxt, fg='white', bg='black', wraplength=160)
        self.lblScore=Label(self.master, text=self.scrTxt, fg='white', bg='black', wraplength=160)
        self.btnClose=Button(self.master, text='Close', fg='white', bg='black',highlightbackground='black', highlightthickness=0.5, wraplength=80, command=self.closeRules)
        self.btnClose.config(gs.getStyle())
    def run(self):
        self.lblRule.pack(side='top',fill=BOTH, expand=True)
        self.lblScore.pack(side='top',fill=BOTH, expand=True)
        self.btnClose.pack(side='bottom',expand=True)
        self.master.grab_set_global()
        self.master.mainloop()    
    def closeRules(self):
        self.master.grab_release()
        self.master.destroy()
