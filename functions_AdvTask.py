# Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the map() function with a lambda function to implement this.

def square_all(numbers):
    return list(map(lambda a: a**2, numbers))

list1 = [12, 21, 4, 8, 15]
result = square_all(list1)
print(result)

# Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. Use the filter() function with a lambda function to implement this.

def filter_positive(numbers):
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    return positive_numbers

list1 = [12,-6, 4, 101, 2, -2, 8, 108]
result = filter_positive(list1)
print(result)

# Write a Python function calculate_factorial(n) that calculates the factorial of a given number n . Use the reduce() function with an appropriate lambda function to implement this.

from functools import reduce

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda a, b: a * b, range(1, n + 1))
    
print(calculate_factorial(5))

# Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an appropriate lambda function to implement this.

from functools import reduce

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return reduce(lambda count, char: count + 1 if char in vowels else count, string, 0)

string = input("enter the text:")
result = count_vowels(string)
print("Number of vowels:", result)

# task with two lists using map function:
list1=[1,2,3,4,5,6,7,8]
list2=[8,9,10,11,12,13,14,15]

def square_all(numbers):
    return list(map(lambda a,b: (a**2,b**2), list1,list2))
result1=square_all(list1)
result2=square_all(list2)

print(result1,result2)