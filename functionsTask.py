# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and returns their sum.

def add(a,b):
    return a+b

#example:
result=add(135,5)
print(result)

# Task 2:Square Function
# Write a Python function named square that takes a number x as input and return its square.

def square(x):
    return x*x

x=int(input("enter the number :",))
print(F"square of {x} is :",square(x))

# Task3:Factorial Function
# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.

def factorial(n):
        if n == 0 or n == 1:
          return 1
        else:
          return n * factorial(n - 1)
        

num=int(input("enter the number is:",))
print(F"Factorial of {num} is:", factorial(num))

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.

def maximum(numbers):
   return max(numbers)

numbers=[34,45,78,1,108,34,56,]
print("Maximum value of numbers in the list is :",max(numbers))

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and returns its reverse.

def reverse(s):
    return s[::-1]

s=str(input("enter the text:",))
print("Reverse string is:",reverse(s))

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .

def is_prime(n):
        if n <= 1:
         return False
        for i in range(2, n):
         if n % i == 0:
          return False
        return True

n=int(input("enter the number is :"))
print(F"Given number is :",is_prime(n))

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Enter a positive number: "))
print("Fibonacci number:", fibonacci(num))

# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .

def is_palindrome(s):
    s = s.lower()          
    return s == s[::-1]    

print(is_palindrome("madam"))     
print(is_palindrome("ram"))
print(is_palindrome("python"))   

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.

def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

numbers=(1,2,3,4)
print("sum of squares of numbers is :",sum_of_squares(numbers))

#Task 10:
#write a python function named average list of numbers as input and returns the average value.

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

num_list = [17, 25, 33, 45, 28]
result = average(num_list)
print("Average:", result)
