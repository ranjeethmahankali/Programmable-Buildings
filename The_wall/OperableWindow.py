import rhinoscriptsyntax as rs
import pickle
outlayer='334f6314-48c3-4c04-b000-c956029d1554'
inlayer='25ac8fdd-b2e4-4789-8259-5bc4262ed2ca'
opening=200

#This funtion keeps the relative  position of inlayer
def RelativeVector(PL,PV):
    pos = [0,0,0]
    if 0<=PL and PL<=100:
        pos[0] = -PL*2
    else:
        print('Please enter integral value between 0 to 100')
    if 0<=PV and PV<=100:
        pos[2] =PV*2
    else:
        print('Please enter integral value between 0 to 100')
    return rs.VectorSubtract(pos,current)
    

def MoveScreen(Vector):
    #print(Vector)
    rs.MoveObject(inlayer,Vector)
    cur = rs.VectorAdd(current,Vector)
    return cur

current=[0,0,0]
with open('data.pkl','rb')as input:
    current = pickle.load(input) 

PercentageLight=rs.GetInteger('Enter percentage of light between 0 to 100%',0,0,100)
#light percentage on x axis
PercentageVentilation=rs.GetInteger('Enter percentage of ventilation between 0 to 100%',0,0,100)
#ventilation percentage on y axis
NewPos = RelativeVector(PercentageLight,PercentageVentilation)
#print(NewPos)
current = MoveScreen(NewPos)


with open('data.pkl','wb')as output:
    pickle.dump(current,output,pickle.HIGHEST_PROTOCOL)  