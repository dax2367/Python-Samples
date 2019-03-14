#creating brand new line and inserting the new thing into that new line, used for headings
file1 = open("E:/pythonstuff/newHeaders.txt")
list2 = file1.readlines()
file1.close
list2.insert (0, "This is the heading\n")
file1 = open("E:/pythonstuff/newHeaders.txt", "w")
file1.writelines(list2)
file1.close
