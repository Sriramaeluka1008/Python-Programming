# Reverse List: Write Python code to reverse the order of elements in the given list my_list.Print the reversed list. my_list = [10, 20, 30, 40, 50, 11].

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print("Reverse the order of numbers :",my_list)

# Common Elements: Given two lists list1 and list2 , find and print the common elements between them.list1 = [1, 2, 3, 4, 5] and list2 = [4, 5, 6, 7, 8]

list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7, 8] 
empty_list = []

for num in list1:
    if num in list2:
        empty_list.append(num)

print("Common elements:", empty_list)

# Unique Elements: Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
 # original_list = [1, 2, 2, 3, 4, 4, 5]

original_list = [1, 2, 2, 3, 4, 4, 5]
empty_list =[]

for num in original_list:
    if num not in empty_list:
        empty_list.append(num)

print("unique elements :",empty_list)


# Remove duplicate elements from the given list duplicated_list and print the list without duplicates while preserving the order.
# duplicated_list = [1, 2, 2, 3, 4, 4, 5].

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
empty_list =[]

for num in duplicated_list:
    if num not in empty_list:
        empty_list.append(num)
print("list without duplicate elements:",empty_list)

# lists concatenation : Write a Python script that concatenates two lists and prints the result.

list_1=[1,2,9,"python",86]
list_2=["kavya",3,5,7,20,56]
concatenate=list_1+list_2
print("Concatenate of two lists is :",concatenate)

# lists Repetition : Write a Python script that repeats a list three times and prints the result.

original_list=[1,"empid",20,23,100]
repeated_list=original_list*3
print("repeated list is :",repeated_list)

# lists removal : Write a Python script that removes the elements at even indices from a list.

original_list=[1,29,34,2,6,3,70,89,42]
new_list=original_list[1::2]
print(" list after removing elements at even indices:",new_list)

# list insertion : Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of the list.

original_list=[1,5,7,8]
new_list=[10,11,12]+original_list
print("new list is :",new_list)

# List comprehensions
# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.

squares=[i**2 for i in range(1,11)]
print(f"squares from 1 to 10 is {squares}")

# 2. Even Numbers: Generate a list of even numbers from 1 to 20.

numbers=[num for num in range(1,21) if num % 2 == 0]
print(f"Even numbers from 1 to 20 is {numbers}")

# 3. Words Lengths: Given a list of words, create a list containing the lengths of each word
# words = ["apple", "banana", "cherry", "date"].

words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]
print(" Each Word lengths:", lengths)