# Operator overloading allows you to define custom behavior for operators (like +, -, *, etc.) when they are used with instances of your classes. This can make your code more intuitive and easier to read. Here's an example of how to overload the addition operator (+) for a simple class called `Point`:

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
point1 = Point(2, 3)
point2 = Point(4, 5)


# Operator Overloading in Python
#   Operator Overloading means giving special meaning to operators (+, -, *, >, etc.) for user-defined objects.
#   Python allows this using magic methods / dunder methods.

# Example:
#   + adds numbers
#   + concatenates strings
#   This is polymorphism in Object-Oriented Programming.



# 🔹 Common Magic Methods

# | Operator | Magic Method    |
# | -------- | --------------- |
# | `+`      | `__add__()`     |
# | `-`      | `__sub__()`     |
# | `*`      | `__mul__()`     |
# | `/`      | `__truediv__()` |
# | `>`      | `__gt__()`      |
# | `<`      | `__lt__()`      |
# | `==`     | `__eq__()`      |


class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)