# IN python __ is used to make a variable private
# When we write __pin so it represnted  as python with this _Atm__pin 
# Nothin in python is truly private but it someone use the same variable -Atm__pin so it is easily omitable so thats why nothing is private.
# As we had hidden so __pin so now we will make te method so that one can access it and second one can make it edit okkay thats it. This is how the python works man and that term in python is known as getter and setter.
# Need of encapsulation is that none can ommit the methods variable so we protect it by first converting it to the private attribute and then we add getter and setter so that we can access and omit the valye of the method variable.
# private atrributes : __ used with the data as well as method so that other can change and omit it.
# class diagram in which at the top there is a class name and that is Atm and then comes the attibutes which is represented by the varibale in front of that if they are private so we add - in the front of it. Also at the last in the classdiagram so we have methods such as __init__(), menu, change_pint(), deposit, withdraw, checkbal so we had to add + means they are public and they are added at the fron of the skeletan class diagram vaiable name.


class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()

        def get_pin(self):
            return self.__pin
        
        def set_pin(self, new_pin):
            if type(new_pin) == str:
                self.__pin = new_pin
                print("Pin changed successfully")
            else:
                print("Invalid pin type")

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


## Reference variable is a variable which is used to refer the object of the class. So when we create the object of the class we have to store it in some variable so 
# that we can access the methods and attributes of the class through that variable okkay. So that variable is known as reference variable.  eg = sbi = Atm() so here sbi is the refernece variable.

