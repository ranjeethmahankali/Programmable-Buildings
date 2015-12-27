import rhinoscriptsyntax as rs
import math
import time
#created on 24th december 2015, to explore python for rhino
rs.Command("_SelAll _Delete")
radius = 10
frame = 0
ang = 0
pos = [radius,0,0]
point = rs.AddPoint(pos)
while frame < 120:
	newPos = [radius*math.cos(ang), radius*math.sin(ang), 0]
	moveVec = rs.PointSubtract(newPos,pos)
	pos = newPos
	rs.MoveObject(point,moveVec)
	frame += 1
	ang += 3*(math.pi/180)
	time.sleep(0.02)