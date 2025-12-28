'''i=1
while i<=100:
    print(i)
    i+=1'''

'''j=100
while j>=1:
    print(j)
    j-=1'''

'''n=int(input("Enter a number you want multiplication table of: "))
i=1
while i<=10:
    mul= n*i
    print(n,"*",i,"=", mul)
    i+=1'''


'''
#print the elements of the given list usin loop
nums=[1,3,9,26,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1
    '''

'''
#search for a number x in the given tuple using loop
nums=(1,3,9,16,25,36,49,64,81,100)
x=int(input("enter a number you want to search form the tuple: "))
i=0
while i<len(nums):
    if x==nums[i]:
        print(x, "found in position", i)
    else:
        print(x,"Not found")
    i+=1
'''
#wap to find the sm of n natural numbers using while loop
sum=0
i=0
n=int(input("enter the value of n: "))
while(i<=n):
    sum+=i
    i+=1
print("sum= ", sum)

#wap to find the factorial of first n natural numbers
fact=1
i=1
n=int(input("enter the value of n: "))
while(i<=n):
    fact=fact*i
    i+=1
print("factorial of ",n,"is",fact)
