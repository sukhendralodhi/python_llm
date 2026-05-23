# first aproach to get time 

import time

start = time.time()

for i in range(1,101):
    print(i)

print(time.time() - start)


# o(n) - Linear time complexity 

def fact_iter(n):
    """assumes a an int >= 0"""
    answer = 1

    while n > 1:
        answer *= n
        n -= 1
    
    return answer

# 1. computer factorial
# 2. number of steps
# 3. worst case asymptotic complexity:
# ignore additve constants
# ignore multiplicative contants 

# n*n + 2n + 2 => remove constans
# n*n + n => remove small one
#n*n => o(n*n) - this is our time complexcity

# if input increase 2 then time 4 guna if 4 then 16 guna 


# TYPES OF ORDERS OF GROWTHS

# 1. constant
# 2. linear
# 3. quadratic
# 4 logaritmetic
# 5 n log n
# 6 exponential