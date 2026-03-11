''' Task 1: Dictionary Update
# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# # Your code here
# # Output should be: {'name': 'python', 'age': 25, 'city': 'westgodavari'}'''

my_dict = {'name': 'python', 'age': 25}
# my_dict['city']="westgodavari"
# print(my_dict)#one way
my_dict2={'city':'west godavari'}#2nd way
my_dict.update(my_dict2)
print(my_dict)

"""Task 2: Dictionary Access
Write Python code to access and print the value associated with the key 'price' in 
the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1
200}
# Your code here
# Output should be: 1200"""

product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info['price'])#1st way
print(product_info.get('price'))#2nd way


"""Task 3: Dictionary Removal
Write Python code to remove the key-value pair with the key 'city' from the 
following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30"""

my_dict = {'name': 'john', 'age': 30, 'city': 'Bhimavaram'}
my_dict2=my_dict.pop('city')
print(my_dict)

"""Task 4: Dictionary Keys
Write Python code to print all the keys present in the following dictionary:
# Your code here
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundr
y'}
# Output should be: ['name', 'age', 'city'"""


my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())



"""Task 5: Dictionary Values
Write Python code to print all the values present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Your code here
# Output should be: ['python', 25, 'tanuku']"""

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())

print('------------task 2--------------')


# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.

dict_1={1:'CSE',2:'ECE',3:"EEE",4:'(IT,CSD,CSM)',5:'CIVIL'}
dict_1['6']='MECH'
print(dict_1)


# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific 
# key in a dictionary.

dict_2={'name':'ram','age':22,'city':'Hyderabad'}
print(dict_2.get('name'))


# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.

dict_2={'name':'raj','age':22,'city':'Warangal'}
dict_3=dict_2.pop('city')
print(dict_2)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary.

dict_2={'name':'ravi','age':28,'city':'delhi'}
print(dict_2.keys())

# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary.

dict_2={'name':'mahi','age':42,'city':'chennai'}
print(dict_2.values())


