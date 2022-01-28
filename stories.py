from place import Place
import time, os
import tkinter as tk
import json
class Stories():
    def __init__(self, name, play, master):
        print('init stories')
        self.curr_r=0
        self.curr_c=0
        self.master=master
        self.master.title(name.rstrip('.json'))
        self.map=self.populate('stories/'+name)
        self.play=play
    def run(self):
        self.printMap()
        self.currentPlace().renderPlace()
        ch=input('>>> ')
        quit()
    def btnClick(self,loc):
        self.currentPlace().clear()
        if loc==[-1,-1]:
            self.play.render()
        else:
            self.curr_r, self.curr_c=loc
            self.currentPlace().renderPlace()
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
            p = Place(self.master,self,"btnClick",**datalist[i])
            print('2')
            places.append(p)
            print('3')
            if p.r > maxr:
                maxr = p.r
            print('4')
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
        print('='*(j+3)) 
        print(format("Map", " ^"+str(j+3)))
        print('-'*(j+3))
        for row in range(i):
            for col in range(j):
                if self.map[row][col]!=0:
                    print('X',end=' ')
                else:
                    print(' ', end=' ')
            print()
        
        print('='*(j+3))
    def currentPlace(self):
        return self.map[self.curr_r][self.curr_c] 