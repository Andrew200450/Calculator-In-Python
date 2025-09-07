# My First Project
# Calculator
# 09/07/2025

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def  multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Mathematical Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number:"))
    except ValueError:
        print("Invalid Input. Try using numbers only and it will work!")
        exit()
        

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "X", num2, "=", multiply(num1, num2))

elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero is note possible! Try again with another number.")
    else:
        print(num1, "÷", num2, "=", divide(num1, num2))

next_calculation = input("Do you want to perform another calculation? (yes/no): ")
if next_calculation == "yes":
    import os
    os.system('python Calcolatrice.py')


if next_calculation == "no":
    print("Alright, see ya!")
    exit()

else:
    print("Invalid Input")