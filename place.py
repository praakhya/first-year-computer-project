#from art import *
import os
import tkinter as tk
from time import process_time
class Place():
    def __init__(self,master,story, callback, r,c,options,actions=[],message=[]):
        self.r=r
        self.c=c
        self.message=message
        self.options=options
        self.actions=actions
        self.master=master
        self.story = story
        self.callback = callback           
        self.btns=[]
        self.startTime=process_time()
    def printPic(self):
        if self.message !=None:
            for i in self.message:
                print(i)
    def chooseOption(self,loc):
        #self.clear()
        fn=getattr(self.story, self.callback)
        fn(loc,process_time()-self.startTime)
        #return loc
    def showOptions(self):
        print(self.options)   
    def renderPlace(self):
        #self.showOptions()
        self.lblFrame=tk.Frame(self.master, padx=5, pady=5,bg='black')
        self.btnFrame=tk.Frame(self.master, padx=5, pady=5,bg='black')
        tk.Label(self.lblFrame, text=self.message, fg='white', bg='black',wraplength=450,pady=10).pack(side="top")
        for ch in self.options:
            self.btns.append(tk.Button(self.btnFrame, text=ch, fg="white", bg="black", padx=5, pady=5,highlightbackground="white", highlightthickness=0.5, command = lambda l=self.options[ch]: self.chooseOption(l)))
            self.btns[-1].pack()
        self.lblFrame.pack()
        self.btnFrame.pack()
        activeTime=process_time()-self.startTime
        #print(activeTime)
        if activeTime>=0.30:
            print('OUT')
            #self.chooseOption([1,3])
        else:
            print('IN')
    def clear(self):
        self.lblFrame.destroy()
        self.btnFrame.destroy()