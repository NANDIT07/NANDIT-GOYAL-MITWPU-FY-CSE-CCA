
# BASIC PROGRAMS 

# 1.Write a program that prints "Hello, World!" to the console
print ("Hello, World!")


# 2.To find largest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3.Accept two numbers from the user and print their sum

num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))

sum = num_1 + num_2
print(sum)


# 4.Write a program to determine if a number is even or odd

num = float(input("Enter a number:"))

if num % 2==0:
    print ("The number is even")
else:
    print("The number is odd")


# 5.Build a calculator to perform addition , subtraction , division , multilplication

num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))

print("\nChoose your operation: 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division")
choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(num_1 + num_2)
elif choice == 2:
    print(num_1 - num_2)
elif choice == 3:
    print(num_1 * num_2)
elif choice == 4:
    print(num_1 / num_2)
else:
    print("Invalid choice", "\nRun the program again and choose a valid option.")


# 6.Write a python code to check given number is positive, negative or zero

n = float(input("Enter your number: "))

if n < 0:
    print("Your number is negative")
elif n > 0:
    print("Your number is positive")
else:
    print("Your number is zero")


# 7.Write a program to print sum of all the digits of given number

num = int(input("Enter any number: "))
sum_1 = 0

while num > 0:
    digit = num % 10
    sum_1 = sum_1 + digit
    num = num // 10

print("The sum of the digits is:", sum_1)


# 8.write a program to find the factorial of a given number

num = int(input("Enter any number: "))
fact = 1

for i in range(1, num + 1): 
    fact = fact * i

print ("The factorial of the number is:", fact)


# 9.write a python program to check if given number prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not a prime number")
else:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print("The number is not a prime number")
            break
    else:
        print("It is a prime number")


# 11.write a program to accept 5 numbers from the user and display their cube values

for i in range (5):
    num = int(input("Enter a number"))
    cube = num**3
    print("Cube:", cube)


# 12.Write a program to reverse a given number

num = int(input("Enter a number:"))
reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num//10
print("Reverse:", reverse)


# 13.To determine whether a given year is a leap year or not

year = int(input("Enter a year:"))

if year % 400 == 0:
    print("The year is a leap year.")
elif year % 100 == 0:
    print("The year is not a leap year.")
else:
    print("The year is not a leap year.")


# 15.Write a python program to print the following statements as an output using print statement.

#Student Name:
#Address:
#Contact Number:
#Mother Tongue:
#School Name:
#Year:
#Panel:
#Roll no:

student_name = str(input("Student Name:"))
address = str(input("Address:"))
contact_no = int(input("Contact Number:"))
mother_tongue = str(input("Mother Tongue:"))
school_name = str(input("School Name:"))
year = int(input("Year:"))
Panel = int(input("Panel:"))
roll_no = int(input("Roll no:"))



# 16.Accept Student  Name, Roll Number and Marks of the 3 subjects from the user. 
#Calculate the percentage of the marks and display it. Display the Subject with Highest and lowest marks

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

marks_list = []

for score in range(3):
    while True:
        marks = float(input(f"Enter marks for subject {score + 1}: "))

        if 0 <= marks <= 100:
            marks_list.append(marks)
            break
        else:
            print("Invalid marks! Please enter a mark between 0 and 100.")

aggregate_marks = sum(marks_list)
total_subjects = 3
max_marks_per_subject = 100
calculate_percentage = (aggregate_marks / 300) * 100

# Finding highest and lowest marks
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

# Finding which subject has the highest and lowest marks
highest_subject = marks_list.index(highest_marks) + 1
lowest_subject = marks_list.index(lowest_marks) + 1

print("\nStudent Name:", student_name)
print("Roll Number:", roll_number)

print("\nTotal Marks:", marks_list)
print("Aggregate:", aggregate_marks)
print("Percentage:", calculate_percentage)

print("\nHighest Marks:", highest_marks, "Subject:", highest_subject)
print("Lowest Marks:", lowest_marks, "Subject:", lowest_subject)
