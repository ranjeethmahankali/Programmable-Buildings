import math

def calculatePix(ht, maxHt):#caluclates the pixel value scaled to 256 (i.e. 0 to 255)
	ratio = ht/maxHt
	scaled = ratio*255
	pixVal = scaled
	return math.floor(pixVal)

maxHeight = float(input("Enter the maximum height the floor can be raised to: "))
height = None

while True:
	height = input("Enter the height of the panel, or type 'exit' to exit: ")
	
	if height == 'exit':
		break
	else:
		height = float(height)
		print('The pixel value for that panel is : '+ str(calculatePix(height,maxHeight)))