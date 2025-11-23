# Data Types


# Task 1: Convert the following values to the specified types and print the results
print("Task 1:")
value_1 = int(3.75)
print(f"3.75 as integer: {value_1}")

value_2 = float("123")
print(f"\"123\" as float: {value_2}")

value_3 = bool(0)
print(f"0 as boolean: {value_3}")

value_4 = str(False)
print(f"False as string: {value_4}")

# Task 2: Convert all characters in the string to uppercase. x = "hello"
print("\nTask 2:")
str_input = "hello"
uppercase_result = str_input.upper()
print(f"Uppercase of 'hello': {uppercase_result}")

# Task 3: Perform arithmetic operations and print the results
print("\nTask 3:")
x = 5
y = 3.14
z = x + y
print(f"z = {z}, type: {type(z).__name__}")
print(f"z as integer: {int(z)}")


# Task 4: Given the string s = 'hello', perform the following operations:
print("\nTask 4:")

# 4.1 Convert to uppercase
s = 'hello'
upper_s = s.upper()
print(f"Uppercase: {upper_s}")

# 4.2 Replace 'e' with 'a'
replaced_s = s.replace('e', 'a')
print(f"After replacement: {replaced_s}")

# 4.3 Check if starts with 'he'
starts_with_he = s.startswith('he')
print(f"Starts with 'he': {starts_with_he}")

# 4.4 Check if ends with 'lo'
ends_with_lo = s.endswith('lo')
print(f"Ends with 'lo': {ends_with_lo}")


"""
======= OUTPUT =======

Task 1:
3.75 as integer: 3
"123" as float: 123.0
0 as boolean: False
False as string: False

Task 2:
Uppercase of 'hello': HELLO

Task 3:
z = 8.14, type: float
z as integer: 8

Task 4:
Uppercase: HELLO
After replacement: hallo
Starts with 'he': True
Ends with 'lo': True
"""