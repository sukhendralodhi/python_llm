
# 🔹 Aggregation in Python OOP
# Aggregation is a relationship where one class contains another class object.

# It represents a "has-a" relationship.

# Example:
# A Department has Teacher
# A Car has Engine
# A School has Students

# The contained object can exist independently.


class Engine:
    def start(self):
        print("Engine start")


class Car:
    
    def __init__(self, engine):
        self.engine = engine # Aggregation 

    def drive(self):
        self.engine.start()
        print("Car is running")



# eng = Engine()     # Engine object created separately
# car = Car(eng)     # Pass engine object to Car
# car.drive()

# 🔹 Why This is Aggregation?
    # Because:
    # Engine can exist without Car
    # Car uses Engine
    # Objects are loosely connected


# 🔹 Real-World Example

class Student:

    def __init__(self, name):
        self.name = name


class College:

    def __init__(self, student):
        self.student = student


    def show(self):
        print("Student name", self.student.name)


s1 = Student("Sukhendra")
c1 = College(s1)

c1.show()
        






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


# add = Address("Indore", 452001, "Madhya Pradesh")
# customer = Customer("Sanju", "Male", add)

# customer.edit_profile("Sardar", "Jhanshi", 559900, "Uttar Pradesh")

# print(customer.address.city)
# print(customer.address.state)
# print(customer.address.pincode)
        