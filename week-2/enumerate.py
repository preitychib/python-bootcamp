# ========= Enumerate =========

'''
Using below list and enumerate(), print index followed by value. 

Input: fruits = ["apple", "banana", "cherry"]
Output: 
0 apple
1 banana
2 cherry

'''
fruits = ["apple", "banana", "cherry"]
print("1. Using enumerate(), print index followed by value.")
print("Input: ",fruits)
print("Output: ")
for serial_number,fruit in enumerate(fruits):
    print(serial_number," ",fruit)

'''
Using below dict and enumerate, print key followed by value

Input: person = {"name": "Alice", "age": 30, "city": "New York"}

Output:
name: Alice
age: 30
city: New York

'''
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\n2. Using enumerate, print key followed by value")
print("Input: ",person)
print("Output: ")
for key,value in person.items():
    print(key,": ",value)

''' 
Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], 
use enumerate() to create a list of tuples where each tuple contains the index 
and the corresponding fruit, but only for even indices.
Output: [(2, 'banana'), (4, 'date')]
'''
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("\n3. For give list, print only even indexed fruit.")
print("Input: ",fruits)
print("Output: ")
list_of_fruits=[]
for fruit_number,fruit in enumerate(fruits, start=1):
    if fruit_number%2==0:
        list_of_fruits.append((fruit_number,fruit))
print(list_of_fruits)

# using list comprehension
# result = [(i, fruit) for i, fruit in enumerate(fruits, start=1) if i % 2 == 0]
# print(result)

'''
1. Using enumerate(), print index followed by value.
Input:  ['apple', 'banana', 'cherry']
Output: 
0   apple
1   banana
2   cherry

2. Using enumerate, print key followed by value
Input:  {'name': 'Alice', 'age': 30, 'city': 'New York'}
Output: 
name :  Alice
age :  30
city :  New York

3. For give list, print only even indexed fruit.
Input:  ['apple', 'banana', 'cherry', 'date', 'elderberry']
Output: 
[(2, 'banana'), (4, 'date')]
''' 