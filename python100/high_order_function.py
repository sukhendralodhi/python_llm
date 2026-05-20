# higher order function => a function that takes another function as an argument or returns a function as a result.

def return_sum(list):

    even_sum = 0
    odd_sum = 0
    div3_sum = 0

    for i in list:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        
        if i % 3 == 0:
            div3_sum += i   

    return (even_sum, odd_sum, div3_sum)

# result = return_sum([1,2,3,4,5,6,7,8,9])
# print(result)

# map function => a function that takes a function and an iterable as arguments and returns an iterable of the results.

# numbers = [1,2,3,4,5]

# map_result = map(lambda x : x ** 2, numbers)
# print(list(map_result))

# create list of students that have name, father name and address

students = [
    {"name": "John", "father_name": "Doe", "address": "123 Main St"},
    {"name": "Jane", "father_name": "Smith", "address": "456 Elm St"},
    {"name": "Bob", "father_name": "Johnson", "address": "789 Oak St"},
]

# res = map(lambda x : x["name"], students)
# print(list(res))


# ========================================================================================================

# filter function => a function that takes a function and an iterable as arguments and returns an iterable of the elements for which the function returns true.

numbers = [1,2,3,4,5,6,7,8,9]

# filter_result = filter(lambda x : x < 4, numbers)
# filter_result1 = filter(lambda x : x > 4, numbers)
# print(list(filter_result))
# print(list(filter_result1))

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]

# filter_result = filter(lambda fruit : "e" in fruit, fruits)
# print(list(filter_result))


# =====================================================================================================================

# Differences between map and filter functions:

# 1. map function applies a given function to each item of an iterable and returns a list of the results, while filter function applies a given function to each item of an iterable and returns a list of the items for which the function returns true.
# 2. map function can be used to transform the items of an iterable, while filter function can be used to select a subset of the items of an iterable.
# 3. map function can be used to perform operations on the items of an iterable, while filter function can be used to perform operations on the items of an iterable and return a subset of the items.
# 4. map function can be used to create a new list of the same length as the original list, while filter function can be used to create a new list that is shorter than the original list.



#======================================================================================================================

# REDUCE FUNCTION => a function that takes a function and an iterable as arguments and returns a single value that is the result of applying the function to the items of the iterable.


import functools
# numbers = [1,2,3,4,5]
# reduce_result = functools.reduce(lambda x,y : x+y, numbers)
# print(reduce_result)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

reduce_result = functools.reduce(lambda x,y : x if x > y else y, numbers)
print(reduce_result)