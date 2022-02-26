from personData import PersonData
class PlaceData():
    def __init__(self,first,second,third,count):
        self.first=PersonData(**first)
        self.second=PersonData(**second)
        self.third=PersonData(**third)
        self.count=count

