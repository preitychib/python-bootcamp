# ========= All and Any =========

'''
Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
Input : numbers = [1, 2, 3, 4, 5]
#Expected Output : True
'''
print("1. Check if All Numbers are Positive.")
numbers = [1, 2, 3, 4, 5]
are_these_positive= all(x>0 for x in numbers)
print("Output: ",are_these_positive)

'''
Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
Input: numbers = [1, 3, 5, 7, 8]
#Expected Output: True
'''
print("2. Check if Any Number is Even.")
numbers = [1, 3, 5, 7, 8]
is_there_an_even= any(x%2==0 for x in numbers)
print("Output: ",is_there_an_even)

'''
Determine if any number in a list is divisible by 5 an print.
''' 
print("3. Determine if any number in a list is divisible by 5 an print.")
numbers = [1, 3, 5, 7, 8]
is_there_a_five= any(x%5==0 for x in numbers)
print("Output: ",is_there_a_five)


'''
Output:
1. Check if All Numbers are Positive.
Output:  True
2. Check if Any Number is Even.
Output:  True
3. Determine if any number in a list is divisible by 5 an print.
Output:  True
'''