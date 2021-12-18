from place import Place
import map
from colorama import Fore, Back, Style
from termcolor import colored, cprint     # For Termcolor
from noPathExcept import NoPathException
class Play():
    def __init__(self,map):
        self.map=map
        self.currposr=0
        self.currposc=0
        self.running=True
    def run(self):
        self.printMap()
        self.place=self.map[self.currposr][self.currposc]
        self.place.printPic()
        while self.running==True:
            key=input().lower()
            try:
                returnval=self.handleKeys(key)
                if returnval:
                    self.place=self.map[self.currposr][self.currposc]
                    self.place.printPic()
                else:
                    print(colored('quitting', 'yellow', 'on_red', attrs=['blink', 'bold']))
            except NoPathException:
                print(colored("Path not available", 'yellow', 'on_red', attrs=['blink', 'bold']))

            
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
            return False

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
    def printMap(self):
        i=len(self.map)
        j=len(self.map[0])
        for row in range(i):
            for col in range(j):
                if self.map[row][col]!=0:
                    print('X',end=' ')
                else:
                    print(' ', end=' ')
            print()
map=map.populate("places.json")
p1=Play(map)
p1.run()    