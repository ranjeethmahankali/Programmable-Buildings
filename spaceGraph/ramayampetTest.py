from spaceGraph import *

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

    print('================================================')
    for path in paths:
        for p in path:
            print(p)
        print('================================================')
