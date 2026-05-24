class Parent:

    def __init__(self):

        self.num = 100



class Child(Parent):

    def __init__(self):

        super().__init__() # calling parent class constructor
        self.val = 200


    def show(self):

        print(self.num) # accessing parent class variable using child class object is possible because of super keyword
        # it will call parent class constructor and initialize parent class variable in child class object 
        print(self.val)


son = Child() 
son.show()