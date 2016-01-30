from collections import defaultdict

def reportError(errMsg):
    print(errMsg)

class spaceGraph:

    def __init__(self):
        self.graph = defaultdict(set)
        self.graph['0'] = set()

    def addConnection(self,space1,space2, biDir = True):
        self.graph[space1].add(space2)

        if biDir:
            self.graph[space2].add(space1)

    def addSpace(self,space):
        if not space in self.graph:
            self.graph[space] = set()
        else:
            reportError('space name already taken')

    def hasSpace(self, space):
        if space in self.graph:
            return True
        else:
            return False

    

    


        
