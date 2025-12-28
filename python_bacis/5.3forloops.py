'''#Print the elements in the list using for loop
nums=[1,3,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)
else: #optional
    print("loop executed")


#search for an element x using for loop
nums=(1,4,9,16,25,36,49,64,81,100,49)
index=0
x=int(input("enter a element you want to search from the list: "))
for val in nums:
    if(x==val):
        print(x,"found at position", index)
        break
    print(val)
    index+=1
else:
    print(x, "not found")

#range()
print(range(5))

seq=range(5)
print(seq[0])
print(seq[1])
print(seq[3])
print(seq)
for el in range(10): #range(stop) start=0 by default, step=1 by default
    print(el)

for el in range(2,10): #range(start, stop) step=1 by default
    print(el)

for el in range(2,10,2): #range(start, stop, step) 
    print(el)'''

'''#print all numbers from 1 to 100
for i in range(1,101):
    print(i)

#print numbers from 100 to 1
for i in range (100, 0,-1):
    print(i)

#print the multiplication table of n
n=int(input("Enter a number"))
for i in range(1,11):
    mul=n*i
    print(n,"*",i,"=",mul) '''

'''#wap to find the sm of n natural numbers using while loop
sum=0
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    sum+=i
print("sum is ", sum)'''

#wap to find the factorial of first n natural numbers
fact=1
n=int(input("enter the value of n: "))
for i in range(1,n+1):
    fact=fact*i
print("factorial of ",n,"is",fact)