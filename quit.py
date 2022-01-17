import time
def qt(t):
    numBars=10
    timeEach=t/numBars
    print(timeEach)
    numBarsOver=0
    bar='\u2593'
    while numBarsOver<=numBars:
        print(bar,end='')
        time.sleep(timeEach)
        numBarsOver+=1
        
qt(3)
