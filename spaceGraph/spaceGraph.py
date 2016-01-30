from collections import defaultdict

def reportError(errMsg):
    print(errMsg)

def connectSpaces(space1, space2):
    space1.connect(space2)
    space2.connect(space1)

class cSpace:

    def __init__(self, name):
        self.label = name
        self.subSpace = defaultdict(object)
        self.leadSpace = self.label
        self.connected = set()

    def addSpace(self,space):
        if not space.label in self.subSpace:
            if len(self.subSpace) == 0:
                self.leadSpace = space.label
                
            self.subSpace[space.label] = space
        else:
            reportError('space name already taken')

    def addSpaces(self, spaceArr):
        for sp in spaceArr:
            self.addSpace(sp)

    def connect(self, space):
        self.connected.add(space.label)
        sp2 = space
        while len(sp2.subSpace)>0:
            self.connected.add(sp2.leadSpace)
            sp2 = sp2.subSpace[sp2.leadSpace]

        if len(self.subSpace)>0:
            self.subSpace[self.leadSpace].connect(space)

    def connectSubSpaces(self, spaceLabel1, spaceLabel2):
        if self.hasSpace(spaceLabel1) and self.hasSpace(spaceLabel2):
            connectSpaces(self.subSpace[spaceLabel1], self.subSpace[spaceLabel2])
    
    def hasSpace(self, spaceLabel):
        if spaceLabel in self.subSpace:
            return True
        else:
            return False

    def isConnected(self, space):
        if space.label in self.connected:
            return True
        else:
            return False

    def subSpaceList(self):
        spaceList = []
        for sp in self.subSpace:
            spaceList.append(sp)

        return spaceList
    

"""
house = cSpace('House')

house.addSpaces([cSpace('Kitchen'),cSpace('Hall'),cSpace('MasterBedroom')])
house.subSpace['MasterBedroom'].addSpaces([cSpace('MasterBed'),cSpace('MasterToilet')])
house.subSpace['Kitchen'].addSpaces([cSpace('Cooking'),cSpace('Washing')])
house.subSpace['Kitchen'].subSpace['Cooking'].addSpaces([cSpace('Stove'),cSpace('Sink')])
house.subSpace['Kitchen'].subSpace['Washing'].addSpaces([cSpace('Washer'),cSpace('Dryer')])
house.subSpace['MasterBedroom'].subSpace['MasterBed'].addSpaces([cSpace('Basin'),cSpace('Commode')])

house.connectSubSpaces('Kitchen','MasterBedroom')
"""
