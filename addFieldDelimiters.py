import arcpy
from arcpy import env
#make sure to always check folder
arcpy.env.workspace = "E:/pythonstuff"
arcpy.env.overwriteoutput = True

#AddFieldDelimiters

#change cities for what ever it is, fc1 = veriable
fc1 = "cities.shp"
#change field to which ever u need
fieldname = "POP2007"
#output for which ever u want
output1 = "Pop2007.shp"
delimfield = arcpy.AddFieldDelimiters(fc1, fieldname)
#select by atribute
select1 = arcpy.Select_analysis(fc1, output1, delimfield + " > 30000")
print select1
