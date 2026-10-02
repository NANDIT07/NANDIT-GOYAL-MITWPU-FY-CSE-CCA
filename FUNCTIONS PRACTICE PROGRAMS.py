# 1. Write a python program that accepts the three numbers from user and display its addition using functions.

x = int(input("Enter value of x:"))
y = int(input("Enter value of y:"))
z = int(input("Enter value of z:"))

def cal_sum(x, y, z):
    sum = x + y + z
    return sum

s = cal_sum(x, y, z)
print(s)


# 2. Write a Python program to receive three integers from keyboard
# and get their sum and product calculated through a user-defined function cal_sum_prod().

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

def cal_sum_prod(x, y, z):
    sum = x + y + z
    product = x * y * z
    return sum, product

s, p = cal_sum_prod(x, y, z)

print(s, p)


# 3. Write a python program to accept the number from the user and display prime factors of that number.

num = int(input("Enter your number: "))

print("Prime factors are:")

def prime_factors(num):
    factor = 2

    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num // factor
        else:
            factor = factor + 1

prime_factors(num)



# 4. Write a python program whcih will print all even numbers in a range 1 to 100.

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# 5. Write a python program which accepts 3 coefficients of the quadratic equation and generates real roots (with same or different values). 
#If (b raised to 2 - 4ac) < 0, use of math.sqrt function generates an exception as Value error "math domain error". 
#Show exception handling for ValueError, NameError and TypeError.

import math

def find_roots (a, b, c):
    try:
        d = b**2 - 4*a*c
        if d<0:
            #This will generate ValueError
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
        
        elif d==0:
            r1=r2= -b/(2*a)
            print("Roots are equal.")
            print("Root 1 =", r1)
            print("Root 2 =", r2)

        else:
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
            print("Roots are real and different.")
            print("Root 1 =", r1)
            print("Root 2 =", r2)

    except ValueError as e:
        print("Value Error:", e)
        print("Cannot calculate square root of a negative number.")

    except NameError as e:
        print("Name Error:", e)

    except TypeError as e:
        print ("Type Error:", e)
        print ("Coefficients must be numbers.")

    def main():
        try:
            a = float(input("Error coefficient a"))
            b = float(input("Error coefficient b"))
            c = float(input("Error coefficient c"))
            if a==0:
                print ("Not a quadratic equation.")
            else:
                find_roots (a,b,c)
        except ValueError as e:
            print ("Value Error", e)
            print ("Please enter numeric values")
        
        except TypeError as e:








# RECURSION

#1. print the numbers

def print_numbers(n):
    if n==0:     #Base Condition
        return
        print_numbers(n-1)  #Recursive Call
        print(n)
    n = int(input("Enter n:"))
    print_numbers (n)


# 2. Write a python program to show factorial of a number.

def factorial (n):
    if n==0 or n==1:
        return 1
    return n*factorial (n-1)

    n = int(input("Enter a number:"))
    print("Factorial =", factorial(n))


# 3. Write a python program to show the numbers in fibbonacci sequence.

def fibbonacci (n):
    if n<=1:
        return n
    return fibbonacci(n-1) + fibbonacci(n-2)
n = int(input("Enter number of terms:"))
for i in range (n):
    print (fibbonacci(i), end="")
