# Donovan Blankley

# P2HW1

# adding module 4 concepts onto P1HW2 (fstring)

print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total = gas + accommodation + food
remaining_balance = budget - total

print("\n------------Travel Expenses------------")
print(f"{'Location:':20} {destination}")
print(f"{'Initial Budget:':20} ${budget:.2f}")
print(f"{'Fuel:':20} ${gas:.2f}")
print(f"{'Accommodation:':20} ${accommodation:.2f}")
print(f"{'Food:':20} ${food:.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':20} ${remaining_balance:.2f}")