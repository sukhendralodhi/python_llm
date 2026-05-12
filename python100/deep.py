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