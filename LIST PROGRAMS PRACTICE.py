# LIST PROGRAMS PRACTICE

# 1) Write a program to create a list of 5 integers and display the list items. Access individual elements through index. 

numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

print("\nFirst number:", numbers[0])
print("Second number:", numbers[1])
print("Third number:", numbers[2])
print("Fourth number:", numbers[3])
print("Fifth number:", numbers[4])


# 2 ) Write a program to append a new item to the end of the list.

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print("\nAfter Adding:", numbers)



# 3) Write a program to reverse the order of the items in the list.

numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("\nAfter Reversing:", numbers)


# 4) Write a program to print the number of occurrences of a specified element in a list.

numbers = [10, 20, 30, 40, 50, 20, 20]

element = int(input("Search for your number: "))

count = numbers.count(element)

if count > 0:
    print("Yes, your number is there")
    print("It appears", count, "time(s)")
else:
    print("No, your number is not there")


# 5) Write a program to append the items of list1 to list2 in the front.

list1 = [10, 20, 30]
list2 = [40, 50, 60]

list2 = list1 + list2

print("After appending list1 to the front of list2:", list2)


# 6) Write a program to insert a new item before the second element in an existing list. 

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

numbers.insert(1,15)
print("After Inserting:", numbers)



# 7) Write a program to remove the item from a specified index in a list. 

numbers = [10, 20, 30, 40, 50]
index = int(input("\nEnter the index to remove:"))
numbers.pop(index)
print("List after removal:", numbers)


# 8) Write a program to remove the first occurrence of a specified element from a list.

numbers = [10, 20, 30, 40, 50]
element = int(input("Enter the element to remove:"))
numbers.remove(element)
print("List after removal:", numbers)



# 9) Write ap rogram to accept 20 values from user and save it in list. Perform following operations on it:
numbers = []
for i in range (20):
    num = int(input("Enter a number:"))
    numbers.append(num)
    print("\nList:", numbers)
# a) count similar elements of list and print their index value
    print("\nSimilar elements and their Index values:")
for i in range (20):
    if numbers.count(numbers[i]) > 1:
        print(numbers [i], "->", end = " ")
for j in range (20):
    if numbers [j] == numbers [i]:
        print(j, end = " ")
print()

# b) count even and odd values of list
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2==0:
        even_count += 1
    else:
        odd_count += 1
print("\nEven numbers count:", even_count)
print("Odd numbers count:", odd_count)

# c) count positive and negative values of list

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("\nPositive numbers count:", positive_count)
print("Negative numbers count:", negative_count)
print("Zero count:", zero_count)






# 10) Write a program to accept 10 values from user and save it in list. Perform following operations on it  

numbers = []

for i in range (5):
    num = int(input("Enter the value:"))
    numbers.append (num)
print("\nOriginal List:", numbers)

# a) Sort list in ascending order using sorted() function and display sorted list
ascending = sorted(numbers)
print("Ascending Order:", ascending)

# b) sort list in descending order using sort() function
numbers.sort(reverse=True)
print("Descending Order:", numbers)

# c) display length of list
length = len(numbers)
print("Length of List:", length)




# 11) Write a program to accept two lists from user and merge them using "+" in a single list.

list1 = []
list2 = []

print("Enter 5 elements for List 1:")

for i in range(5):
    num = int(input("Enter value: "))
    list1.append(num)

print("\nEnter 5 elements for List 2:")

for i in range(5):
    num = int(input("Enter value: "))
    list2.append(num)

merged_list = list1 + list2

print("\nList 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)




# 12) An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them.
#     For example, RAM is an acronym for “random access memory.” Write a program that allows the user to type in a 
#     phrase and then outputs the acronym for that phrase. 
#     Note: the acronym should be all uppercase, even if the words in the phrase are not capitalized.

phrase = input ("Enter a phrase:")
words = phrase.split()
acronym = ""

for word in words:
    acronym = acronym + word[0]
print("Acronym:", acronym)





# 13 Write a program to print the abbreviation of a month, given its number.

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_num = int(input("Enter a month number (1-12) :"))

if month_num>=1 and month_num<=12:
    print("Month Abbreviation:", months[month_num - 1])
else:
    print("Invalid Number")




# 14.Write a Python program to insert, delete, and display elements of a list.

fruit = ["orange", "banana", "cherry", "watermelon"]

print("Original List:", fruit)

# Insert an element
fruit.insert(1, "apple")
print("After inserting apple:", fruit)

# Delete an element using remove()
fruit.remove("banana")
print("After deleting banana:", fruit)

# Delete an element using index
del fruit[2]
print("After deleting item at index 2:", fruit)

# Display final list
print("Final List:", fruit)



# 15) Python program to merge two lists into a dictionary (one list as keys, another as values.

key= [101, 102, 103, 104] 
values = ["Amit", "Rahul", "Priya", "Sneha"] 
student_dict = dict(zip(key, values)) 
print("Dictionary:", student_dict)



# 16) Write a Python program to remove duplicate elements from a list.

a=[1,2,3,3,4,5,5,6]
u= list(set(a))
print(u)



# 17) Write a python program to convert two lists into a dictionary using zip().


key= [101, 102, 103, 104] 
values = ["Amit", "Rahul", "Priya", "Sneha"] 
student_dict = dict(zip(key, values)) 
print("Dictionary:", student_dict)





# 18) Write a python program to find common elements in two lists.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for element in list1:
    if element in list2:
        common.append(element)
print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common)