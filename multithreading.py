#multi threading
# Threading is a technique where a program can run multiple operations (tasks) concurrently (at the same time) using threads.

#     A thread is the smallest unit of a program that can be executed independently.

#     Python has a built-in module called threading to work with threads.

#     A thread shares the same memory space as other threads in the same process


# Multithreading is the process of running multiple threads at the same time within the same program.

# import time
# def square(numbers):
#     print(f"square numbers")
#     for i in numbers:
#         print(f"square of {i} is {i**2}")
# list_1 = [1,2,3,4,5]
# square(list_1)


# def cubes(numbers):
#     print(f"cubes numbers")
#     for i in numbers:
#         print(f"cubes of {i} is {i**3}")
# list_1 = [1,2,3,4,5]
# cubes(list_1)







# import time
# def square(numbers):
#     print(f"square numbers")
#     for i in numbers:
#         print(f"square of {i} is {i**2}")
#         time.sleep(0.2)
# initial_time = time.time()
# list_1 = [1,2,3,4,5]
# square(list_1)
# print(f"time taken {time.time()-initial_time}")

# def cubes(numbers):
#     print(f"cubes numbers")
#     for i in numbers:
#         print(f"cubes of {i} is {i**3}")
#         time.sleep(0.2)
# initial_time = time.time()
# list_1 = [1,2,3,4,5]
# cubes(list_1)
# print(f"time taken {time.time()-initial_time}")



import threading
import time
def square(numbers):
    print(f"square numbers")
    for i in numbers:
        print(f"square of {i} {i**2}")
        time.sleep(0.2)
def cubes(numbers):
    print(f"cube numbers")
    for i in numbers:
        print(f"cubes of {i} {i**3}")
        time.sleep(0.2)
initial_time = time.time()
list_1 = [1,2,3,4,5]
t1= threading.Thread(target=square,args = (list_1,))
t2 = threading.Thread(target=cubes,args = (list_1,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"time taken {time.time()-initial_time}")



#  Main Reason:

# To do multiple tasks at the same time (concurrently) within a single program.


# Use Case Example	Why Threads Are Useful
# Downloading multiple files	All downloads run in parallel

# Threads are used to run multiple tasks concurrently without waiting for one to finish — making your program faster and more responsive.






# projects

#1. dictionary
#2. ATM functions
#3. super market
#4. BMS *
#5. Ebook
#6. EDA *
#7. webscraping
#8. railway ticket reservation
#9. to do list
#10. django related student management