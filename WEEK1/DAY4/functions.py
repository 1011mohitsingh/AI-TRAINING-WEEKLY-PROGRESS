# A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoiding code repetition.
# functions name are just like naming the variable

# A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

""" From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called."""

def my_function(name): 
  print("Hello", name)

my_function("MOHIT SINGH") 
# We have to give the exact no of arguments to the no of parameter defined if it vary then it will give an error

# DEFAULT PARAMETER VALUES : You can assign default values to parameters. If the function is called without an argument, it uses the default value
def my_function(name = "friend"):
  print("Hello", name)

my_function("Mohit")
my_function("Simran")
my_function()

# keyword arguments: you can send the arguments with the key = value syntax
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
  
my_function("dog","buddy")

# Positional Arguments
"""When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:

Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")"""


#  Mixing Positional and Keyword Argument . You can mix positional and keyword arguments in a function call. However, positional arguments must come before keyword arguments:

# Passing Different Data Types .You can send any data type as an argument to a function (string, number, list, dictionary, etc.). The data type will be preserved inside the function:
"""Example
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

"""

# we can return the function as well with some value, data types and alll.

"""You can specify that a function can have ONLY positional arguments.  To specify positional-only arguments, add , / after the arguments:

Example
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

Example
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")


Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:

Example
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

Example
def my_function(name):
  print("Hello", name)

my_function("Emil")

Combining Positional-Only and Keyword-Only
You can combine both argument types in the same function.

Arguments before / are positional-only, and arguments after * are keyword-only:

Example
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
"""

## Python *args and **kwargs ( Arbitrary arguments)
""" By default, a function must be called with the correct number of arguments. However, sometimes you may not know how many arguments that will be passed into your function. *args and **kwargs allow functions to accept a unknown number of arguments.
If you do not know how many arguments will be passed into your function, add a * before the parameter name. This parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# You can combine regular parameters with *args. Regular parameters must come before *args:
eg : def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
In this example, "Hello" is assigned to greeting, and the rest are collected in names

"""

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name. This way, the function will receive a dictionary of arguments and can access the items accordingly:

""" def my_function(**kid):
      print("His last name is "+ kid["lname"])
      
      my_function(fname = "Tobias", lname = "Refsnes")

The **kwargs parameter allows a function to accept any number of keyword arguments. Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

eg : unction(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
      """


""" Combining *args and **kwargs
You can use both *args and **kwargs in the same function.

The order must be:

regular parameters
*args
**kwargs
Example
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
"""



""" 
Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:
Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


Unpacking Dictionaries with **
If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

Example
Using ** to unpack a dictionary into keyword arguments:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")


 Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.
"""


"""A variable is only available from inside the region it is created. This is called scope.
Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
Function Inside Function : As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.
Naming Variables : If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.

To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

## The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.


# The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
eg : x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

"""


