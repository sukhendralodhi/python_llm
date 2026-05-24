class Product:

    def review(self):
        print("This is a product review.")

class Phone(Product):

    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        print("This is a phone.")

    def buy(self):
        print(f"You have bought a {self.brand} phone for {self.price} dollars with a {self.camera} camera.")

    def return_phone(self):
        print(f"You have returned the {self.brand} phone.")


class Smartphone(Phone):
    pass

s = Smartphone(999, "Apple", "12MP")

s.review() # inherited from Product class
s.buy() # inherited from Phone class
s.return_phone() # inherited from Phone class