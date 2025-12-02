# ========= Lambda Map Filter Reduce =========

from functools import reduce

'''
Given a list let's see how to double each element of the given list. Using map() 
a = [1, 2, 3, 4]
Expected Output: [2, 4, 6, 8]
'''
a = [1, 2, 3, 4]
list_of_double=list(map(lambda x: x * 2, a))
print("1. Using map() to double each element of the given list.")
print("Given list: ",a)
print("List of double: ",list_of_double)

'''
Use filter() and lambda to extract all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected Output: [2, 4, 6, 8, 10]
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums= list(filter(lambda x: x%2==0, numbers))
print("2. Using filter() and lambda to extract all even numbers from a list of integers.")
print("Given numbers: ",numbers)
print("Even numbers: ",even_nums)

'''
Use reduce() and lambda to find the longest word in a list of strings.
from functools import reduce
words = ["apple", "banana", "cherry", "date"]
Expected Output: 'banana'
'''

words = ["apple", "banana", "cherry", "date"]
longest_word= reduce(lambda x,y: x if len(x)>=len(y) else y, words)
print("3. Using reduce() and lambda to find the longest word in a list of strings.")
print("Given words: ",words)
print("Longest word: ",longest_word)

'''
Use map() to square each number in the list and round the result to one decimal place.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
'''
print("4. Using map() to square each number in the list and round the result to one decimal place.")
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_of_floats= list(map(lambda x: round(x**2,1), my_floats))
print("Given floats: ",my_floats)
print("Square of floats: ",square_of_floats)

'''
Use filter() to select names with 7 or fewer characters from the list.
	my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
	Expected Output: ['olumide', 'josiah', 'omoseun']
'''
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names= list(filter(lambda x : len(x)<=7, my_names))
print("5. Using filter() to select names with 7 or fewer characters from the list.")
print("Given names: ",my_names)
print("Short names: ",short_names)

'''
Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
'''
print("6. Using reduce() to calculate the sum of all numbers in a list.")
sum= reduce(lambda x,y:x+y, [1, 2, 3, 4, 5])
print("Given list: ", [1, 2, 3, 4, 5])
print("Sum: ",sum)


''' Output:
1. Using map() to double each element of the given list.
Given list:  [1, 2, 3, 4]
List of double:  [2, 4, 6, 8]
2. Using filter() and lambda to extract all even numbers from a list of integers.
Given numbers:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers:  [2, 4, 6, 8, 10]
3. Using reduce() and lambda to find the longest word in a list of strings.
Given words:  ['apple', 'banana', 'cherry', 'date']
Longest word:  banana
4. Using map() to square each number in the list and round the result to one decimal place.
Given floats:  [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
Square of floats:  [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
5. Using filter() to select names with 7 or fewer characters from the list.
Given names:  ['olumide', 'akinremi', 'josiah', 'temidayo', 'omoseun']
Short names:  ['olumide', 'josiah', 'omoseun']
6. Using reduce() to calculate the sum of all numbers in a list.
Given list:  [1, 2, 3, 4, 5]
Sum:  15
'''