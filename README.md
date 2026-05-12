# Python Revision Notes

This README collects the code from the `python100` folder in one place for easy revision.

## Files

- `python100/deep.py`
- `python100/dict.py`
- `python100/function.py`
- `python100/list.py`
- `python100/mutability.py`
- `python100/sets.py`
- `python100/tuples.py`

## `python100/deep.py`

```python
# Aliasing

# a=4
# b=a
# print(a) # this will print 4
# print(b) # this will also print 4

# id(a) # this will print the memory address of a
# id(b) # this will print the same memory address as a because b is referencing the same object as a

# REFRENCE COUNT

import sys

# a='hello'
# b=a
# c=b

# id(a) # this will print the memory address of a
# id(b) # this will print the same memory address as a because b is referencing the same object as a
# id(c) # this will print the same memory address as a and b because c is also referencing the same object as a and b

# print(id(a)) # this will print the memory address of a
# print(id(b)) # this will print the same memory address as a because b is referencing the same object as a
# print(id(c)) # this will print the same memory address as a and b because c is also referencing the same object as a and b

# print(a) # this will print 'hello'
# print(b) # this will also print 'hello'
# print(c) # this will also print 'hello'

# # how we can check how much variable ponting to the same object
# print(sys.getrefcount(a)) # this will print the reference count of a
# print(sys.getrefcount(b)) # this will print the reference count of b
# print(sys.getrefcount(c)) # this will print the reference count of c

# a='hdhakshkd'
# b=a
# c=b

# print(sys.getrefcount(a)) # this will print the reference count of a


# ===========================================================


# GARBAGE COLLECTION

# // in python garbage collection is done by reference counting and cyclic garbage collector

# DEFINATION OF GARBAGE COLLECTION
# garbage collection is the process of automatically freeing up memory by destroying objects that are no longer needed by the program. In python, garbage collection is done by reference counting and cyclic garbage collector.


# SOME WEIRD STUFF

a=61
b=a
c=b

# print(sys.getrefcount(a)) # this will print the reference count of a

a=5
b=5

# print(id(a)) # this will print the memory address of a
# print(id(b)) # this will print the same memory address as a because b is referencing the

# but if we create variable with value greater than 256 then it will not be stored in the memory and a new object will be created for each variable. So in this case, the reference count of a will be 1 because a is referencing a different object in memory than b and c.

a=257
b=257

# print(id(a)) # this will print the memory address of a
# print(id(b)) # this will print a different memory address than a because b is referencing a different object in memory than a

# if we create variable between -5 to 256 then it will be stored in the memory and will be reused whenever we create a variable with the same value. This is called interning. So in this case, the reference count of a will be 3 because a, b and c are all referencing the same object in memory.

# ====================================================================================

list1 = [1, 2, 3]

# print(id(list1[0])) # this will print the memory address of the first element of list1
# print(id(list1[1])) # this will print the memory address of the second element of list1
# print(id(list1[2])) # this will print the memory address of the third element of list1

# print(id(1)) # this will print the memory address of the integer 1
# print(id(2)) # this will print the memory address of the integer 2
# print(id(3)) # this will print the memory address of the integer 3

# print(id(list1)) // this will print the memory address of the list1 object in memory
```

## `python100/dict.py`

```python
# rules in dictionary
# 1. dictionary is a collection of key-value pairs
# 2. keys must be unique and immutable (string, number, tuple) but values can be of any data type and can be duplicate
# 3. dictionary is unordered collection of items
# 4. dictionary is mutable

# create empty dictionary
# d1 = {} # this will create an empty dictionary
# print(d1) # this will print {}

# 2d dict
# d2 = {"name": "John", "age": 30, "city": "New York"} # this will create a dictionary with 3 key-value pairs
# print(d2) # this will print {'name': 'John', 'age': 30, 'city': 'New York'}
```

## `python100/function.py`

```python
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
```

## `python100/list.py`

