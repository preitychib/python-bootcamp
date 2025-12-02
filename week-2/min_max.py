# ===== Min Max =====

'''Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
'''
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print("1. Find the Maximum and Minimum Values in a List")
print("Input: ",numbers)
print("Output: ",max(numbers),min(numbers))

'''
Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
'''
setn = {5, 10, 3, 15, 2, 20}
print("\n2. Given a set of numbers, find the maximum and minimum values.")
print("Input: ",setn)
print("Output: ",max(setn),min(setn))


'''
Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, 
in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.

Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
Output: ('kiwi', 'grapefruit')
'''
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print("\n3. Find the shortest and longest word from the list.")
print("Input: ",words)
print("Output: ",min(words,key=len),max(words,key=len))

''' Output
1. Find the Maximum and Minimum Values in a List
Input:  [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
Output:  79 1

2. Given a set of numbers, find the maximum and minimum values.
Input:  {2, 3, 20, 5, 10, 15}
Output:  20 2

3. Find the shortest and longest word from the list.
Input:  ['apple', 'banana', 'kiwi', 'grapefruit', 'orange']
Output:  kiwi grapefruit
''' 