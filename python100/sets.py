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