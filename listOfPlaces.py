from place import Place
import pickle
import readWritePlaces as placOp
newplaces=[]
#Home
name='Home'
pic=[
'    ___     ___     _________        ____    ____   __________',
'   |   |   |   |   /   ____   \     |    \  /    | |    ______|',
'   |   |___|   |  /   /    \   \    |     \/     | |   |___',
'   |    ___    |  |   |    |   |    |   |\__/|   | |   ____|',
'   |   |   |   |  \   \____/   /    |   |    |   | |  |_______',
'   |___|   |___|   \__________/     |___|    |___| |__________|',
'                                                               ',
'   Enter \'P\' to PLAY',
'   Enter \'Q\'/Esc to QUIT'
]
coord=(0,0)
newplaces.append([coord[0],coord[1],pic,name])
placOp.append(newplaces,'places.dat')
print('ADD PLACES')
while True:
    coordx=int(input('x: '))
    coordy=int(input('y: '))
    print('Pic\n')
    pic=[]
    while True:
        pic.append(input())
    name=input('Name: ')
    newplaces.append([coordx,coordy,pic,name])
    placOp.append(newplaces,'places.dat')
data=placOp.read('places.dat')
for row in data:
    pl=Place(row[0],row[1],row[2],row[3])
    pl.printCoord()
    print()
    pl.printPic()
