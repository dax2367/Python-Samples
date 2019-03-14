import arcpy
from arcpy import env
#make sure to always check folder
arcpy.env.workspace = "E:/pythonstuff"
arcpy.env.overwriteoutput = True

#update Cursor

fc = "volcanoes.shp"
#updateing the specific field with what ever you tell it to
cursor = arcpy.da.UpdateCursor(fc, ["LOCATION"])
for row in cursor:
   row[0] = "OR"
   cursor.updateRow(row)



