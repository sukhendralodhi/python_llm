# RECURSION 
# A function that calls itself is called a recursive function.
# A recursive function must have a base case to stop the recursion, otherwise it will run indefinitely

def multiply(a,b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)


# result = multiply(10,3)
# print(result)


# multiply using for loop 
def multiply(a,b):
    result = 0
    for i in range(b):
        result += a
    return result

# result = multiply(10,3)
# print(result)


# factorial using for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# result = factorial(5)
# print(result)

# factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# result = factorial(5)
# print(result)

# palindrome = "madam"

def is_palindrome(s):

    reverse = ""

    for i in s:
        reverse = i + reverse

    if s == reverse:
        return True
    else:
        return False
    

# print(is_palindrome("madam"))

# if is_palindrome("hello"):
#     print("The string is a palindrome")
# else:    
#     print("The string is not a palindrome")


# using recursion

def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])
    
# print(palindrome("madam"))




