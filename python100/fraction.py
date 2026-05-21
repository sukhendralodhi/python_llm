class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.denom = denominator


x = Fraction(1, 2)
print(type(x))

# Magic method in python is a special method that is called when an object of the class is created. It is used to initialize the attributes of the object. The __init__ method is a constructor method that is called when an object of the class is created. It is used to initialize the attributes of the object. In the above example, we have defined a class called Fraction with two attributes: num and denom. The __init__ method takes two parameters: numerator and denominator, which are used to initialize the num and denom attributes of the Fraction object when it is created.

# __init__ is a constructor method that is called when an object of the class is created. It is used to initialize the attributes of the object. In the above example, we have defined a class called Fraction with two attributes: num and denom. The __init__ method takes two parameters: numerator and denominator, which are used to initialize the num and denom attributes of the Fraction object when it is created.

# __str__ is a magic method that is called when we want to represent the object as a string. It is used to define how the object should be represented as a string. In the above example, we have defined the __str__ method to return a string representation of the Fraction object in the form of "numerator/denominator". When we print the Fraction object, it will call the __str__ method and return the string representation of the object.

# example of using __str__ method in the Fraction class:  

class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.denom = denominator

    def __str__(self):
        return f"{self.num}/{self.denom}"   
    

x = Fraction(1, 2)
print(x)