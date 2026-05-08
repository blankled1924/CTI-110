 # Donovan

# P1HW2

# Assignment assess student ability to edit and enhance exiting programs

# Pseudo Code:
# 1. Display a message explaining the program purpose
# 2. Ask the user to enter their budget
# 3. Ask the user to enter their travel destination
# 4. Ask the user to enter expected gas expenses
# 5. Ask the user to enter expected accommodation expenses
# 6. Ask the user to enter expected food expenses
# 7. Add all expenses together
# 8. Subtract total expenses from the budget
# 9. Display the travel destination
# 10. Display the initial budget
# 11. Display each expense amount
# 12. Display the remaining balance

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))

accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

food = float(input("Last, how much do you need for food? "))

total = gas + accommodation + food

remaining_balance = budget - total

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)