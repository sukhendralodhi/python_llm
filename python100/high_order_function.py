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

filter_result = filter(lambda fruit : "e" in fruit, fruits)
print(list(filter_result))
