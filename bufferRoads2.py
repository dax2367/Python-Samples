import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Temp"
fcs = arcpy.ListFeatureClasses("","point")
if arcpy.Exists("roads.shp"):
    for buff in fcs:
        arcpy.Buffer_analysis (buff, "Results\Buffer" + buff, "0.25 MILES")
else:
    print "the file does not exists"
