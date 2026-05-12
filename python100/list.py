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
    