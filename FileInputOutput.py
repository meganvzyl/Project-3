# Introduction to Programming, Task 20: File input and output
# Megan van Zyl, 06/05/2019
# Python code: File input and output

import numpy as np                  #import numpy to be able to calculate percentiles
ofile = open("output.txt", "w")     #open the output file to write to it
f = open ("input.txt" , "r")        #open the input file to read it
ans = []

for line in f:                      
    x = line.split(":")             #split x at :
    y = x[1].strip("\n")            #only want the second item, take out any new lines   
    z = y.split(",")                #make it a list
    
    if x[0] == "min":               #conditions if the line includes the word min
        ans = min(z)
        for line in enumerate(ans):
            line = str(line)
            line = int(line[5])
            z = str(z)
            line = str(line)
            ofile.write ("The min of ") #write to output file
            ofile.write (z)
            ofile.write (" is ")
            ofile.write (line)
            ofile.write (".\n")

    if x[0] == "max":               #conditions if the line includes the word max
        ans = max(z)
        for line in enumerate(ans):
            line = str(line)
            line = int(line[5])
            z = str(z)
            line = str(line)
            ofile.write ("The max of ") #write to output file
            ofile.write (z)
            ofile.write (" is ")
            ofile.write (line)
            ofile.write (".\n")
            
    if x[0] == "avg":               #conditions if the line includes the word avg
        z = [int(i) for i in z]
        ans = float(sum(z)/len(z))
        ans = str(ans)
        z = str(z)
        ofile.write ("The avg of ") #write to output file
        ofile.write (z)
        ofile.write (" is ")
        ofile.write (ans)
        ofile.write (".\n")

    if x[0] == "sum":               #conditions if the line includes the word sum
        z = [int(i) for i in z]
        ans = sum(z)
        ans = str(ans)
        z = str(z)
        ofile.write ("The sum of ") #write to output file
        ofile.write (z)
        ofile.write (" is ")
        ofile.write (ans)
        ofile.write (".\n")

    if x[0] == "p90":               #conditions if the line includes the word p90
        z = [int(i) for i in z]
        a = np.array(z)
        ans = np.percentile(a, 90) #return 90th percentile
        ans = int(ans)
        ans = str(ans)
        z = str(z)
        ofile.write ("The 90th percentile of ") #write to output file
        ofile.write (z)
        ofile.write (" is ")
        ofile.write (ans)
        ofile.write (".\n")

    if x[0] == "p70":               #conditions if the line includes the word p70
        z = [int(i) for i in z]
        a = np.array(z)
        ans = np.percentile(a, 70) #return 70th percentile
        ans = int(ans)
        ans = str(ans)
        z = str(z)
        ofile.write ("The 70th percentile of ") #write to output file
        ofile.write (z)
        ofile.write (" is ")
        ofile.write (ans)
        ofile.write (".\n")


ofile.close()       #close output file
f.close()           #close the input file
