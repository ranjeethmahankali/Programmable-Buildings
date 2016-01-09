import rhinoscriptsyntax as rs
import math
import time
#created on 9th Jan 2015

filePath = rs.OpenFileName()
view = rs.CurrentView()
rs.Wallpaper(view, filePath)