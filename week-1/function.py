# Functions

# 1. Define a function calculate_area that calculates the 
# area of a rectangle and return the result. 
# If no width is provided, it defaults to 10.
def calculate_area(length, width=10):
    return length * width

# 2.  Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Write a function that takes one parameter as a string and reverse it and return.

def reverse_string(s):
    return s[::-1]

# 4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 
# a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.
def sum_list(list_1, list_2):
    return sum(list_1) + sum(list_2)

# 5. Write a Python function that takes a list and returns a new list with distinct and sorted elements
#  from the first list. a = [4,1,2,3,3,1,3,4,5,1,7] Output = [1,2,3,4,5,7]
def distinct_sorted(numbers):
    return sorted(list(set(numbers)))


if __name__ == "__main__":
    # Test calculate_area
    print("1. Area with both parameters:", calculate_area(5, 3))
    print("Area with only length:", calculate_area(7))
    
    # Test factorial
    print("\n2. Factorial of 8:", factorial(8))

    # Test reverse_string
    print("\n3. Reverse of 'hello':", reverse_string("hello")) 
    
    # Test sum_list
    list_a = [8, 2, 3, 0, 7]
    list_b = [3, -2, 5, 1]
    print("\n4. Sum of list_a and list_b:", sum_list(list_a,list_b))
    
    # Test distinct_sorted
    test_list = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
    print("\n5. Distinct and sorted list:", distinct_sorted(test_list))

"""
======= OUTPUT =======

1. Area with both parameters: 15
Area with only length: 70

2. Factorial of 8: 40320

3. Reverse of 'hello': olleh

4. Sum of list_a and list_b: 27

5. Distinct and sorted list: [1, 2, 3, 4, 5, 7]
"""