```python
# diff between list and array
# 1. array homogeneous, list heterogeneous
# 2. array fixed size, list dynamic size
# 3. array are much faster than list
# 4.lists are more programming friendly than arrays

# multidemensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2D list
list1 = [1,2,3,[4,5,6]]

# 3D list

list2 = [[[1,2,3],4,5],6,7]

# list creation type
list3 = list("Hello")
list4 = list()

# how to access element from list
# list1[index]

# edit list
# list[index] = value
# list[-index] = value // this will edit last value of index

# add new value in list
# there are ways to add new values in python list
# 1. append
# 2. extend
# 3. insert

# append = this will add one value in the last at end
# list.append(100)
# list.append([3,4]) // if you do this then it will add list not element bcz append add only one value for multiple value you can use extend


# extend = this will add mutilple value in the last at end

# list.extend([2,3,4,5,6]) // this will add all the value in list
# list.extend("hello") = this will convert first hello in list then add all the element seprate from hello so if you want to add only one item use append

# insert = insert give a option to add element in list your desired position
# list.insert(2, 100) // fisrt index , second value you want to add that provided index number



# DELETE // for deleting a element from list have 4 methods
# 1. del
# 2. remove
# 3. pop
# 4. clear

# del = that will delete element from list provided index number
# del list[index position]
# del list // this will delete entire list

# you can also remove elment by doing negative indexing
# del list[-5]

# REMOVE  // if you don't know what is the index position but you know that value exist then you can provide a value inside remove like this
# list.remove('hello') // this will remove that perticular value from list


# POP // delete element from last
# list.pop() // this will delete last element from the list

# CLEAR = this will clear (empty) your list not delete
# ex. list.clear() // this list will empty



# LIST OPERATIONS

# 1. concatination

l1 = [1,2,3,4]
l2 = [5,6,7]

# if you do
# l1+l2 = this will create new list bcz concatination always create a new list

# 2. multipication

# l1*3 = this will be // [1,2,3,4,1,2,3,4,1,2,3,4]

# YOU CAN APPLY LOOP ON LIST

list = [1,2,3,4,5,6,7,8,9]

# for i in list:
#     print(i)

h1 = [1,2,3,[4,5]]

# print(4 in h1) // this will return false bcz 4 not in h1 list
# print(4 in h1[3])

# lenth function
# len(h1) // it will give you length of list

# min // it will give you min number from list

# max // it will give you max number from list

# sorted // this will sort your list in ascending order
# sorted(h1) // this will give you error bcz h1 have list inside list

# sort // it will make changes in original list and sort it in ascending order

# index // this will give you index number of that value

name  = "hello how are you"

# print(name.title())

# print(name.split())

l = []

for i in name.split():
    # print(i.capitalize())
    l.append(i.capitalize())

# print(l)
# print(" ".join(l))

email = "sanju@gmail.com"

# print(email[:email.find("@")]) # this will give you abc


list4 = [1,3,4,2,3,1,2,3]
new_list = []

for i in list4:
    if i not in new_list:
        new_list.append(i)

print(new_list)
```

## `python100/mutability.py`

```python
# MUTABILITY = ability is the ability of an object to change its state or contents after it has been created. In Python, there are two types of objects based on mutability: mutable and immutable.

# IMMUTABLE OBJECTS = objects that cannot be changed after they have been created. Examples of immutable objects in Python include integers, floats, strings, tuples, and frozensets. When you try to modify an immutable object, a new object is created in memory with the new value.

# MUTABLE OBJECTS = objects that can be changed after they have been created. Examples of mutable objects in Python include lists, dictionaries, sets, and bytearrays. When you modify a mutable object, the same object in memory is updated with the new value.

a="hello"

# print(id(a)) # this will print the memory address of a

a=a+" world"

# print(id(a)) # this will print a different memory address than the previous one because a is referencing a new object in memory after the concatenation operation.

# for tuple
t=(1,2,3)
# print(id(t)) # this will print the memory address of t
t=t+(4,5)
# print(id(t)) # this will print a different memory address than the previous one because t is referencing a new object in memory after the concatenation operation.


# list
l=[1,2,3]
# print(id(l)) # this will print the memory address of l
l.append(4)
# print(id(l)) # this will print the same memory address as the previous one because l is referencing the same object in memory after the append operation.

# SIDE EFFECTS OF MUTABILITY
# when we assign a mutable object to a new variable, both variables will reference the same object in memory. So if we modify the object using one variable, the changes will be reflected in the other variable as well because they are both referencing the same object in memory.

# HOW WE CAN AVOID SIDE EFFECTS OF MUTABILITY
# we can avoid side effects of mutability by creating a copy of the mutable object instead of referencing the same object in memory. This way, when we modify the copy, the original object will not be affected.

L1 = [1, 2, 3]
L2 = L1.copy() # this will create a reference to the same object in memory as L1
# L3 = L1.copy() # this will create a new object in memory with the same contents as L1

# print(id(L1)) # this will print the memory address of L1
# print(id(L2)) # this will print the same memory address as L1 because L2


list1 = [1, 2, 3]
list2 = list1[:] # this will create a new object in memory with the same contents as list1

# print(id(list1)) # this will print the memory address of list1
# print(id(list2)) # this will print a different memory address than list1 because list2 is a separate object in memory
```

