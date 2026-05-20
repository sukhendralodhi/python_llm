

# fibonacci sequence with rabbits

def fib(n):

    a = 0
    b = 1

    sum = 0

    for i in range(n):
        sum = a + b
        a = b
        b = sum

    return sum


# result = fib(12)
# print(result)

# using recursion

def fib_rec(n):

    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
    

result = fib_rec(12)
print(result)