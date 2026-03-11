<!-- ------------------PYTHON MODULES---------------- -->

 <!-- **1) math – Mathematical operations** -->

 Example 1: Square root

 import math

 print(math.sqrt(25))   ----- output - 5

 Example 2: Power

 import math

 print(math.pow(2, 3)) ----- output  - 8


 <!-- **2) random – Random values** -->

 Example 1: Random integer

 import random

 print(random.randint(1, 10)) ---- output - (prints any random value in between 1-10)

 Example 2: Random choice

 import random

 print(random.choice(\["red", "blue", "green"])) ------- output - (prints any random choise or color from 3 )


 <!-- **3) datetime – Date and time** -->

 Example 1: Current date \& time

 import datetime

 print(datetime.datetime.now()) ---- output( prints current datetime)

 Example 2: Only current date

 import datetime

 print(datetime.date.today()) -----output( prints only current date)


 <!-- **4) os – Operating system interaction** -->

 Example 1: Current directory

 import os

 print(os.getcwd()) ------output (prints current working directory name)

 Example 2: List files

 import os

 print(os.listdir())


 <!-- **5) sys – System information** -->

 Example 1: Python version

 import sys

 print(sys.version)

 Example 2: Platform name

 import sys

 print(sys.platform)


 <!-- **6) json – JSON data handling** -->

 Example 1: Convert dictionary to JSON

 import json

 data = {"name": "Sai", "age": 22}

 print(json.dumps(data))

 Example 2: Convert JSON to dictionary

 import json

 text = '{"name":"Sai","age":22}'

 print(json.loads(text))


 <!-- **7) time – Time functions** -->

 Example 1: Current time

 import time

 print(time.time())

 Example 2: Delay program

 import time

 time.sleep(2)

 print("Waited 2 seconds")


 <!-- **8) collections – Special data structures** -->

 Example 1: Counter

 from collections import Counter

 print(Counter("apple"))

 Example 2: defaultdict

 from collections import defaultdict

 d = defaultdict(int)

 d\["a"] += 1

 print(d)


 <!-- **9) statistics – Statistical calculations** -->

 Example 1: Mean

 import statistics

 print(statistics.mean(\[10, 20, 30]))

 Example 2: Median

 import statistics

 print(statistics.median(\[10, 20, 30]))



 <!-- **10) sqlite3 – Simple database** -->

 Example 1: Create database

 import sqlite3

 conn = sqlite3.connect("test.db")

 print("Database created")

 conn.close()

 Example 2: Create table

 import sqlite3

 conn = sqlite3.connect("test.db")

 cursor = conn.cursor()

 cursor.execute("CREATE TABLE IF NOT EXISTS student(id INT, name TEXT)")

 conn.close()