# Input and Print


# Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting message using their name.
print("Task 1: Greet the user")
name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome to the program.")


# Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
print("\nTask 2: Basic Arithmetic Operations")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"\nSum: {a} + {b} = {a + b}")
print(f"Product: {a} * {b} = {a * b}")
if b != 0:
    print(f"Division: {a} / {b} = {a / b:.2f}")
else:
    print("Cannot divide by zero!")


# Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
print("\nTask 3: Process List of Names")
names = input("Enter names separated by commas: ")
names_list = [name.strip() for name in names.split(',')]
print(f"List of names: {names_list}")


# Task: Ask the user to enter their age and check if they are eligible to vote based on their age.
print("\nTask 4: Check Voting Eligibility")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print(f"You will be eligible to vote in {18 - age} years.")


# Task: For value = 3.14159, Using f-string print output for only up to 2 decimal places.
print("\nTask 5: Format Floating Point Number")
value = 3.14159
print(f"Formatted value: {value:.2f}")


"""
======= Output =======

Task 1: Greet the user
Please enter your name: Preeti Chib
Hello, Preeti Chib! Welcome to the program.

Task 2: Basic Arithmetic Operations
Enter first number: 13
Enter second number: 12

Sum: 13.0 + 12.0 = 25.0
Product: 13.0 * 12.0 = 156.0
Division: 13.0 / 12.0 = 1.08

Task 3: Process List of Names
Enter names separated by commas: Muskan,Sheetal,Rita,Sonu
List of names: ['Muskan', 'Sheetal', 'Rita', 'Sonu']

Task 4: Check Voting Eligibility
Enter your age: 19
You are eligible to vote!

Task 5: Format Floating Point Number
Formatted value: 3.14
"""
