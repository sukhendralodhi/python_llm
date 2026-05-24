# Types of Inheritance in Python
    # 1. Single Inheritance
    # 2. Multiple Inheritance
    # 3. Multilevel Inheritance
    # 4. Hierarchical Inheritance
    # 5. Hybrid Inheritance


# Single Inheritance

# CLASS A:  => # CLASS B(A):



class Parent:

    def __init__(self):

        self.num = 100

class Child(Parent):

    def __init__(self):

        super().__init__() # calling parent class constructor

        self.val = 200  


# Multi level Inheritance


# Class A: => Class B(A) => Class C(B)

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

# Note: In multi level inheritance, child class can access parent class variable and also grand parent class variable because of super keyword. It will call parent class constructor and initialize parent class variable in child class object.


# Hierarchical Inheritance

# Class A: => Class B(A) and Class C(A) 
class Parent:

    def __init__(self):

        self.num = 100

class Child1(Parent):

    def __init__(self):

        super().__init__() # calling parent class constructor

        self.val1 = 200 
    
class Child2(Parent):

    def __init__(self):

        super().__init__() # calling parent class constructor

        self.val2 = 300


# Multiple Inheritance

# Class A: => Class B and Class C => Class D(B,C)

class Parent1:

    def __init__(self):

        self.num1 = 100

class Parent2:

    def __init__(self):

        self.num2 = 200

class Child(Parent1, Parent2):

    def __init__(self):

        super().__init__() # calling parent class constructor
        self.val = 300

# Note: In multiple inheritance, child class can access variable of both parent class because of super keyword. It will call parent class constructor and initialize parent class variable in child class object.


# Hybrid Inheritance

# Class A: => Class B(A) and Class C(A) => Class D(B,C)

