# Recursion : Recursion is when a function calls itself. Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

"""
A simple recursive function that counts down from 5:

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)"""

"""Base Case and Recursive Case
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
"""

# fibonacci sequence:
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# Recursion with list
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


""" Recursion Depth Limit
Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

Example
Check the recursion limit:

import sys
print(sys.getrecursionlimit())

If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:

Example
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
"""


""" Python Generators:Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

# REFER THE W3 SCHOOL DOCUMENTATION
"""