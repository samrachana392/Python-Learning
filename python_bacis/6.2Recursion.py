'''def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end of show(n) where n = ", n)
show(10)'''

'''#wap to print factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
x=int(input("Enter x: "))
print(fact(x))'''

'''#wap to print sum of first n natural numbers using recursion
def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)
x=int(input("Enter x: "))
print(sum(x))'''

#WAP to print all elements of list using recursion
def print_list(lst,idx):
    if(idx==len(lst)):
        return
    print(lst[idx])
    print_list(lst,idx+1)
fruits=["apple","mango","orange","grapes","papaya"]
print_list(fruits,0)