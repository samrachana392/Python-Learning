'''#write a function(WAF) to print the length of a list (list is the parameter)
def length(list):
   # print(len(list))
    return len(list)

var=[1,67,"Sam","San",71]
len=length(var)
print("length of the list is: ", len)

#WAF to print the element of a list in a single line
def elements(lst):
    for item in lst:
        print(item, end=" ")
       
var=[1,67,"Sam","San",71]
elements(var)

#WAF to find the factorial of n
def factorial(n):
    fact=1
    i=1
    #while(i<=n):
    #    fact=fact*i
    #    i+=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ", n, "is", fact)
n=int(input("enter a n: "))
factorial(n)

#WAF to convert USD into NPR
def usd_to_npr(usd):
    npr=usd*140
    print(usd,"in nepali rupees is", npr)
usd_to_npr(5)
usd_to_npr(4.99)
usd_to_npr(12)
usd_to_npr(12*8)
usd_to_npr(12*8*4)
usd_to_npr(12*8*4*4) '''

#WAF that takes a number input and retrns odd or even accordingly
def odd_even():
    n=int(input("Enter n: "))
    if(n%2==0):
        return("EVEN")
    else:
        return "ODD"
result=odd_even()
print(result)