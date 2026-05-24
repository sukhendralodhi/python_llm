
# The super() function is used to access methods or constructors of the parent class inside the child class.

# 🔹 Why Use super()?
#  1. Call parent constructor
#  2. Reuse parent methods
#  3. Avoid rewriting code
#  4. Maintain inheritance properly

# Note: super() keyword ko class ke bahar use nahi kiya jata.
# Note: super() keyword se parent class ke methods aur constructor ko access kar sakte hain.
# Note: super() keyword se parent class ke attributes bhi indirectly access kar sakte hain.


class Parent:

    def __init__(self):
        print("Parent constructor")


class Child(Parent):

    def __init__(self):
        super().__init__()   # calling parent constructor
        print("Child constructor")


obj = Child()


class Phone:

    def __init__(self, price, brand, camera):

        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):

    def buy(self):
        print("Buying smartphone")
        super().buy() # super ko call krne par parent ka method invoke hoga


# s = Smartphone(2000, "Apple", 15)

# s.buy()