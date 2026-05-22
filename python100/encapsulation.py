# Encapsulation is one of the fundamental principles of object-oriented programming. It refers to the bundling of data and methods that operate on that data within a single unit, typically a class. Encapsulation helps to protect the internal state of an object from unintended interference and misuse by restricting access to its components. In Python, encapsulation is achieved through the use of access modifiers, such as public, private, and protected. By convention, a single underscore prefix (e.g., _variable) indicates that a variable or method is intended for internal use (protected), while a double underscore prefix (e.g., __variable) indicates that it is intended to be private and should not be accessed directly from outside the class. Encapsulation allows for better modularity, maintainability, and security of code by controlling how the internal state of an object can be accessed and modified.


# instance variable: A variable that is defined within a class and is associated with an instance of the class. It is used to store data that is specific to each instance of the class. Instance variables are typically defined within the __init__ method of the class and are accessed using the self keyword.

# instance variable example: have different value for different object of the class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age