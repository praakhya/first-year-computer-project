from rules import Rules
from stories import Stories
from quit import Quit
import os, time
from tkinter import *

class Play():
    def __init__(self):
        self.master=Tk()
        self.master.geometry('500x500')
        self.master.configure(bg='black')
        self.render()
        self.story=None
    def run(self):
        self.master.mainloop()
    def getStory(self,sname, sframe):
        self.story=Stories(sname,self,self.master)
        sframe.destroy()
        self.story.run()   
    def choose(self):
        listStories=os.listdir('stories')
        storyFr=Frame(self.master, padx=10, pady=10, bg='black')
        for story in listStories:
            Button(storyFr,text=story.rstrip('.json'),bg='black',fg='white',highlightbackground='white',highlightthickness=0.5,command=lambda s=story, sfr=storyFr: self.getStory(s,sfr),pady=5).pack()
        self.mFrame.destroy()
        storyFr.pack()

    def rules(self):
        r=Rules(self).run()
    def quit(self):
        q=Quit(self).show()
    
    def render(self):
        self.master.title('Text Game')
        self.mFrame=Frame(self.master, padx=5,pady=5,bg='black')
        self.lblFrame=Frame(self.mFrame, padx=5,pady=5,bg='black')
        self.btnFrame=Frame(self.mFrame, padx=5,pady=5,bg='black')
        self.playB=Button(self.btnFrame,text='Play',bg='black',fg='white',highlightbackground='white',highlightthickness=0.5,command=self.choose,pady=5)
        self.ruleB=Button(self.btnFrame,text='Rules',bg='black',fg='white',highlightbackground='white',highlightthickness=0.5,command=self.rules,pady=5)
        self.quitB=Button(self.btnFrame,text='Quit',bg='black',fg='white',highlightbackground='white',highlightthickness=0.5,command=self.quit,pady=5)
        self.lhead=Label(self.lblFrame, text='Text a Story',font=('Courier 30 underline'),fg='white',bg='black')
        self.lsub=Label(self.lblFrame, text='Choose an option to continue:-',font=('Courier 14'),fg='white',bg='black',pady=5)
        for frame in self.mFrame.winfo_children():
            for widget in frame.winfo_children():
                widget.pack()
            frame.pack()
        self.mFrame.pack()
    
p1=Play()
p1.run()    