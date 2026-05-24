
num = int(input("Enter the four digit number: "))

# extract digitts

num1 = (num % 10)
num2 = (num // 10) % 10
num3 = (num // 100) % 10
num4 = num // 1000

print(num1)
print(num2)
print(num3)
print(num4)

reverse = (num1 * 1000) + (num2 * 100) + (num3 * 10) + num4
print("Reversed number =", reverse)

# Check whether reverse is same or not
if num == reverse:
    print("True - Number is Palindrome")

else: 
    print("False - Number is not Palindrome")