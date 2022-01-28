#from art import *
import os
import tkinter as tk
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
        print("STORY/CALLBACK", story, callback)

    def printPic(self):
        #if self.pic != None:
            #for i in self.pic:
                #print(text2art(i))
        if self.message !=None:
            for i in self.message:
                print(i)
    def chooseOption(self,loc):
        print(loc)
        print('returning to stories')
        self.clear()
        return loc
        '''
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
        '''
    def renderPlace(self):
        #self.printPic()
        msg=''
        '''
        for i in self.message:
            print(i)
            msg+=i+'\n'
        msg+='-'*50+'\n'
        print('-'*50)
        '''
        self.lblFrame=tk.Frame(self.master, padx=5, pady=5,bg='black')
        self.btnFrame=tk.Frame(self.master, padx=5, pady=5,bg='black')
        print(msg)
        tk.Label(self.lblFrame, text=self.message, fg='white', bg='black',wraplength=450,pady=10).pack(side="top")
        print("OPTIONS", self.options)
        for ch in self.options:
            tk.Button(self.btnFrame, text=ch, fg="white", bg="black", padx=5, pady=5,highlightbackground="white", highlightthickness=0.5, command = lambda: getattr(self.story, self.callback)(self.options[ch])).pack()
        self.lblFrame.pack()
        self.btnFrame.pack()
        #self.master.mainloop()
        print('label mainllop')
    def clear(self):
        self.lblFrame.destroy()
        self.btnFrame.destroy()
    
    
            
            
