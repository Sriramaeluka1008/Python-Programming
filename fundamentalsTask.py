# Item1: Create a Python script with both single-line and multi-line 
# comments explaining the purpose of the script.

# The below print statement displays a sample message
print("This is a sample Python program")
'''
The below code performs a subtraction operation.
Var1 represents the value 50.
Var2 represents the value 30.
Using the subtraction operator (-), we calculate the result.
'''
Var_1 = 69
Var_2 = 32
Result = Var_1 + Var_2
# Display the result of the subtraction
print(Result)

# Item2: Declare two variables:
# One variable stores a string (Employee Name)
# The other variable stores an integer (Employee Salary)
employee_name = "Sriram"
employee_salary = 30000
# Display the employee name
print(employee_name)
# Display the employee salary
print(employee_salary)

#Item3: Write a program that prints a pattern using multiple print statements.

print('Python Life')
print('8545')
print("this is sample programm")
print(1.5, 2.5, 3.5)
print('reddy')

#Item4 : Create a Python script for a simple task and add comments to explain each step
#Create variables of different data types(int,float,str) and print their values.
# Step 1: Variable Declaration

employee_id = 21641         # Employee ID (integer)
employee_name = 'kanth'     # Employee Name (string)
employee_height = 5.5       # Employee Height in feet (float)
employee_city = "sec"        # Employee City (string)
product_id = 53             # Product ID (integer) 


# Step 2: Display the declared variables using print statements

print("Employee ID:", employee_id)
print("Employee Name:", employee_name)
print("Employee Height:", employee_height)
print("Employee City:", employee_city)
print("Product ID:", product_id)

#Item5: Determine the memory location and data type of a variable.

product_name = 'science Guide'  #Variable storing the product name (String)
print(id(product_name))    #Print the memory location (unique ID) of the variable
print(type(product_name))  #Print the data type of the variable

product_count = 785   # Variable storing product count (Integer)
print("Printing the memory location of the variable is:" ,  id(product_count))
print("Printing the data type of the variable is:", type(product_count))

product_weight = 20.4 #variable storing the product weight (Float)
print("Printing the memory location of the variable is : ", id(product_weight))
print("Printing the data type of the variable is : ", type(product_weight))

#Item6: Create a program that takes user age = “23ˮ, converts it to an integer,and then prints the result type.
employee_Age = "23"
print(type(employee_Age))  # Output : <class 'str'>
###converting string to Integer using type conversion 
integer_Conversion = int(employee_Age)
print("Successfully converted this variable to Integer:", integer_Conversion)
#data type check after conversion to Integer
print("Data type after conversion:", type(integer_Conversion))

#Item7: Converting Integer value to float 
ProductSale_Count = 653
print(type(ProductSale_Count))
float_conversion = float(ProductSale_Count)
print(type(float_conversion))
print("Successfully converted to Float ", float_conversion) #output : 342.0

#Item8: Concatenate two strings and print the result using Input().
Department_Name  = input("Department name : ")
Department_id =  input("Enter department id :")
manager_id = input("Enter manger id : ")
result_concat = Department_Name + Department_id + manager_id
print("Contactinating and printing for user inputs:" , result_concat)

#Concatenate and type convertion from string to INT
Number_1 = '33'
Number_2 = '44'
Num_result = Number_1 + Number_2
print(type(Num_result))  #output : <class 'str'> Output is 77

Integer_convert1  = int(Number_1)
print(type(Integer_convert1)) #output : <class 'int'>
Integer_convert2  = int(Number_2)
print(type(Integer_convert2)) #output : <class 'int'>
Final_resutset= Integer_convert1 + Integer_convert2
print(Final_resutset) #output is 75 

# Item9: Repeat special characters, strings, and numbers multiple times
# Step 1: Print repeated characters and strings
special_character1 = "!"
special_character2 = '@'
special_character3 = '''#'''
special_integer = 89
special_float = 54.2
special_string = 'Sample'

# Step 2: Print repeated characters and strings
print(special_character1 * 56)
print(special_character2 * 35)
print(special_character3 * 75 )
print(special_integer * 120)
print(special_float * 60)
print(special_string * 21)