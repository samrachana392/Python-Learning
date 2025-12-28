'''with open("demo.txt","r") as fp:
    print(fp.read())
     
with open("demo.txt","w") as f:
    f.write("new data after write mode")

with open("demo.txt","a") as f:
    f.write(" appending")'''

#deleting a file
import os
os.remove("demo.txt")
    