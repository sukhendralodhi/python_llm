# lambda functions => anonymous functions
# defination # lambda arguments: expression

# example 1

# square = lambda x : x ** 2
# print(square(9))

# sum = lambda a,b : a+b
# print(sum(10,20))

res = lambda x : x[0] == "a"

# print(res("apple"))
# print(res("banana"))

result = lambda x : "even" if x % 2 == 0 else "odd"

# print(result(10))
print(result(11))


# diffrence between lambda and normal function
# 1. lambda functions are anonymous, they do not have a name, while normal functions have a name.
# 2. lambda functions can only contain a single expression, while normal functions can contain multiple statements.
# 3. lambda functions are generally used for short, simple functions, while normal functions are used for more complex functions.
# 4. lambda functions are often used as arguments to higher-order functions, while normal functions can be used in a wider variety of contexts.
# 5. not reusable, lambda functions are not reusable, they can only be used once, while normal functions can be reused multiple times.
# 6. one liner, lambda functions are often used for one-liner functions, while normal functions can be used for multi-line functions.
# 7. lambda functions are often used in functional programming, while normal functions are used in procedural programming.

# ------------------------------------------------------------------------





