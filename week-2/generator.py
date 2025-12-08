# ===== Generator =====

'''
1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
Of 10  numbers 

Output:
0
1
1
2
3
5
8
13
21
34
'''

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("1. Fibonacci Generator")
for i in fibonacci_generator(10):
    print(i)

'''
3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.

word = “hello”
times = 5
'''
def repeat_word(word, times):
    for _ in range(times):
        yield word

print("3. Repeat Word")
print(list(repeat_word("hello", 5)))


'''
2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.

  Input n=3

Output:
3
6
9
12
15
…
'''

def infinite_multiples(n):
    while True:
        yield n
        n += n

print("2. Infinite Multiples of 3, use Ctrl+C to stop the generator")
for i in infinite_multiples(3):
    print("\n\n",i)
    

'''
======= Output =========
1. Fibonacci Generator
0
1
1
2
3
5
8
13
21
34
3. Repeat Word
['hello', 'hello', 'hello', 'hello', 'hello']
2. Infinite Multiples of 3, use Ctrl+C to stop the generator

Traceback (most recent call last):
  File "/home/preeti-chib/PythonProjects/PythonBootcamp/week-2/generator.py", line 65, in <module>
    print("\n\n",i)
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
'''