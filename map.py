import json
from place import Place
def populate(fname):
    places = []
    maxr=0
    maxc=0
    map=[]
    try:
        with open(fname,'r') as plcdat:
            data=plcdat.read()
        datalist=json.loads(data)
        for data in datalist:
            p = Place(**data)
            places.append(p)
            if p.r > maxr:
                maxr = p.r
            if p.c > maxc:
                maxc = p.c
        maxr+=1;maxc+=1
    except:
        pass
    for i in range(maxr):
        map.append([])
        for j in range(maxc):
            map[i].append(0)
    for place in places:
        i=place.r
        j=place.c
        map[i][j]=place
    return map
