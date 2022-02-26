from placeData import PlaceData
from personData import PersonData
import uuid
from readJson import read
from multiUserData import MultiUserData as mud
class MultiUserInterface():
    online=False
    userScore=0
    userName=''
    userId=uuid.getnode()

    @staticmethod
    def isOnline():
        return MultiUserInterface.online
    @staticmethod
    def register(p_userName):
        MultiUserInterface.userName=p_userName
        MultiUserInterface.online=True
        print(MultiUserInterface.userName)
        return True
    @staticmethod
    def getServerData(newR,newC,server='testServer.json'):
        data=mud(**read(server))
        MultiUserInterface.userScore=data.myScore
        plc={}
        for i in data.placeData:
            plc[i]=PlaceData(**data.placeData[i])        
        return plc
