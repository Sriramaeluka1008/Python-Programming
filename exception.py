# <----------------------Practice exceptional handling with examples------------------>


#1.finally block : (finally always executes whether the error occurs or not)
try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ended")

#2.filenotfounderror:( It Occurs when file does not exist)
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError, File not found.")

#3.try and except: (if user enters 0 also the program will not get error)
try:
    num1 = int(input("enter  the first number: "))
    num2 = int(input("enter  the second number: "))
    result = num1 / num2
    print("result:", result)
except ZeroDivisionError:
    print("Error:  It Cannot divide by zero")      

#4.else block:(else block runs,only if no exception occurs)
try:
    num = int(input("enter a number: "))
    result = 250 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)

#5.Value error:(Occurs when correct type but wrong value is given)
try:
    num = int("sri")   #<----- Invalid conversion
except ValueError:
    print("ValueError occurred, Cannot convert string to integer.")

#6.Type error:(Occurs when wrong data type is used)
try:
    result = "25" + 5   #<----- Cannot add string and integer
except TypeError:
    print("TypeError occurred,wrong data types.")

#7.RunTimeerror:(Occurs during program execution)
try:
    raise RuntimeError("Something went wrong!")
except RuntimeError:
    print("RuntimeError occurred!")

#8.Indexerror:(Occurs when accessing invalid index)
try:
    list1 = [8, 5, 2, 6]
    print(list1[6])
except IndexError:
    print("IndexError! List index out of range.")

#9.overflow error: (Occurs when result is too large)
import math
try:
    print(math.exp(2400))   # Very large number
except OverflowError:
    print("OverflowError, Number too large.")

#10. Exception :(Base class of all exceptions),Exception is the base class for all built-in exceptions
try:
    num = int("sri")
except Exception as e:
    print("Exception found")
    print("Error message:", e)

#11.IOerror:(Occurs during input/output operation failure)
try:
    file = open("sample.txt", "r")
    file.write("Hi")           #<----- Writing in read mode
except IOError:
    print("IOError! Cannot perform I/O operation.")

#12.object error:(Occurs when object has no such attribute)
try:
    x = 8
    x.append(4)                #<-----int has no append method
except AttributeError:
    print("AttributeError! Attribute not found.")

#13.keyerror:(Occurs when key not found in dictionary)
try:
    dict = {"name": "sri"}
    print(dict["id"])
except KeyError:
    print("KeyError! Key not found in dictionary.")

#14.zerodivisionerror:(Occurs when dividing by zero)
try:
    a = 18
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("ZeroDivisionError, Cannot divide by zero.")



