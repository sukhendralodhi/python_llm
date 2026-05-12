# FUNCTION = > A block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# ABSTRACTION = > Abstraction is the process of hiding the implementation details and showing only the functionality to the user. In python, we can achieve abstraction by using functions.

# DECOMPOSITION = > Decomposition is the process of breaking down a complex problem into smaller, more manageable parts. In python, we can achieve decomposition by using functions.

# SYNTAX OF FUNCTION
# def function_name(parameters):
#     # code to be executed


def is_even(num):
    """This function takes a number as input and returns True if the number is even, otherwise it returns False."""
    if type(num) == int:
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        return "Please enter a valid integer"
# print(is_even(4)) # this will print True

# for i in range(1, 11):
#     if is_even(i):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# print(is_even.__doc__) # this will print the docstring of the function is_even

# print(is_even("hello")) # this will print "Please enter a valid integer" because the input is not an integer

# ===================================================

# PARAMETER VS ARGUMENT
# PARAMETER = a variable in the declaration of a function. It is a placeholder for the value that will be passed to the function when it is called.

# ARGUMENT = a value that is passed to a function when it is called. It is the actual value that is passed to the function.

# DEFAULT ARGUMENTS = > Default arguments are the arguments that are given a default value in the function definition. If the caller does not provide a value for that argument, the default value will be used.

# def power(a,b):
#     """This function takes two numbers as input and returns the first number raised to the power of the second number."""
#     return a**b

# print(power(2,3)) # this will print 8 because 2 raised to the power of 3 is 8

# print(power(2)) # this will raise a TypeError because the second argument is missing

# HOW WE CAN AVOID THIS ERROR

def power(a,b=2):
    """This function takes two numbers as input and returns the first number raised to the power of the second number. If the second number is not provided, it will default to 2."""
    return a**b

# print(power(2)) # this will print 4 because 2 raised to the power of 2 is 4

# POSITIONAL ARGUMENTS = > Positional arguments are the arguments that are passed to a function in the correct positional order. The first argument is assigned to the first parameter, the second argument is assigned to the second parameter, and so on.   


# KEYWORD ARGUMENTS = > Keyword arguments are the arguments that are passed to a function by explicitly specifying the parameter name. This allows us to pass the arguments in any order, as long as we specify the parameter name.

# ARBITARY ARGUMENTS = > Arbitrary arguments are the arguments that are passed to a function without explicitly specifying the parameter name. This allows us to pass a variable number of arguments to a function. In python, we can use *args and **kwargs to achieve this.

# EX AMPLE OF ARBITARY ARGUMENTS
def sum(*args):
    """This function takes a variable number of arguments and returns the sum of all the arguments."""
    total = 0
    # // WHAT IS *args => *args is a special syntax in python that allows us to pass a variable number of arguments to a function. It is used to pass a variable number of non-keyword arguments to a function. The *args syntax allows us to pass any number of arguments to the function, and they will be treated as a tuple inside the function.    
    for num in args:
        total += num
    return total


# GLOBAL VARIABLE = > A global variable is a variable that is defined outside of a function and can be accessed from anywhere in the code. It is not limited to the scope of a function and can be used by any function in the code.

# SHOULD I CHANGE THE VALUE OF A GLOBAL VARIABLE INSIDE A FUNCTION?
# It is generally not recommended to change the value of a global variable inside a function because it can lead to unexpected behavior and make the code harder to debug. If you need to change the value of a global variable inside a function, it is better to use the global keyword to explicitly indicate that you are modifying a global variable. However, it is still best practice to avoid modifying global variables inside functions whenever possible.

# example
x = 10 # this is a global variable
def change_x():
    global x # this will indicate that we are modifying the global variable x
    x = 20 # this will change the value of the global variable x to 20      


# LOCAL VARIABLE = > A local variable is a variable that is defined inside a function and can only be accessed from within that function. It is limited to the scope of the function and cannot be used outside of the function.

# example
def my_function():
    y = 5 # this is a local variable
    print(y) # this will print 5


# NESTED FUNCTION = > A nested function is a function that is defined inside another function. The inner function can access the variables and parameters of the outer function, but the outer function cannot access the variables and parameters of the inner function.

# example   
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# print(outer_function(5)(10)) # this will print 15 because the inner function is adding the value of x from the outer function and the value of y from the inner function.

# // here how we can passing y to inner function ?
# ans => we are calling the outer function with the argument 5, which returns the inner function. Then we are calling the inner function with the argument 10, which adds the value of x from the outer function (which is 5) and the value of y from the inner function (which is 10) and returns the result (which is 15).


# EVERYTHING IN PYTHON IS AN OBJECT = > In python, everything is an object, which means that every value, variable, function, class, module, etc. is an object. This is because python is a high-level programming language that abstracts away the underlying implementation details and provides a simple and consistent interface for working with data and code. As a result, all values and variables in python are treated as objects, which allows us to use a wide range of built-in functions and methods to manipulate them.

def f(num):
    """This function takes a number as input and returns the square of that number."""
    return num**2

# print(f(2))
# print(f(9))
# print(type(f)) # this will print <class 'function'> because f is a function object in python

x = f
# print(x(2)) # this will print 4 because x is referencing the same function object as f and we are calling that function with the argument 2

del f # this will delete the function object f from memory
# print(f(2))
# print(f(9))

print(x(2)) # this will still print 4 because x is still referencing the same function object that f was referencing before it was deleted from memory.
print(f(9)) # this will raise a NameError because f is no longer defined in the current scope after it was deleted from memory.


# SHOULD I STORE FUNCTION IN LIST OR DICTIONARY?
# Yes, you can store functions in a list or a dictionary in python. This is because functions in python are first-class objects, which means that they can be treated like any other object in python. You can assign a function to a variable, pass a function as an argument to another function, and even return a function from another function. This allows you to store functions in a list or a dictionary and call them later when needed.