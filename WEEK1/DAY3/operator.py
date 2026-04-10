""" Python divides the operators in the following groups:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
# Arithmetic :  for modulus , for exponentiation , for floor dviision below are the symbol:
x = 15
y = 4
print(x % y)
print(x ** y)
print(x // y)

# Division in python:
#- / Division ( return a float)
print(x/y)
# - // floor ( returns a nearest integer)
print(x//y)

# THE walrus operator : Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
# The count variable is assigned in the if statement, and given the value 5:
number = [1,2,3,4,5]
if(count := len(number)) > 3:
    print(f"List has {count} elements")



# logical operator
x = 5
print(x > 3 and x < 10) # in python we dont use symbol we simply write and , or , not

# identity operator : Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
""" x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
"""

""" x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
"""

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

# Membership Operators : Membership operators are used to test if a sequence is presented in an object:
""" 
x = ['apple', 'banana']
print("banana" in x)
returns True because a sequence with the value "banana" is in the list"""

""" x = ["apple", "banana"]
print("pineapple" not in x)
returns True because a sequence with the value "pineapple" is not in the list
"""

# Membership in Strings :The membership operators also work with strings:
# BITWISE OPERATORS: Bitwise operators are used to compare (binary) numbers:

""" 
-The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
-The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
-The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0
"""

# operator precedence
# () >  **  >  +x, -x, ~x  >  * , /, //, %  >   +, -   >  << >>  > &  > ^ > |  > comparison operator > not > and > or
# in sub one left to right precedence is followed



