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
    cSpace('Bedroom'),
    cSpace('Store Room'),
    cSpace('Toilets'),
    ])

rmpt.connectChildren('Front Yard','Pump')
