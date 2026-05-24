class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    


class Child(Parent):

    def __init__(self, val, num):
        self.__val = val


    def get_val(self):
        return self.__val
    

son = Child(100, 10)
print("Parent num: ", son.get_num())
print("Child val: ", son.get_val())


# Note: Agar child ke pas apna koi constructor ni hai to parent ka constructor call ho jata hai but agar child ke pass apne constructor hai to parent ka constructor call ni hota hai 