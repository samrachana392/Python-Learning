'''i=1
while i<=10:
    if i==3:
        break
    print(i)
    i+=1
print("end of loop when 3 is encountered ")

#search for a number x in the given tuple using loop
nums=(1,3,9,16,25,36,49,64,81,100)
x=int(input("enter a number you want to search form the tuple: "))
i=0
while i<len(nums):
    if x==nums[i]:
        print(x, "found in position", i)
        break
    else:
        print(x,"Not found")
    i+=1
print('END OF LOOP AFTER', x, 'FOUND')'''

'''i=1
while i<=10:
    if i==3:
        i+=1
        continue #skip the rest of loop for i=3
    print(i)
    i+=1
print("end of loop")'''


i=1
while i<=10:
    if i%2==0:
        i+=1
        continue #skip the rest of loop for i=3
    print(i)
    i+=1
print("end of loop")
