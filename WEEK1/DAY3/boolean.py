# boolean value in python means either true or false value
#  When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10>9)
print(10 == 10)

# printing based on the condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("hello"))

# Most Values are True : Any string is True, except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones or the NONE Value or 0 or False results to false.
# You can create functions that returns a Boolean Value:
def my_function():
  return True
print(my_function)

# isinstance() function, which can be used to determine if an object is of a certain data type: which return the boolean value
x = 200
print(isinstance(x, int)) # it return the true value




