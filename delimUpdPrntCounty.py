import arcpy
from arcpy import env
#make sure to always check folder
arcpy.env.workspace = "E:/pythonstuff"
arcpy.env.overwriteoutput = True

#update Cursor

fc = "cities.shp"
fieldname = "STATUS"
#Select all that have a specific name and then adding or change that name.
delimfield = arcpy.AddFieldDelimiters(fc, fieldname)
#the '' is where specific name goes.
cursor = arcpy.da.UpdateCursor (fc, fieldname, delimfield + " = ''")
#the rows = "" is the output name.
for rows in cursor:
	rows[0] = "Not a County Seat"
	cursor.updateRow(rows)
del rows
del cursor



