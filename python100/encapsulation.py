# Encapsulation is one of the fundamental principles of object-oriented programming. It refers to the bundling of data and methods that operate on that data within a single unit, typically a class. Encapsulation helps to protect the internal state of an object from unintended interference and misuse by restricting access to its components. In Python, encapsulation is achieved through the use of access modifiers, such as public, private, and protected. By convention, a single underscore prefix (e.g., _variable) indicates that a variable or method is intended for internal use (protected), while a double underscore prefix (e.g., __variable) indicates that it is intended to be private and should not be accessed directly from outside the class. Encapsulation allows for better modularity, maintainability, and security of code by controlling how the internal state of an object can be accessed and modified.


# instance variable: A variable that is defined within a class and is associated with an instance of the class. It is used to store data that is specific to each instance of the class. Instance variables are typically defined within the __init__ method of the class and are accessed using the self keyword.

# instance variable example: have different value for different object of the class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# private variable: A variable that is defined within a class and is intended to be accessed only within the class itself. In Python, private variables are typically denoted by a double underscore prefix (e.g., __variable). Private variables cannot be accessed directly from outside the class, and they are used to encapsulate data and prevent unintended interference from external code.

class Car:

    def __init__(self, make, model):
        self.__make = make  # private variable
        self.__model = model  # private variable

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

# getter and setter methods: Getter and setter methods are used to access and modify private variables in a class. A getter method is a method that retrieves the value of a private variable, while a setter method is a method that sets the value of a private variable. Getter and setter methods provide controlled access to private variables, allowing for validation or additional logic to be implemented when getting or setting the value.

# Need for encapsulation: Encapsulation is important in object-oriented programming because it helps to protect the internal state of an object from unintended interference and misuse. By restricting access to the components of an object, encapsulation allows for better modularity, maintainability, and security of code. It also promotes the principle of information hiding, which helps to reduce complexity and improve the overall design of a software system. Encapsulation allows developers to create classes that can be easily reused and modified without affecting other parts of the codebase, making it easier to manage and maintain large software projects.

# Private attributes and methods in Python are not truly private, but they are name-mangled to make it more difficult to access them from outside the class. This is done by prefixing the attribute or method name with a double underscore (e.g., __attribute). The name mangling process changes the name of the attribute or method to include the class name, making it less likely to be accessed accidentally from outside the class. However, it is still possible to access private attributes and methods using their mangled names, so it is important to use this feature with caution and follow best practices for encapsulation.


# class diagram
# +------------------+
# |      Class       |
# +------------------+
# | - private_attr   |
# | + public_attr    |
# +------------------+
# | + public_method()|
# | - private_method()|
# +------------------+      