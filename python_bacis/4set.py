set1={1,2.55,'a',"hello","World"}
set2={1,2,2,2} # no duplicate items in set so it is resolved as {1,2}
print(set1)
print(set2)
print(type(set1))
print(type(set2))
collection1={1,2.55,'a',"hello","World"}
collection2={1,2.55,1,'a',"hello","World","World"}
collection3={1,2.55,1,'a',"hello","World","World",5}
print(collection1)
print(collection2)
print(collection3)
print(len(collection1))
print(len(collection2)) 

nullset= set()
print(type(nullset))
print(nullset)
nullset.add(4)
nullset.add("hello")
nullset.add((1,2,3))# tuple is immutable so it can be passed
#nullset.add([1,2,3,5])#list is mutable so it cant be passed
nullset.remove(4)
# nullset.remove("world")-> error removing the emement that is not present in set
print(nullset)

print(len(nullset))
nullset.clear()
print(len(nullset))

collection={1,"hello", "World", "learning", "pyhton", "coding"}
print(collection.pop())
print(collection.pop())
print(collection)


a={5,6,7}
b={2,6,8}
print(a.union(b))
print(a)
print(b)
print(a.intersection(b))
print(a)
print(b)


sample={9.0,9}
print(sample) #9 and 9.0 are treated as same
sample={9,9.0}
print(sample) #first one is printed 
sample={'9.0',9}
print(sample)
sample={'9',9.0}
print(sample)
sample={("int",9),("float",9.0)}
print(sample)