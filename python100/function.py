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

print(power(2)) # this will print 4 because 2 raised to the power of 2 is 4

# POSITIONAL ARGUMENTS = > Positional arguments are the arguments that are passed to a function in the correct positional order. The first argument is assigned to the first parameter, the second argument is assigned to the second parameter, and so on.   


# KEYWORD ARGUMENTS = > Keyword arguments are the arguments that are passed to a function by explicitly specifying the parameter name. This allows us to pass the arguments in any order, as long as we specify the parameter name.

