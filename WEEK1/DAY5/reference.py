# PASS BY REFERENCE: when a function gets the actual object/reference, so changes made inside the function affect the original object outside the function.  In Python, it is more accurately called “pass by object reference” because Python passes the reference to the object, not a copy of the object.
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


    def greet(customer):
        if customer.gender == "Male":
            print("Hello", customer.name,"sir")
        else:
            print("Hello", customer.name,"ma'am")

        cust2 = Customer("Nitish","Male")
        return cust2

cust = Customer("John", "Male") 
print(cust.name) # John

new_customer = cust.greet()
print(new_customer.name) # Nitish

# class ke objects are also mutable just like lists , dict and sets.