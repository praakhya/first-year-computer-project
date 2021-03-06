import tkinter as tk
from time import process_time
from gameStyle import GameStyle as gs
class Place():
    def __init__(self,master,story, callback, r,c,options,timed,actions=[],message=[]):
        self.r=r
        self.c=c
        self.message=message
        self.options=options
        self.actions=actions
        self.master=master
        self.story = story
        self.callback = callback   
        self.timed=timed        
        self.btns=[]
        self.btnStyle=gs.getStyle()
        self.width=self.master.winfo_width()
        self.height=self.master.winfo_height()
        self.score=0
        
    def chooseOption(self,loc):
        fn=getattr(self.story, self.callback)
        fn(loc,self.score)  
    def packPlace(self):
        for frame in self.placeFrame.winfo_children():
            for widget in frame.winfo_children():
                if widget.winfo_class()=='Button':
                    widget.config(self.btnStyle)
                widget.pack()
            frame.pack()
        self.placeFrame.pack()
    def renderOnly(self,score):
        self.score=score
        self.placeFrame=tk.Frame(self.master, width=self.width, height=self.height, padx=5, pady=5,bg='black')
        self.placeFrame.pack(expand=True, fill='both')
        self.placeFrame.pack_propagate(0)
        self.lblFrame=tk.Frame(self.placeFrame, padx=5, pady=5,bg='black')
        self.btnFrame=tk.Frame(self.placeFrame, padx=5, pady=5,bg='black')
        self.msgLabel=tk.Label(self.lblFrame, text=self.message, font=("Courier", 10), fg='white', bg='black',wraplength=self.width-10,pady=10).pack(side="top")
        for ch in self.options:
            self.btns.append(tk.Button(self.btnFrame, text=ch, padx=5, pady=5, highlightthickness=0.5, wraplength=self.width-10,command = lambda l=self.options[ch]: self.chooseOption(l)))
    def renderPlace(self,score):
        self.renderOnly(score)
        self.packPlace()
    def clear(self):
        self.placeFrame.destroy()