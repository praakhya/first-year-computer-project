import pickle
def read(fname):
    try:
        with open(fname,'rb') as plcdat:
            data=pickle.load(plcdat)
    except:
        data=[]
    return data
def append(newdata,fname):
    data=read(fname)
    with open(fname, 'wb') as plcdat:
        for i in newdata:
            if i not in data:
                data.append(i)
        data=list(data)
        pickle.dump(data,plcdat)