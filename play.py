from rules import Rules #
from stories import Stories
from quit import Quit
import os, time
from tkinter import *
from gameStyle import GameStyle as gs
class Play():
    def __init__(self):
        self.master=Tk()
        self.masterW='500'
        self.masterH='500'
        self.master.geometry(self.masterW+'x'+self.masterH)
        self.master.configure(bg='black')
        self.btnStyle=gs.getStyle()
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
        storyFr=Frame(self.master, width=self.masterW, height=self.masterH, padx=10, pady=10, bg='black')
        for story in listStories:
            b=Button(storyFr,text=story.rstrip('.json'),highlightthickness=0.5,command=lambda s=story, sfr=storyFr: self.getStory(s,sfr),pady=5)
            b.config(**self.btnStyle)
            b.pack()
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
        self.btnFrame=Frame(self.mFrame, padx=5,pady=10,bg='black')
        self.playB=Button(self.btnFrame,text='Play',command=self.choose,pady=10)
        self.ruleB=Button(self.btnFrame,text='Rules',highlightthickness=0.5,command=self.rules,pady=10)
        self.quitB=Button(self.btnFrame,text='Quit',highlightthickness=0.5,command=self.quit,pady=10)
        self.lhead=Label(self.lblFrame, text='Text a Story',font=('Courier 30 underline'),fg='white',bg='black')
        self.lsub=Label(self.lblFrame, text='Choose an option to continue:-',font=('Courier 14'),fg='white',bg='black',pady=5)
        for frame in self.mFrame.winfo_children():
            for widget in frame.winfo_children():
                if widget.winfo_class()=='Button':
                    widget.config(**self.btnStyle)
                widget.pack()
            frame.pack()
        self.mFrame.pack()
        
p1=Play()
p1.run()   
