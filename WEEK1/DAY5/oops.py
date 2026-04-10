# This is the repo that contains the playlist that I followed for the oops practical learning & implementation and I learned from campusx - 4hr one shot

# Here we are creating one class that is the implementation of the Atm where we can do some opeations and basic things we do so that for the better understanding okkay such pin, check balance, deposit , widhraw and all

class Atm:
    # constructor is a special method that is written inside code is automatically executed when we create an object of the class okkay.
    # constrcutor is a special method/ magic / dunder methods. Magic methods is a predefined methods. Magic methods is not called by 0bject okkay, on a given criteria it is called automatically.
    # eg: connect to the internet, connect gps , s owe write those code in the constructor and when we create the object of the class it will automatically execute the code inside the constructor and it will connect to the internet, gps and all those things okkay. So that is the use of constructor.
    def __init__(self): # bydefault the naming of the constructor will be the same
        self.__pin = ""
        self.__balance = 0

        self.menu()
     
    def menu(self):
        while True:
            user_input = input("""
                                Hello, how would you like to proceed?
                            1. Enter 1 to create a pin
                            2. Enter 2 to deposit
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to exit
    """)
            
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            else:
                print("bye")
        
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin: ")

        if (temp == self.__pin):
            amount = int(input("Enter the amount"))
            if amount <= self.__balance:
                self.__balance = self.__balance-amount
                print("Operation successful")
            else:
                print("Insuffient balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if (temp == self.__pin):
            print(self.__balance)
        else:
            print("Invalid pin")

# To run this save the file and just in the another file import the method from the class and then run then just create the object it will give the other thing
# self: use of self is used to access the variable and method of the class . In oop there is a data and function in the class and their data can only be accesses by their objects. So self donote the object that is created from the class okkay. So when we create the object of the class then we can access the variable and method of the class by using self. So that is the use of self. It is a convention to use self but we can use any name instead of self but it is a convention to use self okkay. So that is the use of self.


## Instance variable - variable that is created inside the constructor and it is accessed by using self. It is also called as object variable because it is accessed by using the object of the class okkay. So that is the use of instance variable.
# or It is a value of variable which is different for different objects of the class.