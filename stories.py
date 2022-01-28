import map
#from termcolor import colored
from myExceptions import *
from place import Place
import time, os
import tkinter as tk
class Stories():
    def __init__(self, name, master):
        print('init stories')
        self.curr_r=0
        self.curr_c=0
        self.running=True
        self.master=master
        self.map=map.populate(self.master,'stories/'+name)
        self.currPlace=self.currentPlace()
    def run(self):
        self.printMap()
        #self.master.mainloop()
        print('in stories object')
        while self.running:
            print('new run loop')
            self.currPlace.renderPlace()
            if (self.curr_r==len(self.map)-1) and (self.curr_c==len(self.map[0])-1):
                self.running=False
                break
            ch=input('>>> ')
            chosen=self.currPlace.chooseOption(ch)
            #if chosen==[]:
            #    print('--> Option/Interaction invalid! <--')
            #    os.system('cls')
            #elif chosen==False:
            #    self.running=False
            #    break
            #else:
            try:
                self.curr_r,self.curr_c=int(chosen[0]), int(chosen[1])
                self.currPlace=self.currentPlace()
            except:
                print(chosen)
        quit()
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
        for i in self.map:
            for j in i:
                if j!=0:
                    if j.r==self.curr_r and j.c==self.curr_c:
                        opt=j.options
                        act=j.actions
                        message=j.message
                        return Place(self.master,self.curr_r, self.curr_c, opt, act,message)
'''        
try:
    pass        
except NoPathException:
    print(colored("Path not available", 'yellow', 'on_red', attrs=['blink', 'bold']))
except InvalidCommandException:
    print(colored("Invalid Command", 'yellow', 'on_red', attrs=['blink', 'bold']))
def handleKeys(self,key):
        if key=='left':
            return self.moveLeft()
        elif key=='right':
            return self.moveRight()
        elif key=='back':
            return self.moveDown()
        elif key=='ahead':
            return self.moveUp()
        elif key=='q' or key=='quit':
            self.running=False
            return False
        else:
            raise InvalidCommandException 

def moveLeft(self):
    oldc=self.currposc
    self.currposc-=1
    if (self.currposc<0) or (self.map[self.currposr][self.currposc]==0):
        self.currposc=oldc
        raise NoPathException
    return True

def moveRight(self):
    oldc=self.currposc
    self.currposc+=1
    if (self.currposc>len(self.map[0])-1) or (self.map[self.currposr][self.currposc]==0):
        self.currposc=oldc
        raise NoPathException
    return True            
def moveUp(self):
    oldr=self.currposr
    self.currposr-=1
    if (self.currposr<0) or (self.map[self.currposr][self.currposc]==0):
        self.currposr=oldr
        raise NoPathException
    return True
def moveDown(self):
    oldr=self.currposr
    self.currposr+=1
    if (self.currposr>len(self.map)-1) or (self.map[self.currposr][self.currposc]==0):
        self.currposr=oldr
        raise NoPathException
    return True
'''