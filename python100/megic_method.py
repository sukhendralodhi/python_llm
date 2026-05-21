# Magic Method in Python

# Magic methods in Python are special methods that have double underscores at the beginning and end of their names. They are also known as dunder methods (short for "double underscore"). These methods allow us to define the behavior of our objects in certain situations, such as when we want to perform arithmetic operations, compare objects, or represent our objects as strings.

# Note: We can not call constructor method directly, it is called automatically when we create an object of the class. However, we can call other methods directly on the object.

# Constructors are special methods that are called when an object is created. They are used to initialize the attributes of the object. The constructor method in Python is defined using the __init__ method.

# Use of constructor method in Python is to initialize the attributes of the object when it is created. For example, if we have a class called Person, we can use the constructor method to initialize the name and age attributes of the Person object when it is created.


# self in Python is a reference to the current instance of the class. It is used to access the attributes and methods of the class within the class itself. When we define a method in a class, we need to include self as the first parameter of the method. This allows us to access the attributes and methods of the class using self within the method.

# CLASS HAS ONLY DATA AND METHODS 

# that do access only class objects. It does not have any access to the outside world. It is a blueprint for creating objects. It defines the properties and behaviors that the objects created from the class will have. A class can be thought of as a template for creating objects.

# in the class method do not access other method in the class, it only access the class objects. for accessing other method in the class we need to use self keyword. for example:
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def birthday(self):
        self.age += 1
        return f"Happy birthday! You are now {self.age} years old." 
    
    
# In the above example, we have a class called Person with two attributes: name and age. We also have two methods: greet and birthday. The greet method returns a string that introduces the person, while the birthday method increments the age attribute by 1 and returns a string wishing the person a happy birthday.