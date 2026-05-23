# Inheritance = Inheritance is a core concept of object oriented programming that allow one class (child/derived class) to reuse the properties and method of another class (parent/base class)

# What is inheritance?
# Inheritance let's you create a new class based on an existing class.
# The new class inherit attributes (variables) and behaviur (methods) from the parent class.

# Think of like it 

# Parent class => General Concept 
# Child class => More specific version 

# Basic Syntax In Python

class Parent:

    def display(self):
        print("This is a parent class")


class Child(Parent):

    def show(self):
        print("This is a child class")


# obj = Child()
# obj.display()
# obj.show()

# Note: Private member are not inherited 


class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


# child can access parent class methods and attributes 

# student1 = Student()
# student1.login()
# student1.register()
# student1.enroll()
# student1.review()


# But parent can not access child class methods and attributes 

# user = User()
# user.login()
# user.register()
# user.enroll()
# user.review()


# class Phone:

#     def __init__(self, price, brand, camera):
#         print("inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera


# class Smartphone(Phone):
#     pass


# s = Smartphone(80000, "Apple", 14)
# print(s.brand)
# print(s.price)
# print(s.camera)


# Note: Agar class B class A se inherit kr rha hai or class B ke andar koi constructor ni hai to jab ap class B ka object banoge to class A ka consturctor call ho jaega 

# if child class inheriting parent class and child class do not have constructor or be create a object for child class then parent class consturctor would be called 


# INHERITING PRIVATE MEMBER FROM PARENT CLASS

class Phone:

    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.__brand = brand # private attribute. (__variable name)
        self.camera = camera


class Smartphone(Phone):
    pass


s = Smartphone(80000, "Apple", 14)
print(s.__brand) # child class can not access parent class private methods and attributes 
print(s.price)
print(s.camera)