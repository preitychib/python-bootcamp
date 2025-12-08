# ====== Decorators ======

'''
1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.

'''

import time

def get_total_time(func):
	def wrapper():
		start_time = time.time()
		func()
		end_time = time.time()
		print(f"Total time taken: {(end_time - start_time) * 1000} ms")

	return wrapper

@get_total_time
def append_numbers():
	number_list = []
	for i in range(1,1001):
		number_list.append(i)
	return number_list

print("1.Appending numbers to list and calculate total time taken")
append_numbers()

'''
2. Create a parameterised decorator retry that retries a function a specified number of times.

	@retry(3)
            def may_fail(name):
                  print(f"Hello, {name}!")
'''

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All retries failed!")
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
	print(f"Hello, {name}!")

print("\n2. Calling may_fail function with retry decorator")
may_fail("Preeti")
may_fail(9990,"error")
	
'''
3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.

          def square_root(x):
    		return x ** 0.5
'''

def validate_positive(func):
    def wrapper(*args, **kwargs):
        if args and args[0] < 0:
            raise ValueError("Argument must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print("\n3. Testing validate_positive decorator")
try:
    result = square_root(16)
    print(f"Square root of 16 is {result}")
    result = square_root(-4)
    print(f"Square root of -4 is {result}")
except ValueError as e:
    print(f"Error: {e}")

'''
4. Create a decorator cache that caches the result of a function based on its arguments.
	@cache
      	def expensive_computation(x):
    		print("Performing computation...")
    		return x * x
	
	expensive_computation(5)
	expensive_computation(5)

     Write a cache decorator for it to check if the calculation is already performed then return the result.
'''

def cache(func):
	cache_dict = {}
	def wrapper(*args):
		if args in cache_dict:
			print(f"Cache hit for args: {args}")
			return cache_dict[args]
		result = func(*args)
		cache_dict[args] = result
		print(f"Cache miss for args: {args}, result cached")
		return result
	return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print("\n4. Testing cache decorator:")
print(f"Result first time: {expensive_computation(5)}")
print(f"Result second time: {expensive_computation(5)}")
print(f"Result third time: {expensive_computation(5)}")


'''
5. Create a decorator requires_permission that checks if a user has the ‘admin’ 
permission before allowing access to a function,
 if a different user then responds “Access denied”.

 	 def delete_user(user, user_id):
    		print(f"User {user_id} deleted by {user['name']}")

	user1 = {'name': 'Alice', 'permissions': ['admin']}
	user2 = {'name': John, 'permissions': ['dev']}
	user3 = {'name': 'Kurt', 'permissions': ['test’']}
'''

class User:
	def __init__(self, name, permissions):
		self.name = name
		self.permissions = permissions
	
	def has_permission(self, permission):
		return permission in self.permissions
	
	def require_permission(func):
		def wrapper(self,*args, **kwargs):
			if not self.has_permission('admin'):
				raise PermissionError(f"Access Denied")
			return func(self,*args, **kwargs)
		return wrapper
	
	@require_permission
	def delete_user(self, user_id):
		print(f"User {user_id} deleted by {self.name}")

user1 = User("Alice", ["admin"])
user2 = User("Bob", ["dev"])
user3 = User("Charlie", ["test"])

print("\n5. Testing permission decorator:")
try:
    user1.delete_user(123)
    user2.delete_user(123)
except PermissionError as e:
    print(f"Error: {e}")


'''
1.Appending numbers to list and calculate total time taken
Total time taken: 0.04220008850097656 ms

2. Calling may_fail function with retry decorator
Hello, Preeti!
Attempt 1 failed: may_fail() takes 1 positional argument but 2 were given
Attempt 2 failed: may_fail() takes 1 positional argument but 2 were given
Attempt 3 failed: may_fail() takes 1 positional argument but 2 were given
All retries failed!

3. Testing validate_positive decorator
Square root of 16 is 4.0
Error: Argument must be positive

4. Testing cache decorator:
Performing computation...
Cache miss for args: (5,), result cached
Result first time: 25
Cache hit for args: (5,)
Result second time: 25
Cache hit for args: (5,)
Result third time: 25

5. Testing permission decorator:
User 123 deleted by Alice
Error: Access Denied
'''