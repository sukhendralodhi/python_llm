# What is an Iteration in Python?
# Iteration is the process of looping through a sequence (like a list, tuple, or string) and performing an action for each item in that sequence. In Python, we can use loops (like for and while) to iterate over sequences. Additionally, Python provides built-in functions and constructs that make iteration easier and more efficient, such as list comprehensions, generator expressions, and the itertools module.


# list = [1, 2, 3, 4, 5]

# for i in list:
#     print(i)


# Iterators in Python
# An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__(). An iterator allows you to traverse through all the elements of a collection, regardless of its specific implementation. In Python, many built-in data structures (like lists, tuples, and dictionaries) are iterable, meaning they can return an iterator that can be used to iterate through their elements.

list = [x for x in range(1, 10000)]

# for i in list:
#     print(i*2)

import sys

# print(sys.getsizeof(list)/64)

# 85176 bytes in mb = 85176 / (1024 * 1024)
# print(85176 / (1024 * 1024))

x = range(1, 10000)

# print(sys.getsizeof(x)/64)

# What is Iterable in Python?
# An iterable is any Python object capable of returning its members one at a time, allowing it to be iterated over in a for-loop or with other iteration tools. Examples of iterables include lists, tuples, strings, dictionaries, and sets. An iterable must implement the __iter__() method, which returns an iterator object that can be used to iterate through the elements of the collection.


# Point to remember:
# 1. Every Iterator is also and Iterable but every Iterable is not an Iterator.
# 2. An Iterable can be converted to an Iterator using the iter() function.


list1 = [1, 2, 3, 4, 5]

print(type(list1)) # <class 'list'>

# list1 is an Iterable but not an Iterator.

print(iter(list1)) # <list_iterator object at 0x7f8b8c8c8c8c>

print(type(iter(list1))) # <class 'list_iterator'> 