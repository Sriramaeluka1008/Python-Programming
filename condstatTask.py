#1. Vowel Checker
"""Write a Python program that takes a character as input and checks whether
it is a vowel or not"""
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is not a vowel")


#2. Age Group Classification
"""Write a program that takes an age as input and classifies the person into
one of the following age groups"""
age = int(input("Enter your age: "))

if age < 0 or age >100:
    print("Invalid age")

elif age >= 0 and age <= 12:
    print("Child")

elif age >= 13 and age <= 17:
    print("Teenager")

elif age >= 18 and age <= 64:
    print("Adult")

else:
    print("Senior")

#3. Number Classifier
"""Write a program that takes an integer as input and classifies it as positive,
negative, or zero"""
num = int(input("Enter a number: "))
if num > 0:
    print(f"give number is positive")
elif num < 0:
    print(f"given number is negative")
else:
    print(f"given number is zero")

#4. Leap Year Checker:
"""Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400."""

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"given {year} is leap year")
else:
    print(f"given {year} is not a leap year")
    
#5. Calculator:
"""Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation"""
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

print(f"Addition of two numbers is ",num1 + num2)
print(f"Subtraction of two numbers is",num1 - num2)
print(f"Multiplication of two numbers is",num1 * num2)
print(f"Division of two numbers is",num1 / num2)

#6. Short Hand If:
#Rewrite the following code using the short-hand if statement
'''x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"'''

x = int(input("Enter a number: "))
result = "Even" if x % 2 == 0 else "Odd"
print(result)

#7. Discount Calculator:
'''Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input.'''
original_price = float(input("Enter original price: "))
dicount_percent = float(input("Enter dicount percentage: "))

dicount_amount = (original_price * dicount_percent)/100
final_price = original_price - dicount_amount
print("final price after discount is",final_price)

#8. BMI Calculator:
'''Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input.'''
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
BMI = weight / (height**2)
print("your BMI is:",BMI)
