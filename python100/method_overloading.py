# class Geometry:

#     def area(self, radius):
#         return 3.14 * radius * radius
    
#     def area(self, length, breadth):
#         return length * breadth
    

# obj = Geometry()
# print(obj.area(5)) # This will give error because of method overloading. It will consider last defined method and it will expect 2 arguments but we are passing only 1 argument.

# Solution: We can use default arguments to achieve method overloading in python.

class Geometry:

    def area(self, radius, breadth = 0):
       if breadth == 0:
           print("Area of circle is:", 3.14 * radius * radius)
       else:
           print("Area of rectangle is:", radius * breadth)

obj = Geometry()
obj.area(5) # This will call area method with 1 argument and it will calculate area of circle.
obj.area(5, 10) # This will call area method with 2 arguments and it will calculate area of rectangle.