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