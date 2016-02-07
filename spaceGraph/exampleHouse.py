from spaceGraph import *

# create a new cSpace 'house'
house = cSpace('House')

# use the addchild method to add a space as a child to the house
house.addChild(cSpace('Living Room'))

# use the addChildren method to add multiple children in one go
house.addChildren([cSpace('Drawing Room'), cSpace('Master Bedroom'), cSpace('Kitchen')])
house.addChildren([cSpace('Guest Bedroom'), cSpace('Toilet'), cSpace('Dining')])

# use the connect children method to establish various connections between the children of the house object
house.connectChildren('Living Room', 'Drawing Room')
house.connectChildren('Living Room', 'Kitchen')
house.connectChildren('Living Room', 'Dining')
house.connectChildren('Living Room', 'Toilet')
house.connectChildren('Kitchen', 'Dining')

# now use the connectSpaces method to establish the connections
# access the children of the house object using house.c[label]
connectSpaces(house.c['Master Bedroom'], house.c['Living Room'])
connectSpaces(house.c['Guest Bedroom'], house.c['Living Room'])

# now let's add more children to the master bedroom
house.c['Master Bedroom'].addChild(cSpace('Master Bed'))
house.c['Master Bedroom'].addChild(cSpace('Master Toilet'))
# above task can be completed in a single line by using the addChildren method
#now let's add connection between these two spaces
house.c['Master Bedroom'].connectChildren('Master Bed','Master Toilet')

#print the cSpace up to two generations of successor spaces
#each space is printed with it's connections in curly braces next to it
#siblings are printed directly under each other while children are tabbed to right by one step
house.printSpace(2)

#Try out the navigation and path finding methods in the console directly
