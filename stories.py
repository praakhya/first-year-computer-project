from timedPlace import TimedPlace as TPlace
from place import Place
import time, os
import tkinter as tk
import json
from readJson import read
from multiUserInterface import MultiUserInterface as mui

class Stories():
    def __init__(self, name, play, master):
        self.curr_r=0
        self.curr_c=0
        self.master=master
        self.master.title(name.rstrip('.json'))
        self.map=self.populate('stories/'+name)
        self.play=play
    def run(self):
        self.printMap()
        self.currentPlace().renderPlace()
        #ch=input('>>> ')
        #quit()
    def btnClick(self,loc):
        #print(loc)
        self.currentPlace().clear()
        #print(time)
        if loc==[-1,-1]:
            self.play.render()
        else:
            #if time>=0.30:
            self.curr_r, self.curr_c=[3,3]
            #else:
            self.curr_r, self.curr_c=loc
            self.currentPlace().renderPlace()
            self.master.update()

    def populate(self,fname):
        places = []
        maxr=0
        maxc=0
        map=[]
        datalist=read(fname)
        for i in range(len(datalist)):
            if datalist[i]['timed']==True:
                p = TPlace(self.master,self,"btnClick",**datalist[i])
            else:
                p = Place(self.master,self,"btnClick",**datalist[i])
            places.append(p)
            if p.r > maxr:
                maxr = p.r
            if p.c > maxc:
                maxc = p.c
        maxr+=1;maxc+=1
        for i in range(maxr):
            map.append([])
            for j in range(maxc):
                map[i].append(0)
        for place in places:
            i=place.r
            j=place.c
            map[i][j]=place
        return map
    def printMap(self):
        i=len(self.map)
        j=len(self.map[0])
        header="Map: Places to Go..."
        if j>len(header):
            n=j
        else:
            n=len(header)
        n+=4
        print('='*(n)) 
        print(format(header, " ^"+str(n)))
        print('-'*(n))
        for row in range(i):
            rowi=''
            for col in range(j):
                if self.map[row][col]!=0:
                    rowi+='X'
                else:
                    rowi+=' '
            print(format(rowi, " ^"+str(n)))
        
        print('='*(n))
    def currentPlace(self):
        return self.map[self.curr_r][self.curr_c] 