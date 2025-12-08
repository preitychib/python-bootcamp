# ===== File Handling =====

import os
'''
1 . Write a Python program to read the entire content of a file named sample.txt and display it.
'''

def read_file(file_name):
    try:
        with open(file_name,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)

print("1. Read the entire content of a file named sample.txt and display it.")
if not os.path.exists("sample.txt"):
    with open("sample.txt","w") as f:
        f.write("Hello, Python!")
read_file("sample.txt")

'''
2. Write a Python program to count the number of words in a file named words.txt
'''

print("\n2. Count the number of words in a file named words.txt: ",end=" ")
if not os.path.exists("words.txt"):
    with open("words.txt","w") as f:
        f.write("Hello, Python!")
with open("words.txt","r") as f:
    print(len(f.read().split()))

'''
3.Create a program to write the string “Hello, Python!” into a file named output.txt.
'''

print('\n3. Program to write the string "Hello, Python!" into a file named output.txt.')
if not os.path.exists("output.txt"):
    with open("output.txt","w") as f:
        f.write("Hello, Python!")

'''
4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]
'''
print('\n4. CSV file named students.csv with columns Name, Roll Number, and Marks.')
data=[
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]
if not os.path.exists("students.csv"):
    with open("students.csv","w") as f:
        f.write("\n".join([",".join(row) for row in data]))


'''
5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
'''
print('\n5.Print large file data using generator')
def read_file_generator(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

try:
    for line in read_file_generator("modules.py"):
        print(line)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)


'''
===== Output =====
1. Read the entire content of a file named sample.txt and display it.
Hello, Python!

2. Count the number of words in a file named words.txt:  2

3. Program to write the string "Hello, Python!" into a file named output.txt.

4. CSV file named students.csv with columns Name, Roll Number, and Marks.

5.Print large file data using generator
# ===== Modules =====

from datetime import datetime as dt_datetime
import datetime
.....
......
.......

'''