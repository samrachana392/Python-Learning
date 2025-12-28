'''with open ("sample.txt", "w") as f:
    f.write("Hi everyone \n")
    f.write("we are learning file I/O \nusing java.")
    f.write("\nI like programming in java")

#WAF that replaces all occurance of "java" with "python" in the above file:
def checkforword():
    with open ("sample.txt", "r") as f:
        data=f.read()
        new_data=data.replace("java","python")
        print(new_data)
    with open ("sample.txt","w") as f:
        f.write(new_data)
checkforword()

#Search if the word "learning" exists in the file or not
with open ("sample.txt","r") as f:
    dat=f.read()
    if(dat.find("learning")!=-1):
        print("Found")
    else:
        print("not found")

#Waf to find in which line of the file does the word "learning " occur first, 
# print -1 if word is not found
def checkforline():
    word="learning"
    line=1
    data=True # to continue to read till last line: up to line 4 it will be true as there is data but after line 4, there is no data so we should stop reading line after 4, after 4, since there is no data it will be false
    with open("sample.txt", "r") as f:
        while data:
            data=f.readline()
            if(data.find(word)!=-1):
                print(line)
                return
            line +=1
    print("not found")
checkforline()'''

#From a file containging numbers seperated by a comma, print the count of even numbers

with open("practice.txt", "r") as f:
    data=f.read()
    print(data)
    print(type(data)) #string so we need to first concert into integer
    ''' num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            if(int(num)%2 == 0):
                print(int(num), " is even") #do count+=1
            num=""
        else:
            num+= data[i]'''
    count=0
    nums = data.split(",") # list is made using split
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)    