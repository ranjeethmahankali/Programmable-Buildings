import spaceGraph as sg

floorNum = 2
flatsPerFloor = 2

aptBldg = sg.cSpace('Apartment Building')
groundFloor = sg.cSpace('Ground Floor')

circulationCore = sg.cSpace('Circulation Core', aptBldg)
circulationCore.addChildren([sg.cSpace('Elevator'), sg.cSpace('Stairwell')],True)

groundFloor.addChild(sg.cSpace('Parking'))
aptBldg.addChild(groundFloor)

aptRooms = ['Living Room',
            'Drawing Room',
            'Kitchen',
            'Dining',
            'Toilet',
            'Master Bedroom',
            'Guest Bedroom']

masterBedroom = ['Master Bed',
                 'Master Toilet',
                 'Storage Cabinets',
                 'Closet']

kitchen = ['Washing Area',
           'Cooking Area',
           'Storage']

guestBedroom = ['Guest Bed',
                'Storage Cabinets']

# floor number variable
f = 1
while f <= floorNum:
    floorLabel = 'Floor ' + str(f)
    floor = sg.cSpace(floorLabel, aptBldg)
    lobby = sg.cSpace('Lobby '+str(f))
    floor.addChild(lobby)
    sg.connectSpaces(floor, circulationCore)

    # flat number variable
    a = 1
    while a <= flatsPerFloor:
        flatLabel = 'Flat #' + str(f) + '0' + str(a)
        flat = sg.cSpace(flatLabel, floor)
        sg.connectSpaces(flat,lobby)

        for roomLabel in aptRooms:
            room = sg.cSpace(roomLabel, flat)

            spaces = []
            if roomLabel == 'Master Bedroom':
                for sp in masterBedroom:
                    spaces += [sg.cSpace(sp)]
            elif roomLabel == 'Kitchen':
                for sp in kitchen:
                    spaces += [sg.cSpace(sp)]
            elif roomLabel == 'Guest Bedroom':
                for sp in guestBedroom:
                    spaces += [sg.cSpace(sp)]

            room.addChildren(spaces, True)

        flat.connectChildren('Drawing Room', 'Living Room')
        flat.connectChildren('Kitchen', 'Living Room')
        flat.connectChildren('Dining', 'Living Room')
        flat.connectChildren('Dining', 'Kitchen')
        flat.connectChildren('Toilet', 'Living Room')
        flat.connectChildren('Master Bedroom', 'Living Room')
        flat.connectChildren('Guest Bedroom', 'Living Room')
        
        a += 1
    f += 1

aptBldg.printSpace(2)

aptBldg2 = aptBldg.clone('Apartment Building 2')

#print(sg.printRelation(flat.relationTo(aptBldg.child('Floor 1').child('Flat #101').child('Kitchen'))))

#route = aptBldg.navigateTo(aptBldg.child('Floor 1').child('Flat #101').child('Kitchen'))
route = aptBldg.child('Floor 1').child('Flat #101').child('Kitchen').navigateTo(aptBldg)
routePrint = sg.printRoute(route)

print(routePrint)
#sg.printAllSpaces()
