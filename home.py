from art import *
from stories import Stories
import os
"""
def run():
    rules=''' '''
    print(' '*8,text2art('Home'),' '*8)
    print('''
            1. Enter P/p to play
            2. Enter Q/q to quit
            3. Enter rules to view rules
    ''')
    while True:
        listStories=os.listdir('stories')
        if key in ('p','P','play'):
            print('     -- Choose a Story --')
            for i in range(len(listStories)):
                print('\t',i+1,'.',listStories[i].rstrip('.json'))
            ch=int(input('>>> '))
            if ch<=len(listStories):
                story=Stories(listStories[ch-1])
                story.run()
            else:
                print('--> Story not available! <--') 
        elif key in ('rules', 'r'):
            print(rules)
        elif key in ('q', 'Q', 'quit'):
            return False
"""

def runHome():
    print(text2art('Home'))
    print('''
            1. Enter P/p to play
            2. Enter Q/q to quit
            3. Enter rules to view rules
    ''')
    key=input('>>> ')
    return key
    
def runRules():
    print()
    print(text2art('Rules'))
    print('''
            1. Enter commands
            2. Enjoy the story
    ''')
    key=input('>>> ')
    return key
           