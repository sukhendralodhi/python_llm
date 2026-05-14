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

# TUPLES ARE READ ONLY DATA STRUCTURE IN PYTHON WHICH MEANS YOU CAN NOT CHANGE ANY ELEMENT OF TUPLE BUT YOU CAN CHANGE THE ENTIRE TUPLE BY REASSIGNING IT TO A NEW VALUE