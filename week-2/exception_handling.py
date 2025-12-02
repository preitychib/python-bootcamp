
'''
Write a Python program that attempts to divide two numbers a = 10  b = 0
and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error
'''
a = 10
b = 0
try:
    print("1.Dividing",a,"by",b)
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


''' 
Apply exception handling to below code and handle an exception if the index is out of range. 
my_list = [1, 2, 3]
print(my_list[5])
'''
my_list = [1, 2, 3]
try:
    print("\n2.Printing element at index 5 for list with length 3:")
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")


'''Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a,b):
      result = a / b
      print(f"Result: {result}")

safe_divide(1,0)
safe_divide(1,”a”)
'''
def safe_divide(a,b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError as e:
        print("Error: Invalid input. Please provide numbers.",e.__str__())
    finally:
        print("Execution completed")
print("\n3.Safe divide function:")
safe_divide(1,0)
safe_divide(1,"a")

'''
1.Dividing 10 by 0
Error: Cannot divide by zero.

2.Printing element at index 5 for list with length 3:
Error: Index out of range.

3.Safe divide function:
Error: Cannot divide by zero.
Execution completed
Error: Invalid input. Please provide numbers. unsupported operand type(s) for /: 'int' and 'str'
Execution completed
'''