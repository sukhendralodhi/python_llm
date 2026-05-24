class Phone:

    def __init__(self, price, brand, camera):

        print("Printing from inside parent constructor")

        self.__price = price # private attribute
        self.brand = brand
        self.camera = camera

    

class Smartphone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera) # that will call parent constructor
        self.os = os
        self.ram = ram

        print("Inside smartphone constructor")
        


s = Smartphone(20000, "Samsung",48, "Android", 16)

print(s.os)
print(s.brand)