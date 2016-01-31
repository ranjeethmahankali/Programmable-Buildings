from collections import defaultdict

def reportError(errMsg):
    print(errMsg)

def connectSpaces(space1, space2):
    space1.connect(space2)
    space2.connect(space1)

class cSpace:

    def __init__(self, name):
        self.label = name
        #this is a dictionary that contains the children of this space
        self.c = defaultdict(object)
        self.leadSpace = self.label
        self.connected = set()
        self.parent = None

    def addSpace(self,space):
        if not space.label in self.c:
            space.parent = self.label
            self.c[space.label] = space
        else:
            reportError('space name already taken')

    def addSpaces(self, spaceArr, isOpen = False):
        newL = []
        for sp in spaceArr:
            self.addSpace(sp)
            newL.append(sp.label)
            
        if isOpen:
            l=0
            while l < len(newL)-1:
                j = l+1
                while j < len(newL):
                    connectSpaces(self.c[newL[l]], self.c[newL[j]])
                    j += 1
                l += 1

    def connect(self, space):
        self.connected.add(space.label)
        sp2 = space
        while sp2.leadSpace != sp2.label:
            self.connected.add(sp2.leadSpace)
            sp2 = sp2.c[sp2.leadSpace]

        if self.leadSpace != self.label:
            self.c[self.leadSpace].connect(space)

    def connectChildren(self, spaceLabel1, spaceLabel2):
        if self.hasSpace(spaceLabel1) and self.hasSpace(spaceLabel2):
            connectSpaces(self.c[spaceLabel1], self.c[spaceLabel2])
    
    def hasSpace(self, spaceLabel):
        if spaceLabel in self.c:
            return True
        else:
            return False

    def isConnected(self, space):
        if space.label in self.connected:
            return True
        else:
            return False

    def children(self):
        spaceList = []
        for sp in self.c:
            spaceList.append(sp)

        return spaceList

"""
house = cSpace('House')

house.addSpaces([cSpace('Kitchen'),cSpace('Hall'),cSpace('MasterBedroom')], True)
house.c['MasterBedroom'].addSpaces([cSpace('MasterBed'),cSpace('MasterToilet')])
house.c['Kitchen'].addSpaces([cSpace('Cooking'),cSpace('Washing')])
house.c['Kitchen'].c['Cooking'].addSpaces([cSpace('Stove'),cSpace('Sink')])
house.c['Kitchen'].c['Washing'].addSpaces([cSpace('Washer'),cSpace('Dryer')])
house.c['MasterBedroom'].c['MasterBed'].addSpaces([cSpace('Basin'),cSpace('Commode')])

house.c['Kitchen'].leadSpace = 'Cooking'
house.c['MasterBedroom'].leadSpace = 'MasterBed'
house.connectChildren('Kitchen','MasterBedroom')
"""
