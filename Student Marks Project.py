marks_list = []

for score in range(5):
    while True:
        marks = float(input(f"Enter marks for subject {score + 1}: "))

        if 0 <= marks <= 100:
            marks_list.append(marks)
            break
        else:
            print("Invalid marks! Please enter a mark between 0 and 100.")

aggregate_marks = sum(marks_list)
total_subjects = 5
max_marks_per_subject = 100
calculate_percentage = (aggregate_marks / 500) * 100

# Finding highest and lowest marks
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

# Finding which subject has the highest and lowest marks
highest_subject = marks_list.index(highest_marks) + 1
lowest_subject = marks_list.index(lowest_marks) + 1

print("\nTotal Marks:", marks_list)
print("\nAggregate:", aggregate_marks)
print("\nPercentage:", calculate_percentage)

print("\nHighest Marks:", highest_marks, "Subject:", highest_subject)
print("Lowest Marks:", lowest_marks, "Subject:", lowest_subject)

if calculate_percentage >= 90:
    print("\nYou have secured Grade A. Result: PASS")
elif calculate_percentage >= 75:
    print("\nYou have secured Grade B. Result: PASS")
elif calculate_percentage >= 60:
    print("\nYou have secured Grade C. Result: PASS")
elif calculate_percentage >= 40:
    print("\nYou have secured Grade D. Result: PASS")
else:
    print("\nResult: You have Failed")
