import time, os
from tkinter import HORIZONTAL
#from tkinter import *
from tkinter.ttk import *
def ld(t=1.5):
    numBars=10
    timeEach=t/numBars
    numBarsOver=0
    bar='\u2593'
    print('-->|',end='')
    while numBarsOver<=numBars:
        print(bar,end='',flush=True)
        time.sleep(timeEach)
        numBarsOver+=1
    print('|<--')

def qt():
    #print(colored("Quitting", 'yellow', 'on_blue', attrs=['blink', 'bold']))
    ld()
    os.system('cls')
