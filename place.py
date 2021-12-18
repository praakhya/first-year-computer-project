from art import *
class Place():
    def __init__(self,r,c,pic=None,message=None,desc=None,act=None):
        self.r=r
        self.c=c
        self.pic=pic
        self.message=message
        self.desc=desc
        self.act=act
    def printCoord(self):
        print('({:d},{:d})'.format(self.r, self.c), end=' ')
    def printPic(self):
        if self.pic != None:
            for i in self.pic:
                print(text2art(i))
        if self.message !=None:
            for i in self.message:
                print(i)
        '''
        try:
            i=len(self.pic)
            for row in range(i):
                for j in self.pic[row]:
                    print(j,end='')
                print()
        except:
            print(self.pic)
        '''
