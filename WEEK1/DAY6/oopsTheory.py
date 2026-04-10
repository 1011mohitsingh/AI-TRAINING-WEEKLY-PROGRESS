"""Python OOP: Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code

Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class. For example:

Class	Objects
Fruit	Apple, Banana, Mango
Car	Volvo, Audi, Toyota

A Class is like an object constructor, or a "blueprint" for creating objects.
# To create a class, use the keyword class:
class MyClass:
  x = 5
# Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

# Now we can delete the object as well using the del keyword:
del p1

# we can create multiple objects from the same class
p1= myClass()  # each object is indpendednt and has its own copy of the class properties
p2= myClass()
p3 = myClass()
print(p1.x)     
print(p2.x)
print(p3.x)

# The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error
eg: class person:
    pass
"""


"""The  __init__() Method: All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.
# why to use : Without the __init__() method, you would need to set properties manually for each object:
# With __init__(), you can set initial values when creating the object


# We can also set the default value for parameters in the __init__() method.
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# multiple parameters : The __init__() method can have as many parameters as you need:
"""


"""#The self parameter : It is a reference to the current instance of the class.
It is used to access properties and methods that belong to the class.
# Note: The self parameter must be the first parameter of any method in the class.
# Without self, Python would not know which object's properties you want to access .The self parameter links the method to the specific object:

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
# Note: While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
# You can access any property of the class using self: Access multiple properties using self:


# calling methods with the self
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hello, my name is " + self.name
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to the world of Python OOP.")

p1 = Person("Emil")
p1.welcome()
# """

# Learn class properties and the class Methods form the w3 school itself.

# class Methods : __str__method is used to return a string representation of the object when the object is printed. It is called when you use the print() function on an object of the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)


# Pillars of oop in python : Inheritance, polymorphism, encapsulation, and abstraction are the four main pillars of object-oriented programming (OOP) in Python. These concepts help to create a more organized and efficient code structure.  
"""Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.


# Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

Use the Student class to create an object, and then execute the printname method:
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# Add a correct year parameter and pass the correct year when creating an object of the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
"""