class Parent:

    def __init__(self, num):
        
        self.__num = num

    def get_num(self):
        return self.__num
    


class Child(Parent):

    def __init__(self,num,val):
        super().__init__(num) # calling parent class constructor
        self.__val = val


    def get_val(self):

        return self.__val
    

son = Child(100,200)

print(son.get_val())
print(son.get_num())

# Note: while calling super this should be a first statement of method (function)

