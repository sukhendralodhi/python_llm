class Customer:


    def __init__(self, name, age):

        self.name = name
        self.age = age

    def intro(self):
        print("I am ", self.name, "and i am", self.age, "Years old")


c1 = Customer("Sanju", 24)
c2 = Customer("Mohan", 28)
c3 = Customer("Neha", 18)

list = [c1,c2,c3]

for i in list:
    i.intro()