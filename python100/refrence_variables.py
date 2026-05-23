# Refrence variables are used to refer to the same object in memory. When you assign a variable to another variable, they both point to the same object. This means that if you change the object through one variable, it will affect the other variable as well.


# PASS BY REFRENCE: In Python, when you pass a variable to a function, you are passing a reference to the object in memory. This means that if you modify the object within the function, it will affect the original object outside the function as well. However, if you reassign the variable within the function, it will not affect the original variable outside the function.


class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
        
        if customer.gender == "male":
            print(f"Hello, Mr. {customer.name}!")
        else:
            print(f"Hello, Ms. {customer.name}!")

# customer1 = Customer("John", "female")
# print(customer1.name)  # Output: John

# greet(customer1)  # Output: Hello, Ms. John!

customer2 = Customer("Alice", "female")
# print(customer2.name)  # Output: Alice
greet(customer2)  # Output: Hello, Ms. Alice!


# class objects are also mutable like lists, dictionaries and sets. When you create an instance of a class, it is stored in memory as an object. If you assign that object to another variable, both variables will refer to the same object in memory. This means that if you modify the object through one variable, it will affect the other variable as well.