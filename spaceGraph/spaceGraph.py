import uuid
import math
import copy

#Handling the error message
def reportError(errMsg):
    print('Error: ' + errMsg)

#Connects the two spaces back and forth
def connectSpaces(space1, space2):
    space1.connect(space2)
    space2.connect(space1)

#this set contains all the parent-less root spaces in the document
roots = set()

#returns the labels of all the root spaces in the document as a list
def rootLabels():
    rootArr = []
    for sp in roots:
        rootArr.append(sp.label)

    return rootArr

#this method prints all the spaces in the document created till now with their
#appropriate family structure
def printAllSpaces():
    for space in roots:
        space.printSpace()

#This is the class for cSpace object
class cSpace:

    #class initialization
    def __init__(self, name, parentSpace = None):
        self.label = name
        #this is the unique id that is assigned to each space in order to avoid
        #confusion in cases where same label is used multiple times across a family tree
        #for example, the label 'toilet' could be used multiple times in a tree representing
        #an apartment building with many flats, but all toilets will have unique ids
        self.id = uuid.uuid4()
        #this is a dictionary that contains the children of this space
        self.c = dict()
        self.connected = set()
        #this is the deciding the default value for the parent attribute
        #and also updating the roots of the document
        if parentSpace is None:
            self.parent = None
            roots.add(self)
        else:
            parentSpace.addChild(self)

    #This function adds the given space as a child to this space
    def addChild(self,space):
        labelIsValid = (not space.label in self.c) and self.label != space.label
        labelIsValid = labelIsValid and (not self.hasAncestor(space.label))
        if labelIsValid:
            space.parent = self
            self.c[space.label] = space
            #now removving the child space from the roots set if it was already there
            roots.discard(space)
        else:
            errMsg = 'space name '+space.label+' already taken by a sibling or an ancestor'
            reportError(errMsg)

    #This function adds multiple childrfen supplied as a list or a tuple
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
    
    def changeLabel(self, newLabel):
        oldLabel = self.label
        self.label = newLabel
        del self.parent.c[oldLabel]
        self.parent.c[newLabel] = self

    #Adds a one-way connection from the given space to this space 
    def connect(self, space):
        self.connected.add(space)

    #This adds a two way conneciton between the given two children of this space
    def connectChildren(self, spaceLabel1, spaceLabel2):
        if self.hasSpace(spaceLabel1) and self.hasSpace(spaceLabel2):
            connectSpaces(self.c[spaceLabel1], self.c[spaceLabel2])
    
    #Returns a boolean if this space has the given space as a child
    def hasSpace(self, spaceLabel):
        if spaceLabel in self.c:
            return True
        else:
            return False

    #returns true if this space is connected to the given space
    def isConnected(self, space):
        if space in self.connected:
            return True
        else:
            return False

    # instead of accessing directly through the array,
    # this method checks if the child with that label exists and then returns it
    def child(self, childLabel):
        if childLabel in self.c:
            return self.c[childLabel]
        else:
            reportError('No child with that label')
            return None

    #returns a list containing the children of this space
    def children(self):
        spaceList = []
        for sp in self.c:
            spaceList.append(sp)

        return spaceList

    #this method returns the root space of the family tree of which this space is a part of
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()

    #removes the child space with the given label
    def removeChild(self,spaceLabel):
        if spaceLabel in self.c:
            del self.c[spaceLabel]

    #removes all the children spaces with labels in the provided list
    def removeChildren(self, spLabelArr):
        for spL in spLabelArr:
            self.removeChild(spL)

    #returns true if this space has a sibling with the given label
    def hasSibling(self, sibLabel):
        if not self.parent is None:
            if sibLabel in self.parent.c and self.label != sibLabel:
                return True
            elif self.label == sibLabel:
                err = 'the cSpace '+self.label+' is being tested if it is its own sibling'
                #reportError(err)
                return True
            else:
                return False
        else:
            reportError(self.label+' has no parents')
            return False

    #returns the sibling space object by reference
    def sibling(self, sibLabel):
        if self.hasSibling(sibLabel):
            return self.parent.c[sibLabel]
        else:
            reportError('Could not find Sibling')
            return None

    #this function checks if the cSpace has any descendant with label desLabel
    def hasDescendant(self, desLabel):
        if desLabel in self.c:
            return True
        
        for cL in self.c:
            if self.c[cL].hasDescendant(desLabel):
                return True

        return False

    #this function checks if the cSpace has any ancestor with the label anLabel
    def hasAncestor(self, anLabel):
        if not self.parent is None:
            if self.parent.label == anLabel:
                return True
        else:
            return False
            
        if self.parent.hasAncestor(anLabel):
            return True

        return False
    
    # this funtion prints the internal structure and children upto
    # maxDepth number of generations
    def printSpace(self, maxDepth = math.inf, d = 0):
        l = self.label
        tab = d*'\t'
        connections = ''
        if len(self.connected) == 0:
            connections = '-'
        else:
            count = 1
            for space in self.connected:
                name = space.label
                if count < len(self.connected):
                    name += ', '
                
                connections += name
                count += 1

        connections = '{' + connections + '}'

        spacePrint = tab + l + ': ' + connections
        print(spacePrint)
        d += 1

        if d <= maxDepth and len(self.c) > 0:
            for spC in self.c:
                self.c[spC].printSpace(maxDepth, d)

    #this method finds a path to the given sibling space
    #finds a path to the sibling with label sibLabel
    def findPathTo(self, targetSpace, path = []):
        if self.hasSibling(targetSpace.label):
            #find the path
            path = path + [self]

            if self.label == targetSpace.label:
                return path

            for sp in self.connected:
                if sp not in path:
                    newPath = sp.findPathTo(targetSpace, path)
                    if newPath: return newPath
            return None
        else:
            err = 'cannot find path between non-siblings'
            reportError(err)
            return None

    #finds all paths to the sibling with label sibLabel
    def findAllPathsTo(self, targetSpace, path = []):
        if self.hasSibling(targetSpace.label):
            #find all paths
            path = path + [self]

            if self.label == targetSpace.label:
                return [path]

            paths = []
            for sp in self.connected:
                if sp not in path:
                    newPaths = sp.findAllPathsTo(targetSpace, path)
                    for newPath in newPaths:
                        paths.append(newPath)

            return paths
        else:
            err = 'cannot find any paths between non-siblings'
            reportError(err)
            return None

    #finds the shortest path to the sibling with label sibLabel
    def findShortestPathTo(self, targetSpace, path = []):
        if self.hasSibling(targetSpace.label):
            #find the shortest path
            path = path + [self]

            if self.label == targetSpace.label:
                return path

            shortestPath = None
            for sp in self.connected:
                if sp not in path:
                    newPath = sp.findShortestPathTo(targetSpace, path)
                    if newPath:
                        if not shortestPath or len(shortestPath) > len(newPath):
                            shortestPath = newPath

            return shortestPath
        else:
            err = 'cannot find a path between non-siblings'
            reportError(err)
            return None

    # this method returns the path through the family tree from this space and a
    # non-sibling space
    def relationTo(self, space, path = [], direction = 0):
        # direction 0 for the node that is the starting node
        # direction -1 for node that is reached by travelling up the family tree
        # direction 1 for node that is reached by travelling down the family tree
        path = path + [[self.label, direction]]

        if self.id == space.id:
            return path

        # all() and any() are essentially like logic gates for more than two booleans at once
        # all booleans can be passed iterably directly in the parantheses with a
        # syntax similar to that of a for loop
        if (not self.parent is None) and all(self.parent.label not in pE for pE in path):
            newPath = self.parent.relationTo(space, path, -1)
            if newPath: return newPath

        for ch in self.c:
            if all(ch not in pE for pE in path):
                newPath = self.c[ch].relationTo(space, path, 1)
                if newPath: return newPath

        return None

    #this function clones a given space with all the same attributes except the label
    #which is provided as a parameter. The clone will have same connections to the siblings
    #the clone will also occupy the same position in the family tree - like a twin brother
    #to the original space
    #But if you specifiy a parentSpace then the cloned space will be a child of that
    #and it will have no connections
    def clone(self, newLabel, parentSpace = 'sameParent', CloneDepth = 0):
        if parentSpace == 'sameParent':parentSpace = self.parent

        newSpace = copy.deepcopy(self)
        newSpace.label = newLabel
        newSpace.id = uuid.uuid4()
        newSpace.connected = set()

        if parentSpace:
            parentSpace.addChild(newSpace)
            if parentSpace is self.parent:
                for space in self.connected:
                    connectSpaces(newSpace, space)
        else:
            newSpace.parent = parentSpace
            roots.add(newSpace)

        return newSpace

def printPath(path):
    pathPrint = ''
    
    i = 0
    while i < len(path):
        pathPrint += path[i].label
        
        if i != len(path)-1:
            pathPrint += ' -> '

        i += 1
            
    print(pathPrint)
