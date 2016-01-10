import rhinoscriptsyntax as rs
import math
import time
import System
#created on 9th Jan 2015

filePath = rs.OpenFileName()
bitmap = System.Drawing.Bitmap.FromFile(filePath)

width = bitmap.Width
height = bitmap.Height
color = System.Drawing.Bitmap.GetPixel(bitmap, width/2, height/2)
print color
rvalue = color.R