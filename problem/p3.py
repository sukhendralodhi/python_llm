def swap_number(num1, num2):

    temp = num1
    num1 = num2
    num2 = temp

    return num1, num2


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the secoond number: "))

# res = swap_number(num1, num2)
# 
# print(res)

# without using third variable 

def swap_number_without_using_third_var(num1, num2):

    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    return num1 , num2


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secoond number: "))

print(swap_number_without_using_third_var(num1, num2))

