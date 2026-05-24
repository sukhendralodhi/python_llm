

# def sum_of_three_number(num1, num2, num3):

#     return num1 + num2 + num3


# num1 = int(input("Enter the value of number1: "))
# num2 = int(input("Enter the value of number2: "))
# num3 = int(input("Enter the value of number3: "))

# res = sum_of_three_number(num1, num2, num3)

# print(res)


def sum_three_digit(num):

    num1 = (num % 10)
    num = (num // 10)
    num2 = (num % 10)
    num3 = (num // 10)
    
    print("The sum of ", num, "is", num1+num2+num3)

number = int(input("Enter your three digit number: "))
sum_three_digit(number)
