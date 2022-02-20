#from art import *
import os
import tkinter as tk
from time import process_time
from place import Place
class TimedPlace(Place):
    def __init__(self,master,story, callback, r,c,options,timed,actions=[],message=[]):
        super().__init__(master,story, callback, r,c,options,timed,actions,message)
        self.processTime=30
    def updateTime(self):
        self.processTime-=1
        self.timeLabel.config(text='{} seconds remaining'.format(self.processTime))
        self.timeLabel.after(1000,self.updateTime)
    def timeOut(self):
        self.chooseOption([3,3])  
    def renderPlace(self):
        super().renderOnly()
        self.placeFrame.after(self.processTime*1000,self.timeOut)
        self.timeFrame=tk.Frame(self.placeFrame, padx=5, pady=5,bg='black')
        self.timeLabel=tk.Label(self.timeFrame, text='{} seconds remaining'.format(self.processTime), font=("Arial", 25), fg='white', bg='black',wraplength=450,pady=10)
        self.timeLabel.after(1000,self.updateTime)
        self.timeLabel.pack()
        self.timeFrame.pack(side=tk.BOTTOM)
        super().packPlace()