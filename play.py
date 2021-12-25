from place import Place
import map
import home
from art import *
from termcolor import colored, cprint     # For Termcolor
from myExceptions import NoPathException, InvalidCommandException
from stories import Stories
import os
class Play():
    def __init__(self):
        self.running=True
        self.key=None
    def run(self):
        while self.running:
            self.key=home.runHome()
            listStories=os.listdir('stories')
            if self.key.lower() in ('p','play'):
                print('     -- Choose a Story --')
                for i in range(len(listStories)):
                    print('\t',i+1,'.',listStories[i].rstrip('.json'))
                ch=int(input('>>> '))
                if ch<=len(listStories):
                    story=Stories(listStories[ch-1])
                    story.run()
                else:
                    print('--> Story not available! <--') 
            elif self.key.lower() in ('rules', 'r'):
                self.key=home.runRules()
            elif self.key.lower()=='back':
                self.key=home.runHome()
            elif self.key.lower() in ('q', 'quit'):
                self.running= False
            else:
                print('--> Invalid command! <--')
    
p1=Play()
p1.run()    