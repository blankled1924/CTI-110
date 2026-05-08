# Donovan Blankley

# P2HW2 

# This program asks users to enter their grades for Modules 1-6. The grades will be stored in a list. The lowest grade, highest grade, grade sum, and average grade will be displayed.

#Pseudocode
#Create an empty list
#Ask user to enter grades for Mudules 1-6
#Store grades into list
#Find the lowest grade min()
#Find the highest grade max()
#Find the sum of all grades usin sum()
#Find the average by dviding the sum by the number of grades
#Display resuts 

grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':20}{lowest:.1f}")
print(f"{'Highest Grade:':20}{highest:.1f}")
print(f"{'Sum of Grades:':20}{total:.1f}")
print(f"{'Average:':20}{average:.2f}")
print("-------------------------------")