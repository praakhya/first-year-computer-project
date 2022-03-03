from timedPlace import TimedPlace as TPlace
from controlPlace import ControlPlace as CPlace
from place import Place
import time, os
import tkinter as tk
import json
class Stories():
    def __init__(self, name, play, master):
        self.curr_r=0
        self.curr_c=0
        self.master=master
        self.master.title(name.rstrip('.json'))
        self.map=self.populate('stories/'+name)
        self.play=play
        self.score=0
    def run(self):
        self.printMap()
        self.currentPlace().renderPlace(self.score)
    def btnClick(self,loc,score):
        self.score=score
        self.currentPlace().clear()
        if loc==[-1,-1]:
            self.play.render()
        else:
            self.curr_r, self.curr_c=loc
            if loc==[-2,-2] or loc==[0,0]:
                self.score=0
            self.currentPlace().renderPlace(self.score)
            self.master.update()

    def populate(self,fname):
        places = []
        maxr=0
        maxc=0
        map=[]
        with open(fname,'r') as plcdat:
            data=plcdat.read()
        datalist=json.loads(data)
        for i in range(len(datalist)):
            if datalist[i]['timed']==True:
                p = TPlace(self.master,self,"btnClick",**datalist[i])
            else:
                p = CPlace(self.master,self,"btnClick",**datalist[i])
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