#from art import *
import os
import tkinter as tk
from time import process_time
from place import Place
from multiUserInterface import MultiUserInterface as mui
from placeData import PlaceData
from personData import PersonData
class TimedPlace(Place):
    def __init__(self,master,story, callback, r,c,options,timed,actions=[],message=[]):
        super().__init__(master,story, callback, r,c,options,timed,actions,message)
        self.serverText=''
        self.currentplc=''
        self.processTime=30
    def updateTime(self):
        self.processTime-=1
        self.timeLabel.config(text='{} seconds remaining'.format(self.processTime))
        self.timeLabel.after(1000,self.updateTime)
    def timeOut(self):
        self.chooseOption([3,3])
    def renderServerData(self):
        self.serverFrame=tk.Frame(self.placeFrame, width=self.width, height=self.height, padx=5, pady=5,bg='black')
        plc=mui.getServerData(self.r,self.c)
        try:
            self.currentplc=plc[str(self.r)+','+str(self.c)]
        except:
            self.currentplc=PlaceData(**{'first':{'name':mui.userName,'score':mui.userScore},'second':{'name':'-','score':0},'third':{'name':'-','score':0},'count':1})
        print((self.currentplc.first.name,self.currentplc.first.score),(self.currentplc.second.name,self.currentplc.second.score),(self.currentplc.third.name,self.currentplc.third.score),self.currentplc.count,sep='\n',end='---\n')
        formatString = 'Leaderboard\n1. {} - {}\n2. {} - {}\n3. {} - {}\nThere are {} people in this room'
        
        if self.currentplc.count==1:
            formatString = 'Leaderboard\n1. {} - {}\n2. {} - {}\n3. {} - {}\nThere is {} person in this room'

        self.serverText=formatString.format(self.currentplc.first.name,
        self.currentplc.first.score,self.currentplc.second.name,
        self.currentplc.second.score,self.currentplc.third.name,
        self.currentplc.third.score,self.currentplc.count)
    
        self.serverLabel=tk.Label(self.serverFrame, text=self.serverText, font=("Courier", 10), fg='white', bg='black',wraplength=self.width-10,pady=10)
    def renderPlace(self):
        super().renderOnly()
        self.renderServerData()
        self.placeFrame.after(self.processTime*1000,self.timeOut)
        self.timeFrame=tk.Frame(self.placeFrame, padx=5, pady=5,bg='black')
        self.timeLabel=tk.Label(self.timeFrame, text='{} seconds remaining'.format(self.processTime), font=("Arial", 25), fg='white', bg='black',wraplength=450,pady=10)
        self.timeLabel.after(1000,self.updateTime)
        self.timeLabel.pack()
        self.timeFrame.pack(side=tk.BOTTOM)
        super().packPlace()
    