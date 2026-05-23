
# 🔹 Polymorphism in Python OOP

# Polymorphism means "many forms".

# In Object-Oriented Programming, polymorphism allows the same method name to behave differently for different objects.



# Types of Polymorphism in Python
    # 1. Method Overriding (Runtime Polymorphism)
    # 2. Method Overloading (Python handles differently)
    # 3. Operator Overloading



# 1. Method Overriding (Runtime Polymorphism)
class Phone:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):

    def buy(self):
        print("Buying a smartphone")


# s = Smartphone("Apple", 80000)

# s.buy()

# isko bola jata hai methid overriding => Polymorphism

# agar same name se method hai parent and child class me to child class apne method call kregi but agar child class ke pass apna method ni hai tab bo parent class ka method call kregi 


# 2. Method Overloading (Python handles differently)