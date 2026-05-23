# Instance variable => that value is different for every object

# ex. pin, balance

# Static Variable (Class Variable) => a variable that have same value for every object
# 
# Note: Static variable always created outside of the constructor
# 
# 
class Atm:

    # static variable 
    __counter = 1

    def __init__(self):

        # instance variable 
        self.__pin = "" 
        self.__balance = 0 
        self.sno = Atm.__counter # if we access instance variable then we write self.variable name but if we access static variable then we write class name.variable name (Atm.counter)

        Atm.__counter = Atm.__counter+1

    @staticmethod # this is sign for denoting this is a static method
    def get_counter(): # a method that dealing with static variable we do not need self for that
        return Atm.__counter
    
    @staticmethod # this is sign for denoting this is a static method
    def set_counter( new_counter):
        if type(new_counter) == int:
            Atm.__counter = new_counter
        else:
            print("Not Allowed")

# c1 = Atm()
# print(c1.counter)
# c2 = Atm()
# print(c2.counter)
# c3 = Atm()
# print(c3.counter)

# print(Atm.get_counter())
# Atm.set_counter(20)
# print(Atm.get_counter())

# Class shows two type relationship

# Relationship
# 1. Aggregation Relationship (Has - A Relationship)
# 2. Inheritance Relationship (is - A Relationship)

# THIS IS A AGGREGATION 

# customer (class)  =>  has - a => address (class)


# Example 

# THIS IS A INHERITANCE 

#  product class
#       |
#     Is - A 
#       | 
# smartphone class 