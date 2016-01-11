import rhinoscriptsyntax as rs
import math
import time
import System
#created on 9th Jan 2015

class floorPanel:
	h1 = 0
	h2 = -30
	h3 = -30
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
		self.setPanelState(0,-30,-30)

#filePath = rs.OpenFileName()
bitmap = System.Drawing.Bitmap.FromFile('D:\Media\Pictures\Roorkee.jpg')
#print(filePath)
width = bitmap.Width
height = bitmap.Height
color = System.Drawing.Bitmap.GetPixel(bitmap, width/2, height/2)

print(color)

panel1 = '31657b8e-45a1-4179-9b38-703dfd9a3cad'
panel2 = 'ea67afd2-ba40-4a7f-ad04-d6476703de68'
slv = '755ac1ba-7695-430c-b33c-b9824c879baf'

primaryPanel = []
secondaryPanel = []
sleeve = []
panelUnit = []
#creating copeis of these panels
xNum = 3
yNum = 3
moduleSize = 500

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

panelUnit[0][0].setPanelState(1000, 500, 400)
panelUnit[2][1].setPanelState(1000, 500, 400)
panelUnit[0][0].reset()

rs.EnableRedraw(True)