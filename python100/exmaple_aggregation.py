class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

    
class Address:

    def __init__(self, city, pincode, state):

        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state


add = Address("Indore", 452001, "Madhya Pradesh")
customer = Customer("Sanju", "Male", add)

customer.edit_profile("Sardar", "Jhanshi", 559900, "Uttar Pradesh")

print(customer.address.city)
print(customer.address.state)
print(customer.address.pincode)
        