## `python100/sets.py`

```python
# SETS IN PYTHON

# 1. set do not allow duplicate values
# 2. set do not have indexing and slicing
# 3. set do not contain mutable data type like list and dictionary but it can contain immutable data type like tuple and string

# SO 2D AND 3D SETS ARE NOT POSSIBLE IN PYTHON BECZ SET DO NOT SUPPORT NESTED SETS BUT YOU CAN CREATE A SET WITH TUPLE INSIDE IT

# EMPTY_SET
SET = {} # this will create an empty dictionary not set so to create an empty set you have to use set() function
print(SET) # this will print {} which is an empty dictionary

# HOMOGENEOUS SET
SET1 = {1,2,3,4,5} # this will create a set with 5 elements which are all integers
print(SET1) # this will print {1, 2, 3, 4, 5}

# HETEROGENEOUS SET
SET2 = {1, "Hello", (1,2,3), 3.14} # this will create a set with 4 elements which are of different data types
print(SET2) # this will print {1, 'Hello', (1, 2, 3), 3.14}

# SET DO NOT FOLLOW INDEXING
# SET FOLLOW HASING ALGORITHM TO STORE THE ELEMENTS IN SET SO IT DO NOT FOLLOW INDEXING AND SLICING BUT YOU CAN ACCESS THE ELEMENTS OF SET BY USING FOR LOOP OR BY USING IN KEYWORD

# HOW TO ACCESS ELEMENTS FROM SET
# 1. FOR LOOP
for i in SET1:
    print(i) # this will print each element of set in new line

# 2. IN KEYWORD
print(3 in SET1) # this will print True bcz 3 is present in SET1
print(6 in SET1) # this will print False bcz 6 is

# can be add element in set by using add() method
SET1.add(6) # this will add 6 in SET1
print(SET1) # this will print {1, 2, 3, 4, 5, 6}

print(id(SET1)) # this will print the memory address of SET1

# DELETE ELEMENT FROM SET
# 1. remove() // this will remove the specified element from set if the element is not present in set then it will raise an error
SET1.remove(6) # this will remove 6 from SET1
print(SET1) # this will print {1, 2, 3, 4, 5}

# SET functions
# 1. union() // this will return a new set which is the union of two sets
SET3 = {1,2,3}
SET4 = {3,4,5}
print(SET3.union(SET4)) # this will print {1, 2, 3, 4, 5}

# intersection() // this will return a new set which is the intersection of two sets
# print(SET3.intersection(SET4)) # this will print {3} bcz 3 is the only common element in both sets


# difference() // this will return a new set which is the difference of two sets
print(SET3.difference(SET4)) # this will print {1, 2} bcz 1 and 2 are present in SET3 but not in SET4
print(SET4.difference(SET3)) # this will print {4, 5} bcz 4 and 5 are present in SET4 but not in SET3

# symmetric_difference() // this will return a new set which is the symmetric difference of two sets
print(SET3.symmetric_difference(SET4)) # this will print {1, 2, 4, 5} bcz 1 and 2 are present in SET3 but not in SET4 and 4 and 5 are present in SET4 but not in SET3

# isdisjoint() // this will return True if two sets have no common element otherwise it will return False
print(SET3.isdisjoint(SET4)) # this will print False bcz 3 is the common element in both sets

# issubset() // this will return True if one set is a subset of another set otherwise it will return False
print(SET3.issubset(SET4)) # this will print False bcz SET3 is not a subset of SET4
print(SET4.issubset(SET3)) # this will print False bcz

# issuperset() // this will return True if one set is a superset of another set otherwise it will return False
print(SET3.issuperset(SET4)) # this will print False bcz SET3 is not a superset of SET4
print(SET4.issuperset(SET3)) # this will print False bcz

# clear() // this will remove all the elements from set
SET3.clear() # this will remove all the elements from SET3
```

