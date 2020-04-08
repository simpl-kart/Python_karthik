import os
newfile = open("newtestfile.txt","r")
#print  newfile.mode ###returns w+ ## just to check what mode the file is in
#newfile = 2 #### python automatically reassigns the file with 2 by closing above file karthiktst.txt
# for i in range(1,12):
#     newfile.write("Hello welcome to  karthik's world of python \n")

# os.rename("karthiktst.txt", "newtestfile.txt")
# os.remove("newtestfile.txt")
print newfile.seek(5)
print newfile.tell()
print newfile.read()

####file.close()########to close a file
