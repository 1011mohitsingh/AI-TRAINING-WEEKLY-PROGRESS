# Types of inheritance:
# 1. Single inheritance -> when a child class inherits from a single parent class.
# 2. Multiple inheritance -> when a child class inherits from multiple parent classes.
# 3. Multilevel inheritance -> when a child class inherits from a parent class and then another child class inherits from the first child class.
# 4. Hierarchical inheritance -> when multiple child classes inherit from a single parent class. ( not supported in java but supported in python)
# 5. Hybrid inheritance -> when a child class inherits from multiple parent classes and also has its own methods and attributes.


# single level inheritance
class Phone:
    def __init__(self, price , brand, camera):
        self._price = price
        self._brand = brand    
        self._camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

class Smartphone(Phone):
    pass

Smartphone1 = Smartphone(10000, "Samsung", "12MP")
print(Smartphone1._price) # 10000


## Multilevel inheritance
class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self, price , brand, camera):
        self._price = price
        self._brand = brand    
        self._camera = camera

    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):
    pass

s = Smartphone(10000, "Samsung", "12MP")
p = Phone(5000, "Nokia", "8MP")

s.buy() # output: Buying a phone
s.review() # Product customer review
p.review() # Product customer review


## Hierarchical inheritance
class Phone:
    def __init__(self, price , brand, camera):
        print("Inside phone constructor")
        self._price = price
        self._brand = brand    
        self._camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

class Smartphone(Phone):
    pass

class FeaturePhone(Phone):
    pass

Smartphone1 = Smartphone(10000, "Samsung", "12MP")
FeaturePhone1 = FeaturePhone(5000, "Nokia", "8MP")

Smartphone1.buy() # output: Buying a phone
FeaturePhone1.buy() # output: Buying a phone
Smartphone1.return_phone() # output: Returning a phone
FeaturePhone1.return_phone() # output: Returning a phone

## multiple inheritance
class Phone:
    def __init__(self, price , brand, camera):
        print("Inside phone constructor")
        self._price = price
        self._brand = brand    
        self._camera = camera

    def buy(self):
        print("Buying a phone")

class product:
    def review(self):
        print("Product customer review")

class Smartphone(Phone, product): # multiple inheritance implemented
    pass

s = Smartphone(10000, "Samsung", "12MP")
s.buy() # output: Buying a phone
s.review() # output: Product customer review


# MRO (Method Resolution Order) -> it is the order in which the methods are resolved in case of multiple inheritance. It is determined by the C3 linearization algorithm. It is used to determine the order in which the methods are called when there are multiple methods with the same name we can see the example in our scenario as well in which threr eare two buy methods are there but phone method is callled first before the product method because of the MRO. We can check the MRO of a class using the __mro__ attribute or the mro() method. The MRO of a class is determined by the order of the parent classes in the class definition. The MRO of a class is determined by the C3 linearization algorithm which is a method resolution order algorithm that is used to determine the order in which the methods are called when there are multiple methods with the same name. The C3 linearization algorithm is based on the concept of a directed acyclic graph (DAG) and it ensures that the order of the methods is consistent with the order of the parent classes in the class definition. The C3 linearization algorithm is used to determine the MRO of a class and it ensures that the order of the methods is consistent with the order of the parent classes in the class definition. The C3 linearization algorithm is used to determine the MRO of a class and it ensures that the order of the methods is consistent with the order of the parent classes in the class definition.

# method overloading
class Geometry:
    def area(self, a, b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b
    
obj = Geometry()
obj.area(4)
obj.area(4,5)

# operator overloading
'Hello' + ' World' # output: 'Hello World'

#or 
# from fraction import Fraction
# f1 = Fraction(1, 2)
# f2 = Fraction(1, 3)
# print(f1 + f2) # output: 5/6

