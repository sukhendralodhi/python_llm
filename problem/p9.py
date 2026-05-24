# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

def is_triangle(angle1, angle2, angle3):

    if angle1 + angle2 + angle3 == 180:
        return True
    else:
        return False

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if is_triangle(angle1, angle2, angle3):
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")