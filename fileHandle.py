import testKct


# Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt","w") #select write/append/read
N,D = testKct.scrap() 

# \n is placed to indicate EOL (End of Line)
#file1.write("Hello \n")
for i in range(0,len(N)):
    file1.write(N[i]+"   -   "+D[i])        #writing
    file1.write('\n')
file1.close() #to change file access modes
  
file1 = open("myfile.txt","r+") 
  
print("Output of Read function is ")
#print(file1.read())