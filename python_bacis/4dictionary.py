
info={
    "key" : "value", #string
    "name":"samrachana",
    "age": 19, #integer
    "adderess": "lalitpur",
   # "name":"Sharma",  keys cant be duplicate  if made duplicate 
   # python overwrites the old value and prints the new value
    "learning" : "pyhton",
    "is_adult": True, #boolean
    "marks": 99.99, #float
    "subjects": ["python", "java", "C"], #list
    "goals":("Python","numpy","pandas","DSA","SQL") #tuple
}
'''
print("your informatin is ",info)
print(type(info))

#Acessing individual elements
print(info["name"])
print(info["subjects"])
print(info["goals"])
print(info["age"])

##assigning new values
info["age"]=20
print(info)
print(info["age"])

#creating new key-value pair
info["surname"]="Sharma"
print(info)


#NULL/EMPTY dictionary
null_dict = { }
#adding key value to null_dict
null_dict["name"] = "NULL DICTIONARY"
print(null_dict)
print(null_dict["name"])
'''
#Nested dictionary
student = {
    "name": "sam",
    "score":{

        "Maths":100,
        "chemistry":98,
        "physics":99
    }
}
'''
print("Dictionary: ", student)
print("Name: ", student["name"])
print("Score: ", student["score"])
print("Maths: ", student["score"]["Maths"])
print("Physics: ", student["score"]["physics"])
'''

'''
#dictionary methods
print(info.keys())
print(list(info.keys()))
print(len(info))
print(len(list(info.keys())))

print(info.values())
print(list(info.values()))
print(student.values())
print(list(student.values()))
'''

print(student.items())
print(info.items())
print(list(student.items()))
pairs=list(student.items())
print(pairs[0])
print(pairs[1])