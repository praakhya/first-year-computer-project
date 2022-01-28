'''
import json
from place import Place

def populate(master,fname):
    print('in map-populate')
    places = []
    maxr=0
    maxc=0
    map=[]
    #try:
    print('in try')
    with open(fname,'r') as plcdat:
        data=plcdat.read()
    print('read data')
    datalist=json.loads(data)
    print('data loaded in list')
    for i in range(len(datalist)):
        print('1')
        p = Place(master,**datalist[i])
        print('2')
        places.append(p)
        print('3')
        if p.r > maxr:
            maxr = p.r
        print('4')
        if p.c > maxc:
            maxc = p.c
        print('making place objects')
    maxr+=1;maxc+=1
    #except:
    #    print('in except')
    #    pass
    for i in range(maxr):
        print('making zero matrix')
        map.append([])
        for j in range(maxc):
            map[i].append(0)
    for place in places:
        print('making final map')
        i=place.r
        j=place.c
        map[i][j]=place
    return map
'''