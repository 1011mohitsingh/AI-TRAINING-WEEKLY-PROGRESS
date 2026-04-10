# List are used to store multiple items in a single variable. 
thislist = ["apple","banana","cherry"]
print(thislist)

# list items are ordered(means they are ordered as it has defined order and that order will not change, if you add new item to a list, the new iterms will be placed at the end of the list), changeable, and allow duplicate values
# List items are indexed, the first item has index [0] the second has [1] and so on.

# there are methods list methods we can say that can change the order of the the list. such as append , prepend or something liek that if it is in python
# we use len() method to know the length of the list

# Datatype : List items can be of any data type, Also it can contain differenct means mix of hte datatype as well. Eg :  list1 = ["abc", 34, True, 40, "male"]
# From Python's perspective, lists are defined as objects with the data type 'list':

# we can make the list using the list() constructor as well when we create a new list
"""this list = list(("apple","banana","cherry"))
print(thislist)   output : ["apple", "banana", "cherry"]
""" 

# Access items: List items are indexed and you can access them by referring to the index number. The first index has index 0
# And negative indexing means start from the end , We can do the range of indexes as well in which we can start the start and the end range as well.

# check if item exists 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# to change the item value in the list
thislist = ["apple", "banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# you can replace the value as well as by passing the index and givng with the range. either it will replace it and when we insert more values then it will add at that positions as well.
""" thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
"""

# insert items
""" thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) """

# Append Items: To add an item in the end of the list, use the append() method   eg : thislist.append("orange")
# Insert Items : To insert an list item at a specified index, use the insert() method   eg: thislist.insert(1, "orange")


# extend list: To append elements for another list to the current list, we use the extend() method
"""
Add list items - extend list
 append() method we use to add an item to an end of the list
 insert(1, orange) in which index is passes to insert a item at a specific index
 Extend List: add the elemenets of one list to the second list"""
 

## Remove list items: Remove specific item
"""
remove() methods removes the specified item form list : if there are multiple same elements present so it removes the first occurance in the list
To remove ths second item we use list.pop(1) and in the arguments we had to pass the index of which index the elemnts you wanna remove
If we not specify the index so the pop() method removes the last item
we can use the del keyword as well, del list[0] so it removes the element at th 0 index okkay.
we can delete the entire list using this command: del thislist
to clear the list : list.clear()
"""

## Python loop lists
# for loop
thislist = ["apple", "banana","cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers
for i in range(len(thislist)):
    print(thislist[i])

# while loop
i =0
while i < len(thislist):
    print(thislist[i])
    i = i+1

# looping using list comprehension : It offers the shortest syntax for looping through lists.
[print(x) for x in thislist]

# list comprehension : if offers a shorter syntax and what to create a new list based on the values of the existing list
fruits = ["apple","banana","cherry","kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# now using list comprehension we can do that 4 line of code to only one line of code:
print(x for x in fruits if "a" in x)   # SYNTAX : newlist = [expresion for item in iterable if condition == true]   output : return value is a new list, leaving the old list unchanged

# Expression : Is the current item in the iteration but also the outcome which you can manipulate before it end up list a list item in the new list:  new list = [x.upper() for x in fruits]

# sort lists
thislist.sort() # sort() method will sort alpanumerically, ascending by default
thislist.sort(reverse = True)  # this sort list in the descending order

# custmize sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)   # IN this it foud the abs value and accroding to that it sort but the point key of the list is shown in the list okkay in python
print(thislist)

# Note : sort() method is case sensitive , resulting in all capital letters being sorted before lower case letters
# we can perform the case- insensitive sort of the list as well such as thislist.sort(key = str.lower)

# Reverse order : reverse() method reverses the current storing order of the elements

# Copy lists
# copy() method is used to copy the list such as mylist = thelist.copy() as You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# list() method is also used that is built-in-method to make a copy of it, mylist = list(thislist)
# use of slice() : operator  eg- mylist = thelist[:]
# join two list: using + operator, using append , using extend




