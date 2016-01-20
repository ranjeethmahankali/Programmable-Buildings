import rhinoscriptsyntax as rs
import math
import System
# created on 9th Jan 2015

# this class defines a single floorPanel or Tile as an Object with neccessary functions to control it
class floorPanel:
	h1 = 0
	h2 = 0
	h3 = 0
	p1 = None
	p2 = None
	slv = None
	
	panelID = None
	
	def __init__(self,panel1, panel2, sleeve):
		self.p1 = panel1
		self.p2 = panel2
		self.slv = sleeve
		self.panelID = rs.AddGroup()
		rs.AddObjectsToGroup([panel1, panel2, sleeve], self.panelID)
	
	def setPanelState(self, newH1, newH2, newH3):
		dh1 = newH1 - self.h1
		dh2 = newH2 - self.h2
		dh3 = newH3 - self.h3
		
		rs.MoveObject(self.p1, [0,0,dh1])
		rs.MoveObject(self.p2, [0,0,dh2])
		rs.MoveObject(self.slv, [0,0,dh3])
		
		self.h1 = newH1
		self.h2 = newH2
		self.h3 = newH3
	
	def reset(self):
		self.setPanelState(0,0,0)
	
	def delete(self):
		rs.DeleteObjects([self.p1, self.p2, self.slv])
		self.p1 = None
		self.p2 = None
		self.slv = None

# asks the user to load a bitmap preset and uses it on the 'panels' 2d array
def loadPreset(panels):
	rs.EnableRedraw(False)
	file = rs.OpenFileName()
	bitmap = System.Drawing.Bitmap.FromFile(file)
	useBitmap(file, panels)
	rs.EnableRedraw(True)

# resets the floor corresponding to the passed 2d array
def resetFloor(panels):
	rs.EnableRedraw(False)
	x = 0
	while x < len(panels):
		y = 0
		while y < len(panels[x]):
			panels[x][y].reset()
			y += 1
		x += 1
	rs.EnableRedraw(True)

# deletes the entire floor defined by the 2d list - panels and all its components
def deleteFloor(panels):
	rs.EnableRedraw(False)
	for col in panels:
		for tile in col:
			tile.delete()
	rs.EnableRedraw(True)

# uses the bitmap located in the filePath on the floor defined by the 2d array 'panels'
def useBitmap(filePath, panels):
	bitmap = System.Drawing.Bitmap.FromFile(filePath)
	xN = 0
	while (xN < xNum):
		yN = 0
		while (yN < yNum):
			color = System.Drawing.Bitmap.GetPixel(bitmap, xN, bitmap.Height-1-yN)
			#accounting for the inversion of y-axis from bitmap to 3d space in the above line
			h1 = maxHeight*(color.R+1)/255
			h2 = maxHeight*(color.G+1)/255
			h3 = maxHeight*(color.B+1)/255
			panels[xN][yN].setPanelState(h1,h2,h3)
			
			yN += 1
		xN += 1

panel1 = '3b0c40dc-f66f-4b69-85c9-b530e0bdf7ed'
panel2 = 'f9291d72-ec21-47e5-b251-1df1355097ae'
slv = '0b304346-4e53-4290-afab-b2485c846203'

# defining the size of the tile (square shape) and the max Height achivable by it
maxHeight = 3000
moduleSize = 500

# now scaling the imported module to the correct module size
boundingBox = rs.BoundingBox([panel1,panel2,slv])
trueSize = rs.Distance(boundingBox[0], boundingBox[1])
trueHeight = rs.Distance(boundingBox[0], boundingBox[4])
scFxy = moduleSize/trueSize # scaling factor in x and y directions
scFz = maxHeight/trueHeight # scaling factor in z direction
rs.ScaleObjects([panel1, panel2, slv], boundingBox[4], [scFxy, scFxy, scFz])

# defining the number of tiles in the x and y directions - defined by the user
xNum = rs.GetInteger('Enter the number of tiles in the x-direction',10)
yNum = rs.GetInteger('Enter the number of tiles in the y-direction',10)

# these arrays will contain the identifiers of all the different objects
# these are 2d arrays corresponding to positions
primaryPanel = [] # the top panel
secondaryPanel = [] # the secondary panel underneath the top panel
sleeve = [] # the square cross section sleeve
panelUnit = [] # and integrated panelUnit with one each of the above three objects

# creating copeis of these panels and making a floor
rs.EnableRedraw(False)
xN = 0
while (xN < xNum):
	#adding a new empty column to all the 2d arrays
	primaryPanel.append([])
	secondaryPanel.append([])
	sleeve.append([])
	panelUnit.append([])
	yN = 0
	while (yN < yNum):
		#appending the newly created objects into those arrays
		primaryPanel[xN].append(rs.CopyObject(panel1,[moduleSize*xN, moduleSize*yN,0]))
		secondaryPanel[xN].append(rs.CopyObject(panel2,[moduleSize*xN, moduleSize*yN,0]))
		sleeve[xN].append(rs.CopyObject(slv,[moduleSize*xN, moduleSize*yN,0]))
		panelUnit[xN].append(floorPanel(primaryPanel[xN][yN], secondaryPanel[xN][yN], sleeve[xN][yN]))
		
		yN += 1
	xN += 1

#now hiding the original prototype panel from which we generated all the copies in the 2d array
rs.HideObjects([panel1, panel2, slv])
rs.EnableRedraw(True)

#user will now load a preset by selecting an iage file
loadPreset(panelUnit)

# this loop allows the user to go through more presets
while True:
	response = rs.GetString('Do you want to load another preset? (y/n)','y')
	print(response)
	if response == 'y' or response == 'Y':
		resetFloor(panelUnit)
		loadPreset(panelUnit)
	elif response == 'n' or response == 'N':
		break
	else:
		print('Invalid response')
		continue

#this loop forces the user to choose between exporting the results to a new file or discard the changes
#this loop resets the file in the end
while True:
	response = rs.GetString('Do you want to save this model? (y/n)','y')
	if response == 'y':
		rs.Command('_SelAll _Export')
		deleteFloor(panelUnit)
		rs.ShowObjects([panel1, panel2, slv])
		break
	elif response == 'n':
		exitPrompt = 'Are you sure? You will lose the loaded preset (press y if you want to discard the changes and exit)'
		response = rs.GetString(exitPrompt,'y')
		if response == 'y':
			deleteFloor(panelUnit)
			rs.ShowObjects([panel1, panel2, slv])
			break
		else:
			continue