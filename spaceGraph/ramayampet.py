import spaceGraph as sg

rmpt = sg.cSpace('RmptHouse')

rmpt.addChildren([
    sg.cSpace('Front Yard'),
    sg.cSpace('Pump'),
    sg.cSpace('Sales Office'),
    sg.cSpace('Generator Area'),
    sg.cSpace('Backyard'),
    sg.cSpace('Hall'),
    sg.cSpace('Drawing Room'),
    sg.cSpace('Blue Bedroom'),
    sg.cSpace('Kitchen'),
    sg.cSpace('Aisle'),
    sg.cSpace('Bedroom'),
    sg.cSpace('Store Room'),
    sg.cSpace('Toilets'),
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
