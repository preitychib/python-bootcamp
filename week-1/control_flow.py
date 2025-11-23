# Control Flow

# For Loop:
# 1 Write a program that takes the input from the user and checks if a number is even or odd
print("Task 1: Check if a number is even or odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 2 Reverse a string using a for loop and check if it is a palindrome
print("\nTask 2: Reverse a string and check if it is a palindrome")
def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

test_strings = ["civic", "hello"]
for s in test_strings:
    if is_palindrome(s):
        print(f"'{s}' is a palindrome")
    else:
        print(f"'{s}' is not a palindrome")

# 3 Using input from the user to generate Fibonacci sequence
print("\nTask 3: Generate Fibonacci sequence")
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 4 Find two numbers from a list that add up to a target
print("\nTask 4: Find two numbers that add up to 9")
numbers = [1, 2, 3, 4, 5]
target = 9
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Numbers that add up to {target}: [{numbers[i]}, {numbers[j]}]")
            found = True
            break
    if found:
        break

# While Loop
# 5 Print even numbers between 1 and 20
print("\nTask 5: Print even numbers between 1 and 20")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print()

# Break Example
# 6 Find first occurrence of a number in a list and stop further searching
print("\nTask 6: Find first occurrence using break")
numbers = [10, 20, 30, 40, 50]
search_for = 30
for num in numbers:
    if num == search_for:
        print(f"Found {search_for} at position {numbers.index(search_for)}")
        break

# Continue Example
# 7 Using continue statement, print only odd numbers from 1 to 10
print("\nTask 7: Print odd numbers using continue")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

# Pass
# 8 What will be the output 
print("\nTask 8: What will be the output (pass statement)")
print("Output will be:")
for i in range(5):
    if i == 3:
        pass  
    print(i)

# 6. Match 
# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
print("\nTask 9: Check if a day is a weekday or weekend")
day = input("Enter a day of the week: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is a weekday")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is a weekend day")
    case _:
        print("Please enter a valid day of the week")

"""
======= OUTPUT =======
Task 1: Check if a number is even or odd
Enter a number: 34
34 is even

Task 2: Reverse a string and check if it is a palindrome
'civic' is a palindrome
'hello' is not a palindrome

Task 3: Generate Fibonacci sequence
Enter the number of terms: 5
Fibonacci sequence:
0 1 1 2 3 

Task 4: Find two numbers that add up to 9
Numbers that add up to 9: [4, 5]

Task 5: Print even numbers between 1 and 20
2 4 6 8 10 12 14 16 18 20 

Task 6: Find first occurrence using break
Found 30 at position 2

Task 7: Print odd numbers using continue
1 3 5 7 9 

Task 8: What will be the output (pass statement)
Output will be:
0
1
2
3
4

Task 9: Check if a day is a weekday or weekend
Enter a day of the week: sundaY
Sunday is a weekend day
"""