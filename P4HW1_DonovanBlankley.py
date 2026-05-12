# P4HW1
# Donovan Blankley
# Assignment assess student ability to edit and enhance exiting programs

num_scores = int(input("How many scores will you enter?"))

score_list = []

for score in range(num_scores):
    user_score = float(input(f"Enter score #{score + 1}:"))

    while user_score < 0 or user_score > 100:
        print("\nINVALID SCORE ENTERED!!!!!")
        print("Score should be between 0 and 100")

        user_score = float(input(f"Enter score #{score + 1} again: "))
    score_list.append(user_score)
lowest_score = min(score_list)
score_list.remove(lowest_score)

average = sum(score_list) / len(score_list)

if average >=90:
    letter_grade = "A"
elif average >=80:
    letter_grade = "B"
elif average >=70:
    letter_grade = "C"
elif average >=60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\n--------------Results--------------")
print(f"{'Lowest Score:':25}{lowest_score:.1f}")
print(f"{'Modified List:':25}{score_list}")
print(f"{'Scores Average:':25}{average:.2f}")
print(f"{'Grade:':25}{letter_grade}")
print("-------------------------------------")
