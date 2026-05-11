#P4LAb2
# Donovan Blankley
# This program asks user to enter an integer and displays a multiplication table. Will ask user if they would like to run the program again.

'''
Get inteer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again
if yes, run again
if no, program ends
'''

run_again = 'yes'
while run_again != "no" :
    user_num = int(input("Enter an integer: "))
    if user_num >= 0 :
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else: 
        print("This program does not handle negative values")
    run_again = input("Would you like to run the program again? ")
# Loop has been broken. User entered 'no'
print("Program has ended.")
