

def find_big_age(a1, a2, a3):

    if a1 > a2 and a1 > a3:
        return a1
    
    elif a2 > a1 and a2 > a3:
        return a2
    
    else:
        return a3
    

age1 = int(input("Enter age of person 1:"))
age2 = int(input("Enter age of person 2:"))
age3 = int(input("Enter age of person 3:"))

big_age = find_big_age(age1, age2, age3)    
print(f"The biggest age is: {big_age}")