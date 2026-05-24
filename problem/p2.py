

def celcius_to_fahrenheit(celsius):

    if celsius is not None:

        return (celsius * 1.8) + 32
    
    else:
        return "Please enter value of celsius"
    

# celsius = int(input("enter the temprature in celsius: "))

# fah = celcius_to_fahrenheit(celsius)

# print(fah)

# If you want to handle empty input or invalid values, you can do this: 


def celsius_to_fahrenheit(celsius):

    return (celsius * 1.8) + 32


try:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")

except:
    print("Please enter valid input")