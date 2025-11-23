# Built-in Data Structures Operations

# Task 1: Given a list of numbers, find and print the maximum and minimum values.
print("Task 1: Find max and min in a list")
nums = [1, 2, 3, 4, 5]
print(f"List: {nums}")
print(f"Max: {max(nums)}, Min: {min(nums)}")

# Task 2: Given two lists, merge them into a single list.
print("\nTask 2: Merge two lists")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged = a + b
print(f"List 1: {a}")
print(f"List 2: {b}")
print(f"Merged list: {merged}")

# Task 3: Given a list and a value, count how many times the value appears in the list.
print("\nTask 3: Count occurrences of 3")
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count = a.count(3)
print(f"List: {a}")
print(f"Number of 3's: {count}")

# Task 4: Given a list, sort it in ascending order.
print("\nTask 4: Sort a list")
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
sorted_list = sorted(a)
print(f"Original list: {a}")
print(f"Sorted list: {sorted_list}")

# Task 5: Given a set, add an element to it.
print("\nTask 5: Add to set")
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(f"Updated set: {numbers}")

# Task 6: Given a set, remove an element from it.
print("\nTask 6: Remove from set")
numbers = {1, 2, 3, 4, 5}
numbers.discard(3)  # or numbers.remove(3)
print(f"Updated set: {numbers}")

# Task 7: Given two sets, find their intersection.
print("\nTask 7: Set intersection")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Intersection: {intersection}")

# Task 8: Given a tuple, count how many times a specific element appears.
print("\nTask 8: Count in tuple")
fruits = ('apple', 'banana', 'apple', 'cherry')
count = fruits.count('apple')
print(f"Tuple: {fruits}")
print(f"Number of 'apple': {count}")

# Task 9: Given two tuples, concatenate them into a single tuple.
print("\nTask 9: Concatenate tuples")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Combined: {combined}")

# Task 10: Given a dictionary, access a specific value by key.
print("\nTask 10: Access dictionary value")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person: {person}")
print(f"Age: {person['age']}")

# Task 11: Given a dictionary, add a new key-value pair to it.
print("\nTask 11: Add to dictionary")
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print(f"Updated person: {person}")

# Task 12: Given a dictionary, remove a key-value pair.
print("\nTask 12: Remove from dictionary")
person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print(f"After removing 'city': {person}")

# Task 13: Given two dictionaries, merge them into a single dictionary.
print("\nTask 13: Merge dictionaries")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Merged: {merged}")

"""
======= OUTPUT =======
Task 1: Find max and min in a list
List: [1, 2, 3, 4, 5]
Max: 5, Min: 1

Task 2: Merge two lists
List 1: [1, 2, 3, 4]
List 2: [5, 6, 7, 8]
Merged list: [1, 2, 3, 4, 5, 6, 7, 8]

Task 3: Count occurrences of 3
List: [1, 3, 4, 5, 2, 1, 3, 9, 3]
Number of 3's: 3

Task 4: Sort a list
Original list: [1, 3, 4, 5, 2, 1, 3, 9, 3]
Sorted list: [1, 1, 2, 3, 3, 3, 4, 5, 9]

Task 5: Add to set
Updated set: {1, 2, 3, 4, 5, 6}

Task 6: Remove from set
Updated set: {1, 2, 4, 5}

Task 7: Set intersection
Set 1: {1, 2, 3}
Set 2: {3, 4, 5}
Intersection: {3}

Task 8: Count in tuple
Tuple: ('apple', 'banana', 'apple', 'cherry')
Number of 'apple': 2

Task 9: Concatenate tuples
Tuple 1: (1, 2, 3)
Tuple 2: (4, 5, 6)
Combined: (1, 2, 3, 4, 5, 6)

Task 10: Access dictionary value
Person: {'name': 'Alice', 'age': 30, 'city': 'New York'}
Age: 30

Task 11: Add to dictionary
Updated person: {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'M'}

Task 12: Remove from dictionary
After removing 'city': {'name': 'Alice', 'age': 30}

Task 13: Merge dictionaries
Dict 1: {'a': 1, 'b': 2}
Dict 2: {'c': 3, 'd': 4}
Merged: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""