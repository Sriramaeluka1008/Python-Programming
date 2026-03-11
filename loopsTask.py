# # Task 1
# # sum of squares
sum=0
for i in range(1,6):
    squares=i**2
    sum+= squares
print(sum)

# Task-2
# # countdown from 5 to 1
count=6
while count>=2:
    count-=1
    print(count)

# # Task-3:
# # Multiplication table with nested for loop
table=int(input("Enter which table do you want to print"))
for i in range(1,11):
    for j in range(1,2):
        print(f"{table}X{i}={table*i}")


# # Task-4:
# ## sum of even numbers from 1 to 10 using for loop
sum=0
for i in range(0,11,2):
    sum+=i
print(sum)

# using if condtion
sum=0
for i in range(0,11):
    if i%2==0:
        print(i)

## Task-5
# # calculate the all numbers from 1 to a given number
num=int(input("Enter number"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)

# #Task-6
# # Print numbers in list using loop
num_list=[1,2,3,4,5,6,7,8,9,10]
for num in num_list:
    print(num)

# Task-7
## Display numbers from -10 to-1 using for loop
for i in range(-10,0):
    print(i)

# # Task-8
# # cubes of all numbers from 1 to a given number
num=int(input("Enter numbers"))
for i in range(1,num+1):
    print(i**3)

