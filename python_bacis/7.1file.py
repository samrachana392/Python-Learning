# READING A FILE
#fp=open("sample.txt","rt")
#fp=open("D:\Python\sample.txt","r") if the file is not in the same folder 
#as the python file then we need to mention the path of the file

'''data=fp.read() #reads the entire file
print(data)
'''

'''dt=fp.read(7) #reads first 7 characters
print(dt)'''

'''line1=fp.readline() # reads one line at a time
print(line1)
line2=fp.readline()
print(line2)
line3=fp.readline()
print(line3)'''
#fp.close()

'''
#WRITING TO A FILE
f=open("sample.txt","w")
f.write("In write mode all the old data are over written")
f.close()
'''
#APPENDING THE FILE
f=open("sample.txt","a")
f.write("\nIn append mode, new data are added to the last like editing, or adding data")
f.close()

f=open("demo.txt",'w') #in w and a mode if such file doesnot exist then new file is created 
f.close()