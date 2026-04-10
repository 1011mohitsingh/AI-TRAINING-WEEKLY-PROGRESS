# Tuple: Tuples are used to store multiple items in a single variable and it is a collection which is ordered and unchangeable

""" Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
Example
One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) """

# Python - Update Tuples
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Add Items
"""Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
2. 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:"""

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items , Convert the tuple into a list, remove "apple", and convert it back into a tuple:

# The del keyword can delete the tuple completely , del thistuple

""" Python - Unpack Tuples : When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
 fruits = ("apple", "banana", "cherry")
 But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
 fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

"""

# join tuples : 
# To join two or more tuples you can use the + operator

# If you want to multiply the content of a tuple a given number of times, you can use the * operator
"""fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)"""

# Tuple Methods
"""Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)"""
