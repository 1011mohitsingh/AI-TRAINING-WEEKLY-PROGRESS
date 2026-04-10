# It helps in the code reusability and also helps in the code organization. It is a way to create a new class from an existing class. The new class is called the child class or subclass, and the existing class is called the parent class or superclass.
# eg: supose we had to create interface and work for the student and instructor so fo rthe student we had to do login , reg, enorll, renew and for the instructor login , reg, create, answer something like thtat so you can look that login and reg is repeating and here the comes of the inheritance where you cant just create one class in which two method with the login and reg should be there and then we creat two class one for student and one for instructor and then we can just inherit the login and reg method from the parent class and then we can create the other method in the child class so that we can avoid the code repetition and also we can organize our code in a better way.

# things we inherit : data members(variables) and member functions(methods), and constructors are not inherited but we can call the constructor of the parent class in the child class using super() function. Also private members are not inherited but we can access them using getter and setter methods.

class User: # parent class
    def login(self):
        print("Login")
    
    def register(self):
        print("Register")

class Student(User):# child class
    def enroll(self):
        print("Enroll")
    
    def review(self):
        print("Review")

stu1 = Student()
stu1.enroll()
stu1.review()
stu1.login() # we can access the login method of the parent class   
stu1.register() # we can access the register method of the parent class

# ---------------------------------------------------------------------------------------------------------------------------

# If there is no constructor in the child class then the constructor of the parent class is called automatically when we create an object of the child class. But if there is a constructor in the child class then the constructor of the parent class is not called automatically and we have to call it explicitly using super() function.
class Phone:
    def __init__(self, price , brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):
    pass

s = Smartphone(10000, "Samsung", "12MP")
print(s.price) # 10000
print(s.brand) # "Samsung"
print(s.camera) # "12MP"

## Method overloading -> polymorphism -> same method name but different parameters
# Method overriding -> polymorphism -> same method name and same parameters but different implementation in the child class
# operator overloading -> polymorphism -> same operator but different implementation in the child class


# If child has no constructor then parent constructor is called automatically but if child has constructor then parent constructor is not called automatically and we have to call it explicitly using super() function.
class Phone:
    def __init__(self, price , brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")
              
class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy() 

s = Smartphone(10000, "Samsung", "12MP")
s.buy() # output: Buying a phone 
                # Buying a smartphone

