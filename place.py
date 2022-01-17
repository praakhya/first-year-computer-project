from art import *
import os
class Place():
    def __init__(self,r,c,options,actions=[],message=[]):
        self.r=r
        self.c=c
        self.message=message
        self.options=options
        self.actions=actions
    def printPic(self):
        if self.pic != None:
            for i in self.pic:
                print(text2art(i))
        if self.message !=None:
            for i in self.message:
                print(i)
    def renderPlace(self):
        os.system('cls')
        #self.printPic()
        os.system("cls")
        for i in self.message:
            print(i)
        print('-'*50)
    def chooseOption(self,ch):
        if ch is not None:
            if ch in self.options:
                return self.options[ch]
            elif ch in self.actions:
                return self.actions[ch]
            elif ch.lower() in ['q','quit']:
                return False
            else:
                return []
        else:
            return []
            
            
