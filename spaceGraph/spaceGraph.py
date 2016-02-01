from collections import defaultdict

def reportError(errMsg):
    print('Error: ' + errMsg)

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

    def addChild(self,space):
        if not space.label in self.c:
            space.parent = self
            self.c[space.label] = space
        else:
            reportError('space name already taken')

    def addChildren(self, spaceArr, isOpen = False):
        newL = []
        for sp in spaceArr:
            self.addChild(sp)
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

    def removeChild(self,spaceLabel):
        if spaceLabel in self.c:
            del self.c[spaceLabel]

    def removeChildren(self, spLabelArr):
        for spL in spLabelArr:
            self.removeChild(spL)

    def isSibling(self, sibLabel):
        if not self.parent is None:
            if sibLabel in self.parent.c and self.label != sibLabel:
                return True
            elif self.label == sibLabel:
                err = 'the cSpace '+self.label+' is being tested if it is its own sibling'
                reportError(err)
                return False
            else:
                return False
        else:
            reportError(self.label+' has no parents or family')
            return False

    def sibling(self, sibLabel):
        if self.isSibling(sibLabel):
            return self.parent.c[sibLabel]
        else:
            reportError('Could not find Sibling')
            return None
    
    def printSpace(self, maxDepth, d = 0):
        l = self.label
        tab = d*'\t'
        connections = str(self.connected)
        if len(self.connected) == 0:
            connections = '{-}'

        spacePrint = tab + l + ': ' + connections
        print(spacePrint)
        d += 1

        if d <= maxDepth and len(self.c) > 0:
            for spC in self.c:
                self.c[spC].printSpace(maxDepth, d)
        

#This code is for testing the above classes and defnitions
sg = cSpace('spaceGraph')

sg.addChildren([cSpace('A'), cSpace('B'), cSpace('C'), cSpace('D')])
sg.addChildren([cSpace('E'), cSpace('F')])
sg.c['A'].addChildren([cSpace('A1'),cSpace('A2'),cSpace('A3')])
sg.c['A'].connectChildren('A1','A3')

sg.connectChildren('A', 'B')
sg.connectChildren('B', 'C')
sg.connectChildren('B', 'D')
sg.connectChildren('C', 'D')
sg.connectChildren('E', 'F')
sg.connectChildren('F', 'C')

sg.printSpace(2)
