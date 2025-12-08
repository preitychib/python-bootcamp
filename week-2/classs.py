# ====== Classes =======

'''
1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
'''

class Person:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      def display_person(self):
            print(self.name, self.age)

print("Task 1. Create an instance and print its attributes")
person = Person("Preeti", 24)
person.display_person()

'''
2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
'''
class BankAccount:
      def __init__(self,account_number,balance,customer_name):
            self.account_number = account_number
            self.balance = balance
            self.customer_name = customer_name
      def deposit(self,amount):
            self.balance += amount
      def withdraw(self,amount):
            self.balance -= amount
      def check_balance(self):
            return self.balance

print("Task 2. BankAccount operations")
bank_account = BankAccount("123456789", 1000, "Preeti Chib")
bank_account.deposit(500)
bank_account.withdraw(200)
print(bank_account.check_balance())
'''
3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class

      book = Book.from_string("Python Programming, John Doe")
''' 

class Book:
      def __init__(self, title, author):
            self.title = title
            self.author = author
      
      @classmethod
      def from_string(cls, book_string):
            title, author = book_string.split(",")
            return cls(title.strip(), author.strip())

print("Task 3. Book class from_string method")
book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}, Author: {book.author}")

'''
4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.

'''

class Animal:
      def sound(self):
            print("Animal makes a sound")

class Dog(Animal):
      def sound(self):
            print("Dog barks")

class Cat(Animal):
      def sound(self):
            print("Cat meows")

print("Task 4. Animal inheritance with sound()")
# why this has not worked? like java do 
# why its None not the function
animal= Dog()
print("Dog sound: ", end="")
animal.sound()
animal=Cat()
print("Cat sound: ", end="")
animal.sound()

'''
5. Write a code to perform multiple inheritance.
	
'''

class Car:
      def __init__(self,brand):
            self.brand = brand
            
      def start(self):
            print(f"Car of brand {self.brand} is starting")

class Electric_Vehicle:
      def __init__(self,battery):
            self.battery = battery
            
      def charge(self):
            print(f"Electric vehicle with {self.battery} battery is charging")

class Electric_Car(Car, Electric_Vehicle):
      def __init__(self, brand, battery):
            Car.__init__(self, brand)
            Electric_Vehicle.__init__(self, battery)
            
      def start(self):
            Car.start(self)
            
      def charge(self):
            Electric_Vehicle.charge(self)

print("Task 5. Multiple inheritance test")
electric_car = Electric_Car("Tesla", "Lithium-ion")
electric_car.start()
electric_car.charge()
print(f"Electric car brand: {electric_car.brand}, battery: {electric_car.battery}")

'''
==== Output ====
Task 1. Create an instance and print its attributes
Preeti 24
Task 2. BankAccount operations
1300
Task 3. Book class from_string method
Title: Python Programming, Author: John Doe
Task 4. Animal inheritance with sound()
Dog sound: Dog barks
Cat sound: Cat meows
Task 5. Multiple inheritance test
Car of brand Tesla is starting
Electric vehicle with Lithium-ion battery is charging
Electric car brand: Tesla, battery: Lithium-ion
'''