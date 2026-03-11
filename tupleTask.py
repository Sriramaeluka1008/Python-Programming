"""Coding Exercise:
1.Create a Tuple: Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the 
tuple"""

tuple=('sriram',22,'blue')
print(tuple)


"""2.Access Tuple Elements Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple."""

week_tuple=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(week_tuple[3])


"""3. Tuple Concatenation Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result."""

odd_tuple=(1,3,5)
even_tuple=(2,4,6)
print(odd_tuple+even_tuple)


"""4. Tuple Unpacking Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle."""

tuple=(5,5)
length,width=tuple
print(f"the area of recatngle is {length*width}")


"""5.Check if an Element Exists Write a program that checks if a given element 
exists in a tuple."""

tuple=(1,2,3,4,5,'python',6,7,8)
print('python' in tuple)




"""6.Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items
Sample Input:
items = [("Rice", 159), ("Banana", 60), ("Milk", 40)]"""

items = [("Apple", 159), ("Banana", 60), ("Milk", 40)]
print("Item\tPrice")
print("-"*20)
Total=0
for i, j in items:
    print(f"{i}\t{float(j)}")
    Total+=j
print("-"*20)
print(f"Total\t{float(Total)}")