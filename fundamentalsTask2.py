1.#print statement
print("My name is Sriram")#o/p My name is Madhuri
#comments
2.#explaing the single and multiple line comments
'''
comments=comments are used to explain the code
single line comments=which are used to write the brief code
multi line comments=which are used to write the large discriptive
'''
#data structures & datatypes

sample_list=[65,5.4,(2,'rice',1.3),"sweet"]
print(sample_list)#o/p [65, 5.4, (2, 'rice', 1.3), 'sweet']
employee_id={10,11,12}
print(type(employee_id))#<class 'set'>

#string operations

name1="sri"
name2="ram"
print(name1+name2)#sriram
print(name1*3)#srisrisri

#python keywords
'''
if=5 #here we taken python keyword int as variable
print(if)#showing an error because keywords have predefined meaning'''

#type conversions
num1 = 5.6
print(type(num1))#<class 'float'>
print(int(num1))# 5
print(type(int(num1)))#<class 'int'>

num2=6#int==>string
print(type(num2))#<class 'int'>
print(str(num2))# 6
print(type(str(num2)))#<class 'str'>
#input&output
age=input("enter age:")#56
print(age)#o/p 56

#EXERCISE
#1.print statement
print('#')
print('##')
print('###')
print('####')
print('#####')
#2.comments
#performing multiplication of 2 numbers
num1=3
num2=3
print(num1*num2)#o/p 9
'''
here num1 stores the value of 3
num 2 stores the value of 3
in print statement it performs multiplication of 2 numbers and display the output 
'''
#3.data structures and datatypes
sample_dict={"title":"Rasp","author":"ramu","publicated on":2003}
print(sample_dict)# o/p {'title': 'Ramu', 'author': 'ramu', 'publicated on': 2003}
print(type(sample_dict))#<class 'dict'>
#4.string operations
product_price=input("enter price:")# 359
print(product_price)# 359
print(type(product_price))
print(float(product_price))#359.0
print(type(float(product_price)))#{'title': 'Rainbow', 'author': 'surender', 'publicated on': 2003}
#5.concatenate strings
name1="sree"
name2="ram"
print(name1+name2)# o/p sreeram
#6.type conversion
age=input("enter age:")#35
conversion=int(age)
print(type(conversion))#int
print(conversion+5)#o/p 40

#7.input and output
num1=5
num2=3
print(num1*num2)#o/p 15
