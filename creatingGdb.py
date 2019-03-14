import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/Temp"
if arcpy.Exists("GIS.gdb"):
    print "The database already exists"
else:
    arcpy.CreateFileGDB_management("C:/Temp", "GIS.gdb")
prjfile = "C:/Temp/roads.prj"
spatialref = arcpy.SpatialReference(prjfile)
featureC = arcpy.CreateFeatureclass_management ("GIS.gdb", "dams", "POLYGON", "", "", "", spatialref)
print featureC
