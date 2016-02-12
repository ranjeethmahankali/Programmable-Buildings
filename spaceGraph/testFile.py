from spaceGraph import *
"""
rmpt = cSpace('RmptHouse')

rmpt.addChildren([
    cSpace('Front Yard'),
    cSpace('Pump'),
    cSpace('Sales Office'),
    cSpace('Generator Area'),
    cSpace('Backyard'),
    cSpace('Hall'),
    cSpace('Drawing Room'),
    cSpace('Blue Bedroom'),
    cSpace('Kitchen'),
    cSpace('Aisle'),
    cSpace('Bedroom'),
    cSpace('Store Room'),
    cSpace('Toilets'),
    ])

rmpt.connectChildren('Front Yard','Pump')
rmpt.connectChildren('Front Yard','Drawing Room')
rmpt.connectChildren('Drawing Room','Hall')
rmpt.connectChildren('Hall', 'Backyard')
rmpt.connectChildren('Hall','Aisle')
rmpt.connectChildren('Hall','Kitchen')
rmpt.connectChildren('Aisle','Bedroom')
rmpt.connectChildren('Aisle','Store Room')
rmpt.connectChildren('Aisle','Toilets')
#rmpt.connectChildren('Hall','Sales Office')
rmpt.connectChildren('Backyard','Generator Area')
rmpt.connectChildren('Generator Area','Pump')
rmpt.connectChildren('Pump','Sales Office')
rmpt.connectChildren('Blue Bedroom','Drawing Room')

def shortestPath(s1, s2):
    sp1 = rmpt.c[s1]
    path = sp1.findShortestPathTo(s2)

    for p in path:
        print(p)

def allPaths(s1, s2):
    sp1 = rmpt.c[s1]
    paths = sp1.findAllPathsTo(s2)

    if paths:
        print('================================================')
        for path in paths:
            for p in path:
                print(p)
            print('================================================')

"""
sg = cSpace('spaceGraph')

sg.addChildren([cSpace('A'), cSpace('B'), cSpace('C'), cSpace('D')])
sg.addChildren([cSpace('E'), cSpace('F')])
sg.c['A'].addChildren([cSpace('A1'),cSpace('A2'),cSpace('A3')])
sg.c['A'].connectChildren('A1','A3')
sg.c['A'].c['A2'].addChildren([cSpace('A21'),cSpace('A22'),cSpace('A23')])

sg.connectChildren('A', 'B')
sg.connectChildren('B', 'C')
sg.connectChildren('B', 'D')
sg.connectChildren('C', 'D')
sg.connectChildren('E', 'F')
sg.connectChildren('F', 'C')

A = sg.c['A']
path = A.findAllPathsTo('F')
#print(path)
short = A.findShortestPathTo('F')
#print(short)
A22 = sg.c['A'].c['A2'].c['A23']
print(A22.relationTo(A))
