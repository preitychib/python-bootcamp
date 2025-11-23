# List Comprehensions

# 1. Given a list of numeric strings, convert them to integers. Using list comprehension
strings = ["1", "2", "3", "4", "5"]
nums= [int(num) for num in strings]
print("1. Convert strings to integers:")
print(f"Input: {strings}")
print(f"Output: {nums}\n")

# 2. Extract all integer from a list that are greater than 10. Using list comprehensions
numbers = [1, 5, 13, 4, 16, 7]
large_nums = [num for num in numbers if num > 10]
print("2. Numbers greater than 10:")
print(f"Input: {numbers}")
print(f"Output: {large_nums}\n")

# 3. Create a list of squares of numbers from 1 to 5, using list comprehensions
squares = [x**2 for x in range(1, 6)]
print("3. Squares of numbers 1-5:")
print(f"Output: {squares}\n")

# 4. Convert a list of squares for numbers from 1 to 5. Using List Comprehensions
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
row_elements = [num for row in matrix for num in row]
print("4. Flattened 2D list:")
print(f"Input: {matrix}")
print(f"Output: {row_elements}\n")

# 5. Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3],
#  create a dictionary using dictionary comprehension.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
disctionary = {k: v for k, v in zip(keys, values)}
print("5. Dictionary from two lists:")
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Output: {disctionary}\n")

# 6. Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, 
# create a new dictionary containing only the students who scored above 80
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
high_scores = {name: score for name, score in scores.items() if score > 80}
print("6. High scores (above 80):")
print(f"All scores: {scores}")
print(f"High scores: {high_scores}")

"""
======= OUTPUT =======

1. Convert strings to integers:
Input: ['1', '2', '3', '4', '5']
Output: [1, 2, 3, 4, 5]

2. Numbers greater than 10:
Input: [1, 5, 13, 4, 16, 7]
Output: [13, 16]

3. Squares of numbers 1-5:
Output: [1, 4, 9, 16, 25]

4. Flattened 2D list:
Input: [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
Output: [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

5. Dictionary from two lists:
Keys: ['a', 'b', 'c']
Values: [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}

6. High scores (above 80):
All scores: {'Alice': 85, 'Bob': 70, 'Charlie': 90}
High scores: {'Alice': 85, 'Charlie': 90}
"""