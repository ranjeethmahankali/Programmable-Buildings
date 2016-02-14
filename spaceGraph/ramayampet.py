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

'''
rmpt.child('Hall').addChildren([sg.cSpace('TV Area'), sg.cSpace('Dining'), sg.cSpace('Small Bed')])
rmpt.printSpace()
hall = rmpt.child('Hall')
hall.clone('Hall2')
rmpt.printSpace()
hall.connectChildren('Small Bed', 'TV Area')
rmpt.printSpace()

rmpt2 = rmpt.clone('rmptClone')
rmpt2.child('Aisle').changeLabel('Gully')
rmpt2.printSpace()
'''

path = rmpt.child('Store Room').findShortestPathTo(rmpt.child('Blue Bedroom'))
allPaths = rmpt.child('Store Room').findAllPathsTo(rmpt.child('Blue Bedroom'))
