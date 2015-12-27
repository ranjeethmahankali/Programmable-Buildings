import rhinoscriptsyntax as rs
import math
import time
#created on 23rd december 2015, to test out python for rhino

count = rs.GetInteger('Enter the number of boxes that you want to draw',1,1,5)
while count >0:
	rs.EnableRedraw(False)
	p1 = rs.GetPoint('Place the first point')
	p2 = rs.GetPoint('Place the second point')
	count -= 1
	plane = rs.PlaneFromNormal(p1, [0,0,1])
	rectangle = rs.AddRectangle(plane,(p2[0]-p1[0]),(p2[1]-p1[1]))
	surface = rs.AddPlanarSrf(rectangle)
	
	rs.EnableRedraw(True)
	rs.EnableRedraw(False)
	
	height = rs.GetInteger('Enter the height of the box',10,5,50)
	p3 = rs.VectorAdd(p1,[0,0,height])
	path = rs.AddLine(p1,p3)
	
	box = rs.ExtrudeSurface(surface, path,True)
	rs.DeleteObjects([path, rectangle, surface])
