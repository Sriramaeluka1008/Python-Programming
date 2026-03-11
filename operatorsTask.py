# TASK - 1

# Program that takes user input for their name and age. Using formatted (f-strings) to print a message welcoming a user and stating their age

name = input("Enter name :    ")
age = input("enter age :   ")
print(f"Welome the user {name} and stating their age as {age}")

# list creation that contains integers from 1 to 10
number = [1,2,3,4,5,6,7,8,9,10]
print(5 in number)
print(15 not in number )
print (20 in number)



# TASK - 2


# 1.  Program to calculate the area of a rectangular using the given formula area - length * width
print(" **** Task 2 Started **** ")

length = int(input(" Enter the length :"))
width = int(input("Enter the width : "))
area = length * width
print(area)

# 2. Program to demonstrate incrementing and decrementing a variable
#increment
print("variable incrementation")
product_cost = 150
product_cost += 15
print(product_cost)

# decrementation
print("variable decrementation")
product_cost = int(input("enter product cost : "))
product_cost -= int(input("Enter Decrement Value :"))
print(f" product cost after decrementation : {product_cost}")

# 3. Program to convert temperature from celius to Fahrenheit. 
# The formula for conversion is F = (C*9/5)+32.
# take the temperature celsius as input from the user.
c = int (input("Enter temperature in c : "))
fahrenheit = (c*9/5)+32 
print(fahrenheit)

# 4. Program to calculate the simple interest given the principal amount, rate and time

amount = int(input("enter the principal amount :   "))
rate = float(input("Enter the interest :   "))
time = int(input("enter the time :   "))
simple_interest = (amount*rate*time)/100 # formula is ptr/100
print(f" Simple interest is {simple_interest}")
 
 # 5. concatenate two strings and display the result. String taken from user

str1 = input(" Enter the first String :  ")
str2 = input("Enter second String  :    ")
str3 = str1 + ' ' + str2
print(f"Concatenation of two strings is {str3}")

# 6. program to convert from kilometer to miles.

kms = int(input("enter the kilometers to convert to miles"))
miles = kms * 0.621371
print(f" After converting given kms into miles : {miles} ")