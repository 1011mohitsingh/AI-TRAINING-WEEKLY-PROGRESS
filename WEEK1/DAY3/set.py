# set are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed and donot allow duplicate values. A Set is a collection which is unordered, unchangeable and unindexed. but the thing is that we can add and remove items
# It is represented with the curly brackets.

# Once a set is created, you cannot change its items, but you can remove items and add new items.
# Duplicate values are ignored in the set in python. Also True and 1  and False and 0 are treated as same in the set and if it appears in same set so one of them will be ignored.

# LENGTH: Len()
# It is also unindexed and no duplicate members

# python access Items: 
"""" you can't access the iterms in a set by referring to an index or a key. But you can loop using for loop and by using in keyword we can check if specified value is present or not
thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)

To check if specific string in present in the set or not:
thisset = {"apple","banana","cherry"}
print("banana" in thisset)
print("watermelon" not in thisset)
"""

"""  add items : Once a set is created, you cannot change its items, but you can add new items. To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

The object in the update() method does not have to be a set, it can be any iterable object.
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
"""

# REMOVE SET ITEMS : we use the remove() and the discard() method in the set
# note if that item not present in the set it will throws an error.
# vice versa in the case of discard() it will not throw an error

# You can also use the pop() method to remove an item, but this method will remove a random such as thisset.pop() so it will remove any iterms randomly from the set

# clear method - it empties the set
# del keyword - it delecte the set completely.
# we can use loop for iterating in the set


# https://www.w3schools.com/python/python_sets_join.asp    . you can refer for reading the whole join set and what we us and join it.
# There are several ways to join two or more sets in Python.
"""
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates."""

# Join a Set and a Tuple : The union() method allows you to join a set with other data types, like lists or tuples.
# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

"""" union() → combines all unique items from both sets
Example: {1, 2}.union({2, 3}) → {1, 2, 3}

update() → adds all items from another set into the first set (changes original set)
Example:

a = {1, 2}
a.update({2, 3})
print(a)   # {1, 2, 3}
intersection() → keeps only common items
Example: {1, 2, 3}.intersection({2, 3, 4}) → {2, 3}
difference() → keeps items from first set that are not in second
Example: {1, 2, 3}.difference({2, 4}) → {1, 3}
symmetric_difference() → keeps items that are in either set, but not both
Example: {1, 2, 3}.symmetric_difference({2, 3, 4}) → {1, 4}"""

# PYTHON FROZENSET
# frozenset is an immutable version of the set , like sets it contains unique, unorderd , unchangeable elements. 
""" using the frozenset constructor to crate a frozen set from any iterable
    x = frozenset({"apple","banana", "cherry"})
    print(x)
    print(type(x))"""

# check the readme of the week 1 to go with the frozen set METHODS OKKAY THERE ARE MANY SO THAT WE CAN DO THE OPERATION IN THE FROZEN SET METHODS.