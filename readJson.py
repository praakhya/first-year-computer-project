import json
def read(fname):
    with open(fname,'r') as plcdat:
        data=plcdat.read()
        datalist=json.loads(data)
    return datalist