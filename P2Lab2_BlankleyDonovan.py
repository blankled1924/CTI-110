#Donovan Blankley
#4/12/2026
#P2LAB2
#this program will ask provide the user with MPG info stored in a dictionary.


mpg_cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 102.5,
    "Silverado": 15.8
}

keys = mpg_cars.keys()
print(keys)

vehicle = input("Enter a vehicle to see its MPG: ")

mpg = mpg_cars[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons = miles / mpg

print (f"You will need {gallons:.2f} gallons of fuel.")
