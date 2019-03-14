import arcpy
from arcpy import env
#make sure to always check folder
arcpy.env.workspace = "E:/pythonstuff"
arcpy.env.overwriteoutput = True

#AddFieldDelimiters

#change cities for what ever it is, fc1 = veriable
fc1 = "cities.shp"
fieldname = "STATUS"
output1 = "CountySeats1.shp"
delimfield = arcpy.AddFieldDelimiters(fc1, fieldname)

select1 = arcpy.Select_analysis(fc1, output1, delimfield + " = 'County Seat'")
print select1


