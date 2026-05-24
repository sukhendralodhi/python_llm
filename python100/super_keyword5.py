class Parent:
    def __init__(self):
        self.__num = 100


    def get_num(self):
        print("Parent num:", self.__num)


class Child(Parent):
    def __init__(self):
        super().__init__() # calling parent class constructor
        self.__val = 200

    def get_val(self):
        print("Child val:", self.__val)


dad = Parent()
dad.get_num()
son = Child()
son.get_val()