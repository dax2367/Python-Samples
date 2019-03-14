#Used to replace text files or fix up old ones.
input = open("E:/pythonstuff/coordinates.txt")
output = open("E:/pythonstuff/coordFixed.txt", "w")
#Loops through changing each one based on peramiters
for line in input:
    str = line.replace("ID: ", "")
    str = str.replace("Lat: ", "")
    str = str.replace("Long: ", "")
    output.write(str)
input.close()
output.close()
