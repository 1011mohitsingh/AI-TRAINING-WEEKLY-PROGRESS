# python dictionaries
tempdict = {
    "brand": "ford",
    "model" : "Mustang",
    "year" : 1964
}
# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# After version 3.7, dictionaries are ordered. In python 3.6 and earlier , dictionaries are unordered . Also the data type of the dictionary is the dict

# The dict() constructor : It is used to make a dictionary
thisdict = dict(name = 'john', age = 36, country = "Norway")
print(thisdict)

# Acessing items : we can access the items of dictionary by referring to its key name, inside square brackets
x = dict["model"]
# or we can use the get() method to get and access the value of the key
x = tempdict.get("model")

# get keys method that return all the keys of the dictionary
x = tempdict.keys()

# same as key we can get the list of the values as well so for that we use values() method
x = tempdict.values()

# items() method will return each items in a dictionary, as tuples in a list
z = tempdict.items()
print(z)  #output : dict_items([('brand', 'ford'), ('model', 'Mustang'), ('year', 1964)])

# we use the if key Exists : to determine if a specified key present in a dictionary use the in keyword
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
"""

# change dictionary items
thisdict["year"] = 2018

# or we can use the update() method just to update the items from the given argument in a dictionary
thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year":1994
}
thisdict.update({"year":2020})

# Removing items: There are methods to remove the items from a dictionary
thisdict.pop("model")

# popitem() this method is ued to removes the last inserted item , a random item is removed instead
thisdict.popitem()

# del : The del keyword removes the item with the specified key name:
del thisdict["model"]
# And it is also able to delete the dictionary as well completely
del thisdict

#clear() method emptities the dictionary
thisdict.clear()


# looping the dictionary : we can use the for loop for that and the return values are the keys of the dictionary but there are methods to return the values as well.
for x in thisdict:
    print(x)

# to print all value one by one we can use this code instructions
for x in thisdict:
    print(thisdict[x])

# As it return the key so if we want to see the values as well so we can use the values() along with that to see the values of the dictionary:
for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x) # this is used to return the keys of a dictionary

for x,y in thisdict.items():
    print(x,y)



### Python copy dictionaries
# we can use the copy() method to make a copy of the dictionary
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)
print(mydict)

#Nested dictionaries
myfamily = {
    "child1" : {
        "name" : "Mohit",
        "year" : 2004
    },
    "child2" : {
        "name" : "Simran",
        "year" : 2005
    },
}

#To acess items in a Nested Dictionaries
print(myfamily["child2"]["name"])

# how to loop through the nested dictionaries
for x, obj in myfamily.items():
    print(x)
for y in obj:
    print(y+':',obj[y])