## `python100/tuples.py`

```python
# create
# access
# edit
# add delete
# oprations
# functions


# 1. how to create and empty tuple
# t1 = ()

# homogeneous tuple
# t2 = (1,2,3,4)

# heterogeneous tuple
# t3 = (1,2,3,"hello", 4.5)

# 2D tuple
# t4 = ((1,2,3), (4,5,6), (7,8,9))

# if you hae single element in tuple then it will not be considered as tuple it will be a string or integer value
# ex t5 = (1) // this will be considered as integer value not tuple

# if you want to create a single element tuple then you have to add comma after that element
# t6 = (1,)

# print(t6)

# if you pass string in tuple then it will consider each character as a element of tuple
# t7 = ("hello") // this will be considered as string not tuple
# t8 = ("hello",) // this will be considered as tuple with single element
# print(t8)

# t4 = ([1,2,3,4]) // this will be considered as tuple with single element which is list but if you want to create a tuple with single element which is list then you have to add comma after that list
# print(t4)

# t5 = (1,2,3,4) // this will be considered as tuple with 4 element but if you want to change any element of tuple then you can do that by converting tuple into list and then again convert it into tuple
# print(t5)



# ACCESSING ELEMENT FROM TUPLE

# t5 = (1,2,3,4)
# print(t5[0]) // this will print first element of tuple
# print(t5[1]) // this will print second element of tuple
# print(t5[2]) // this will print third element of tuple
# print(t5[3]) // this will print fourth element of tuple

# NEGATIVE INDEXING

# print(t5[-1]) // this will print last element of tuple
# print(t5[-2]) // this will print second last element of tuple
# print(t5[-3]) // this will print third last element of tuple

# SLICING
# print(t5[0:2]) // this will print first two element of tuple
# print(t5[1:3]) // this will print second and third element of tuple

# EDITING TUPLE
# // tuple are immutable so you can not change any element of tuple but you can change the entire tuple by reassigning it to a new value

# DELETING TUPLE
# // you can delete entire tuple by using del keyword but you can not delete any element of tuple

# T7 = (1,2,3,4)

# del T7 // this will delete entire tuple but if you try to access T7 after deleting it then it will give error bcz T7 is deleted

# WE CAN RUN LOOP ON TUPLE
# for i in t5:
#     print(i)

# FUNCTIONS IN TUPLE
# 1. count() // this will count the number of times a element is present in tuple
# t5 = (1,2,3,4,1,2,3,4)
# print(t5.count(1)) // this will print 2 bcz 1 is present 2 times in tuple

# 2. index() // this will return the index of first occurrence of a element in tuple
# print(t5.index(3)) // this will print 2 bcz 3 is

# sorted // this will return a sorted list of tuple
# print(sorted(t5)) // this will print [1,1,2,2,

# MIN
# print(min(t5)) // this will print 1 bcz 1 is the minimum element in tuple

# MAX
# print(max(t5)) // this will print 4 bcz 4 is the maximum element in tuple

# SUM
# print(sum(t5)) // this will print 20 bcz 1+2+3+4+1+2+3+4 = 20

# TUPLES ARE READ ONLY DATA STRUCTURE IN PYTHON WHICH MEANS YOU CAN NOT CHANGE ANY ELEMENT OF TUPLE BUT YOU CAN CHANGE THE ENTIRE TUPLE BY REASSIGNING IT TO A NEW VALUE
```
