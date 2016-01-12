import rhinoscriptsyntax as rs
import math
import time
import System
#created on 9th Jan 2015

class floorPanel:
	h1 = 0
	h2 = 0
	h3 = 0
	p1 = None
	p2 = None
	p3 = None
	
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

panel1 = '3b0c40dc-f66f-4b69-85c9-b530e0bdf7ed'
panel2 = 'f9291d72-ec21-47e5-b251-1df1355097ae'
slv = '0b304346-4e53-4290-afab-b2485c846203'

primaryPanel = []
secondaryPanel = []
sleeve = []
panelUnit = []

xNum = 10
yNum = 10
maxHeight = 3000
moduleSize = 500
#now scaling the imported module to the correct module size
boundingBox = rs.BoundingBox([panel1,panel2,slv])
trueSize = rs.Distance(boundingBox[0], boundingBox[1])
trueHeight = rs.Distance(boundingBox[0], boundingBox[4])
scFxy = moduleSize/trueSize # scaling factor in x and y directions
scFz = maxHeight/trueHeight # scaling factor in z direction
rs.ScaleObjects([panel1, panel2, slv], boundingBox[4], [scFxy, scFxy, scFz])
#creating copeis of these panels
rs.EnableRedraw(False)
xN = 0
while (xN < xNum):
	primaryPanel.append([])
	secondaryPanel.append([])
	sleeve.append([])
	panelUnit.append([])
	yN = 0
	while (yN < yNum):
		primaryPanel[xN].append(rs.CopyObject(panel1,[moduleSize*xN, moduleSize*yN,0]))
		secondaryPanel[xN].append(rs.CopyObject(panel2,[moduleSize*xN, moduleSize*yN,0]))
		sleeve[xN].append(rs.CopyObject(slv,[moduleSize*xN, moduleSize*yN,0]))
		panelUnit[xN].append(floorPanel(primaryPanel[xN][yN], secondaryPanel[xN][yN], sleeve[xN][yN]))
		
		yN += 1
	xN += 1

rs.DeleteObjects([panel1, panel2, slv])
rs.EnableRedraw(True)

def useBitmap(filePath, panels):
	bitmap = System.Drawing.Bitmap.FromFile(filePath)
	xN = 0
	while (xN < xNum):
		yN = 0
		while (yN < yNum):
			color = System.Drawing.Bitmap.GetPixel(bitmap, xN, bitmap.Height-1-yN)
			#accounting for the inversion of y-axis from bitmap to 3d space in the above line
			h1 = maxHeight*(color.R+1)/256
			h2 = maxHeight*(color.G+1)/256
			h3 = maxHeight*(color.B+1)/256
			panels[xN][yN].setPanelState(h1,h2,h3)
			
			yN += 1
		xN += 1

def loadPreset(panels):
	rs.EnableRedraw(False)
	file = rs.OpenFileName()
	bitmap = System.Drawing.Bitmap.FromFile(file)
	useBitmap(file, panels)
	rs.EnableRedraw(True)
	
loadPreset(panelUnit)