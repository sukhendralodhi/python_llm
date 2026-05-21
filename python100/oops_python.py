# object oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for the creation of reusable and modular code, making it easier to manage and maintain.

# What is an object?
# An object is an instance of a class. It is a self-contained unit that contains data and behavior. Objects can represent real-world entities, such as a person, a car, or a bank account.

# what is a class?
# A class is a blueprint for creating objects. It defines the properties and behaviors that the objects created from the class will have. A class can be thought of as a template for creating objects.

# Generality to Specificity
# In OOP, we can create a general class that defines common properties and behaviors, and then create specific classes that inherit from the general class. This allows us to reuse code and avoid duplication.

# What is object literal?
# Object literal is a way to create an object in Python using curly braces {}. It allows us to define properties and values directly within the object. For example:


list = [1, 2, 3, 4, 5]
number = 10


# What is function vs method?
# A function is a block of code that performs a specific task and can be called independently. A method, on the other hand, is a function that is associated with an object and can only be called on that object. Methods are defined within a class and can access the properties of the object they belong to.

class Atm:

    def __init__(self):

        self.balance = 0
        self.pin = ""

        self.menu()

    def menu(self):

        user_input = input("""
        Hello, how would you like to proceed?
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
                           
        Enter your choice:
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()
        else:
            print("Invalid input")
            self.menu()

    def create_pin(self):
        new_pin = input("Enter new pin:")
        self.pin = new_pin
        print("Pin created successfully")

    def deposit(self):

        entered_pin = input("Enter your pin:")

        if entered_pin != self.pin:
            print("Incorrect pin")
            self.menu()
        else:
            amount = int(input("Enter amount to deposit:"))
            self.balance += amount
            print(f"Deposit successful. Your new balance is {self.balance}")

    def withdraw(self):
        entered_pin = input("Enter your pin:")
        if entered_pin != self.pin:
            print("Incorrect pin")
            self.menu()
        else:
            amount = int(input("Enter amount to withdraw:"))
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is {self.balance}")

    def check_balance(self):
        entered_pin = input("Enter your pin:")

        if entered_pin != self.pin:
            print("Incorrect pin")
            self.menu()
        else:
            print(f"Your balance is {self.balance}")

    def exit(self):
        print("Thank you for using our ATM. Goodbye!")


atm = Atm()