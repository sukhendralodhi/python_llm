# Multilevel inheritance is a type of inheritance in which a child class inherits from a parent class, and then another child class inherits from that child class. This creates a chain of inheritance where the grandchild class can access the properties and methods of both the parent and child classes.

# Example of multilevel inheritance:

class Parent:

    def __init__(self):

        self.num = 100

class Child(Parent):

    def __init__(self):

        super().__init__() # calling parent class constructor

        self.val = 200

class GrandChild(Child):

    def __init__(self):

        super().__init__() # calling parent class constructor

        self.grand_val = 300


son = GrandChild()
print(son.num) # accessing parent class variable using grand child class object is possible because of super keyword. It will call parent class constructor and initialize parent class variable in grand child class object.
print(son.val) # accessing child class variable using grand child class object is possible because of super keyword. It will call child class constructor and initialize child class variable in grand child class object.
print(son.grand_val) # accessing grand child class variable using grand child class object is possible because of super keyword. It will call grand child class constructor and initialize grand child class variable in grand child class object.