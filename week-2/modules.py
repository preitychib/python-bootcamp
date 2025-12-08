# ===== Modules =====

from datetime import datetime as dt_datetime
import datetime

'''
1. Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
'''
print("1. Adding a week and 12 hours to the given date:")
str_date="March 22, 2020, at 10:00 AM"
random_date = dt_datetime.strptime(str_date, "%B %d, %Y, at %I:%M %p")
print("Original date time:", str_date)
new_date = random_date + datetime.timedelta(weeks=1, hours=12)
print("New date time:", new_date.strftime("%B %d, %Y, at %I:%M %p"))

'''
2. Code to get the dates of yesterday, today, and tomorrow.
'''
print("\n2. Getting dates for yesterday, today, and tomorrow:")
today_date=datetime.date.today()
yesterday_date = today_date - datetime.timedelta(days=1)
tomorrow_date = today_date + datetime.timedelta(days=1)
print("Yesterday:", yesterday_date.strftime("%d-%b-%Y"))
print("Today:", today_date.strftime("%d-%b-%Y"))
print("Tomorrow:", tomorrow_date.strftime("%d-%b-%Y"))

'''
3. Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
'''
import os

print("\n3. Print CWD and Create test folder and other os module operations")
try: 
    print("Current working directory:", os.getcwd())

    test_folder = "test"
    os.makedirs(test_folder, exist_ok=True)
    print(f"Created folder: {test_folder}")

    print("Files and folders in current directory:")
    for item in os.listdir('.'):
        print(f"  {item}")

    print("Current directory contents:")
    for item in os.listdir('.'):
        item_path = os.path.join('.', item)
        if os.path.isdir(item_path):
            print(f"[DIR] {item}")
        else:
            print(f"[FILE] {item}")

    os.rmdir(test_folder)
    print(f"Removed folder: {test_folder}")
except (OSError, PermissionError, Exception) as e:
    print(f"Error while handling directory: {e}")

'''
4. Write a Python program to rename a file from old_name.txt to new_name.txt.
'''
print("\n4. Renaming a file.")
try:
    with open("old_name.txt","w") as f:
        f.write("Data of a text file that is of no use")
    print("Created old_name.txt")
    os.rename("old_name.txt","new_name.txt")
    print("Rename file from old_name.txt to new_name.txt")
except (FileNotFoundError, PermissionError, Exception) as e:
    print(f"Error while handling file: {e}")
    
'''
5. Create a file and Write a Python program to get the size of a file named example.txt 
'''
print("\n5. Creating example.txt and getting its size")
with open("example.txt","w") as f:
    f.write("Example of data that is in the example file")
file_size = os.path.getsize("example.txt")
print(f"Size of example.txt: {file_size} bytes")

'''
6. Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
O/P: 2020-02-25 16:20:00
'''
print("\n6. Converting string to datetime object")
date_string = "Feb 25 2020 4:20PM"
datetime_object= dt_datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print("Original date:", datetime_object)
print("Converted date time object",datetime_object)

'''
7.Subtract 7 days from the date 2025-02-25 and print the result.
O/P: New date: 2025-02-18
'''
print("\n7. Subtract 7 days from 2025-02-25")
original_date = dt_datetime.strptime("2025-02-25", "%Y-%m-%d")
new_date = original_date - datetime.timedelta(days=7)
print("New date:", new_date.strftime("%Y-%m-%d"))

'''
8. Format the date 2020-02-25 as "Tuesday 25 February 2020"
'''
print("\n8. Formatting date 2020-02-25")
date_to_format = dt_datetime.strptime("2020-02-25", "%Y-%m-%d")
formatted_date = date_to_format.strftime("%A %d %B %Y")
print("Formatted date:", formatted_date)


'''
1. Adding a week and 12 hours to the given date:
Original date time: March 22, 2020, at 10:00 AM
New date time: March 29, 2020, at 10:00 PM

2. Getting dates for yesterday, today, and tomorrow:
Yesterday: 07-Dec-2025
Today: 08-Dec-2025
Tomorrow: 09-Dec-2025

3. Print CWD and Create test folder and other os module operations
Current working directory: /home/preeti-chib/PythonProjects/PythonBootcamp/week-2
Created folder: test
Files and folders in current directory:
  map_filter_reduce_lambda.py
  min_max.py
  test
  file_handling.py
  example.txt
  all_and_any.py
  decorator.py
  enumerate.py
  modules.py
  classs.py
  new_name.txt
  generator.py
  exception_handling.py
Current directory contents:
[FILE] map_filter_reduce_lambda.py
[FILE] min_max.py
[DIR] test
[FILE] file_handling.py
[FILE] example.txt
[FILE] all_and_any.py
[FILE] decorator.py
[FILE] enumerate.py
[FILE] modules.py
[FILE] classs.py
[FILE] new_name.txt
[FILE] generator.py
[FILE] exception_handling.py
Removed folder: test

4. Renaming a file.
Created old_name.txt
Rename file from old_name.txt to new_name.txt

5. Creating example.txt and getting its size
Size of example.txt: 43 bytes

6. Converting string to datetime object
Original date: 2020-02-25 16:20:00
Converted date time object 2020-02-25 16:20:00

7. Subtract 7 days from 2025-02-25
New date: 2025-02-18

8. Formatting date 2020-02-25
Formatted date: Tuesday 25 February 2020
'''