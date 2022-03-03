import platform as p
class GameStyle():
    def getStyle():
        text='Operating system being used: {}'
        osName=p.system().lower()
        if osName=='darwin':
            btnStyle={'fg':'black','font':('Courier 12')}
        else:
            btnStyle={'bg':'black','fg':'white','highlightbackground':'white'}
        return btnStyle    

        