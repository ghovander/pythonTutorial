# print("Garrett Hovander")
# print('o----')
# print(' ||||')
# print('*' * 10)

# x = 1  # int
# x = 1.1  # float
# x = 1 + 2j  # a + bi imaginary/complex numbers

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)  # returns float
# print(10 // 3)  # return int
# print(10 % 3)  # modulus
# print(10 ** 3)  # exponentiation

# price = 10  # int
# rating = 4.9  # float
# name = 'Garrett'  # string
# is_published = False  # boolean (Pascal Case)
# print(price)

# full_name = 'John Smith'
# age = 20
# is_new = True
# name = input('What is your name? ')  # functions that are built into python
# favorite_color = input('What is your favorite color? ')
# print(f'Hi {name} likes {favorite_color}')

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# course = '''
# Hi John,
#
# Here is our first email to you
#
# Thank you,
# Support Team
# '''
# print(course)

# course = 'Python for Beginners'
# print(course[0:2])

# beginners = 'Beginners'
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('P'))
# print(course.title())
# print(course.replace(beginners, f"Absolute {beginners}"))
# print('Python' in course)
# print(course)

# print(10 + 3)
# print(10 / 3)  # float
# print(10 // 3)  # int
# print(10 % 3)  # remainder
# print(10 ** 3)  # get exponent

# x = 10
# x += 3  # augmented assignment operator
# print(x)

# import math
#
# x = 2.9
# math.ceil(x)
# math.floor(x)
# print(round(x))
# print(abs(-2.9))  # module = file with reusable code

# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")

# has_high_income = False
# has_good_credit = True
# has_criminal_record = False
#
# if (has_high_income or has_good_credit) and not has_criminal_record:
#     print("Eligible for loan")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     print('x' * number)

# numbers = [5, 2, 1, 5, 7, 4]
# print(numbers.insert(0, 10))
# print(numbers.sort())
# print(numbers)
# print(numbers.count(5))
# print(numbers.remove(5))
# print(numbers.pop())
# print(numbers.index(5))
# print(numbers)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# numbers = (1, 2, 3)  # tuple - cannot be modified
# print(numbers)

# print(ord("b"))  # numeric representation of character

# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible" # ternary operator
# print(message)

# age = 22
# if 18 <= age < 65:  # Chaining Comparison Operators
#     print("Eligible")

# for number in range(1, 4, 2):
#     print("Attempt", number, number * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# even_numbers_count = 0
# for number in range(1, 10):
#     if not number % 2:
#         even_numbers_count += 1
#         print(number)
# print(f"We have {even_numbers_count} even numbers")


# def greet(first_name, last_name="Hovander"):
#     print("Hi there")
#     print(f"Welcome {first_name} {last_name}")


# greet("Garrett")

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Mosh")

# def increment(number, by):
#     return number + by


# print(increment(2, by=1))

# def increment(number, by=1):
#     return number + by


# print(increment(2))

# def multiply(*numbers): # xargs - allows variable numbers of arguments to be passed to a function with only one parameter defined. Creates Tuple.
#     total = 1
#     for number in numbers:
#         total = total * number
#     return total


# print(multiply(2, 3, 4, 5))

# def save_user(**user):  # xxargs - allows key/value pairs or keyword arguments to be packaged into a dictionary
#     print(user["id"])


# save_user(id=1, name="John", age=22)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1,2,3))

# def fizz_buzz(input):
#     fizz = "Fizz"
#     buzz = "Buzz"
#     is_fizz = input % 3 == 0
#     is_buzz = input % 5 == 0

#     if is_fizz and is_buzz:
#         return f"{fizz} {buzz}"
#     elif is_fizz:
#         return fizz
#     elif is_buzz:
#         return buzz

#     return input


# print(fizz_buzz(15))

# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(chars)

# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[-1])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers[::-1]) # reverse list

# numbers= [1, 2, 3]
# first, second, third = numbers
# # or
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# # can optionally split part of list into variable
# numbers = [1, 2, 3, 4, 4, 4, 4, 4]
# first, second, *third = numbers
# print(first)
# print(third)
# first, *third, second = numbers
# print(first)
# print(third)

# letters = ["a", "b", "c"]

# for index, letter in enumerate(letters):
#     print(index, letter)

# letters = ["a", "b", "c"]

# # Add
# letters.append("d")
# letters.insert(0, "-")
# print(letters)

# # Remove
# letters.pop(0) # method removal
# letters.remove("b")
# del letters[0:3] # delete statement
# letters.clear()
# print(letters)

# letters = ["a", "b", "c"]
# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))

# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# items.sort(key=lambda item:item[1])
# print(items)

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# x = map(lambda item:item[1], items)
# for item in x:
#     print(item)

# prices = list(map(lambda item:item[1], items))
# print(prices)

# items = [
#     ("Product 1", 10),
#     ("Product 2", 9),
#     ("Product 3", 12)
# ]

# prices = list(map(lambda item: item[1], items))
# prices = [item[1] for item in items] # list comprehension - Python way of writing the expression in the line above
# filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirect", browsing_session[-1])
# if not browsing_session:
#     print("disable")

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

# point = (1, 2)
# point = (1, 2) + (3, 4)
# point = (1, 2) * 3
# point = tuple([1, 2])
# point = tuple("Hello World")
# print(type(point))
# x, y = point
# if 10 in point:
#     print("exists")

# x = 10
# y = 11

# x, y = y, x
# a, b = 1, 2

# print("x", x)
# print("y", y)

# from array import array

# numbers = array("i", [1, 2, 3])
# print(numbers)

# numbers2 = ["hello", 1]
# print(numbers2)

# numbers = [1, 2, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# print(first | second) # gets union of sets - all unique objects from each set and new set created
# print(first & second) # intersection of two sets
# print(first - second) # get difference between sets
# print(first ^ second) # get symetric difference (objects only existing in one collection)

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2) # using keyword arguments to initialize the dictionary
# point["z"] = 20
# if "a" in point:
#     print(point["x"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for x in point:
#     print(x, point[x])
# for x in point.items():
#     print(x)
# for key, value in point.items(): # unpacking dictionary into variables for each iteration
#     print(key, value)

# values = {}
# for x in range(5):
#     values[x] = x * 2

# # [expression for item in items]
# values = {x: x * 2 for x in range(5)} # Dictionary Comprehension

# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

# from sys import getsizeof

# values = (x * 2 for x in range(1000))
# print("gen:", getsizeof(values))
# values = [x * 2 for x in range(1000)]
# print("list:", getsizeof(values))

# values = (x * 2 for x in range(10)) # creates iterable generator object that creates next values on the fly during each iteration, instead of holding a huge dataset in memory
# print(values)
# for x in values:
#     print(x)

# unpacking operator - by prefixing the variable with an asterisk(*), just like in javascript with the spread operator(...), all the objects can be unpacked and passed to the function as arguments
# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, *second]
# print(values)

# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)

# from pprint import pprint

# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1)
# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])

# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't eneter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown.")
# print("Execution Continues")

# try:
#     with open("app.py") as file:
#         print("File opened.")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()

# from timeit import timeit

# code = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
# """

# print("First Code:", timeit(code, number=10000))

# from timeit import timeit

# code = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise None
#     return 10 / age

# xfactor = calculate_xfactor(-1)
# if xfactor = None:
#     pass
# """

# print("First Code:", timeit(code, number=10000))

# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point = Point.zero()
# point.draw()
# print(point.default_color)
# print(Point.default_color)
# print(point.x)
# print(type(point))
# print(isinstance(point, Point))

# other1 = Point(10, 20)
# other2 = Point(1, 2)
# print(point == point)
# print(other1 > other2)
# print(other1 + other2)

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

# cloud = TagCloud()
# cloud["python"]
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.__tags)

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

# product = Product(50)
# print(product.price)

# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")

# # Animal: Parent, Base
# # Mammal: Child, Sub
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal Constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")

# m = Mammal()
# print(m.age)
# print(m.weight)
# print(isinstance(m, object))
# print(issubclass(Mammal, object))

# class Animal:
#     def eat(self):
#         print("eat")

# class Bird(Animal):
#     def fly(self):
#         print("fly")

# class Chicken(Bird):
#     pass


# class Employee:
#     def greet(self):
#         print("Employee Greet")

# class Person:
#     def greet(self):
#         print("Person Greet")

# class Manager(Employee, Person):
#     pass

# from abc import ABC, abstractmethod

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")


# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")

# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownList()
# textBox = TextBox()
# print(isinstance(ddl, UIControl))
# draw([ddl, textBox])


# class Text(str):
#     def duplicate(self):
#         return self + self

# text = Text("Python")
# print(text.duplicate())

# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)

# list = TrackableList()
# list.append("1")


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
# print(id(p1))
# print(id(p2))

# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(x=1, y=2)
# p2 = Point(x=10, y=2)
# p2 = Point(x=1, y =2)
# print(p1 == p2)

# from sales import calc_shipping, calc_tax # object from module
# import sales # module as an object

# calc_shipping()
# calc_tax()

# from ecommerce.shopping import sales
# import sys

# print(sys.path) # All the default paths for finding the module


# from ecommerce.shopping import sales

# print(dir(sales))
# print(sales.__name__) # magic attribute that returns name of module
# print(sales.__package__) # name of package
# print(sales.__file__) # file address


# from pathlib import Path

# class foo:
#     def __init__(self,p1):
#         self.a1 = p1

#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__

# path1 = foo(Path(r"C:\Program Files\Microsoft"))
# path12 = foo(Path("C:/Program Files/Microsoft"))
# print(path1 == path12)
# path2 = Path() # represents the current folder
# path3 = Path("ecommerce/__init__.py")
# path4 = Path() / "ecommerce" / "__init__.py"
# path5 = Path.home()


# from pathlib import Path

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# print(path.absolute())
# path = path.with_suffix(".txt")
# print(path.absolute())


# from pathlib import Path

# path = Path("ecommerce")
# # path.exists()
# # path.mkdir()
# # path.rmdir()
# # path.rename("ecommerce2")

# paths = [p for p in print(path.iterdir()) if p.is_dir()]
# print(paths)
# py_files = [p for p in path.rglob("*.py")] # used for recursive folder/file search
# print(py_files)


# from pathlib import Path
# from time import ctime
# import shutil

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# path.read_bytes()

# print(path.read_text())
# path.write_text("...")

# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"

# shutil.copy(source, target)
# target.write_text(source.read_text())


# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")


# import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1000, 2, 15])
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# import json
# from pathlib import Path

# movies = [
#     { "id": 1, "title": "Terminator", "year": 1989 },
#     { "id": 2, "title": "Kindergarten Cop", "year": 1993 },
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["title"])

# pip commands
# install latest version of package: pip install <package_name>
# upgrade to latest version of existing package: pip install --upgrade <package_name>
# show all packages with their semantic versioning: pip list
# get specific package version: pip install <package_name>==<major.minor.patch>
#       patch can be wildcard asterisk which will get the latest compatible version or pip install <package_name>~=<major.minor.patch>
# uninstall package: pip install <package_name>

# import requests

# response = requests.get("http://google.com")
# print(response)

# virtual environment commands
# creating virtual environment: python -m venv env
# activate environment: env\Scripts\activate.bat
# deactivate environment: deactivate

# pipenv
# install pipenv: pip install pipenv
# install package: pipenv install <package_name>
# installation location: pipenv --venv
# activate virtual environment: pipenv shell
# deactivate virtual environment: exit
# install missing packages with pipenv file: pipenv install
# install missing packages with pipenv.lock file: pipenv install --ignore-pipfile
# view dependency tree: pipenv graph
# uninstall package: pipenv uninstall <package_name>
# update outdated packages (checks packages version numbers in pipfile): pipenv update --outdated

# publishing packages
# install ve packages for publishing packages: pipenv install setuptools wheel twine
# create distribution package: python setup.py sdist bdist_wheel
#      sdist = source distribution
#      bdist = built distribution
# upload sdist & bdist files to pypi: twine upload dist/*

# pydoc
# switch for creating html doc from module documentation: pydoc -w <package_name>.<module_name>
# host documentation on port: pydoc -p 1234

# import time 

# def send_emails():
#     for i in range(1000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# from datetime import datetime
# import time

# dt = datetime(2018, 1, 1)
# dt = datetime.now()
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d") # converts string representation of a datetime to a datetime object. To configure format, you can use directive (Year: %Y, Month: %m, Day: %d)
# dt = datetime.fromtimestamp(time.time())
# print(dt)
# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m")) # converts datetime objects into a string

# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("second", duration.seconds)
# print("total_seconds", duration.total_seconds())

# import random
# import string

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)


# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# template = Template(Path("template.html").read_text())

# message = MIMEMultipart()
# message["from"] = "Mosh Hamedani"
# message["to"] = "testmime@maildrop.cc"
# message["subject"] = "This is a test"
# body = template.substitute({"name": "John"})
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("images/pythonImg.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testmime@maildrop.cc", "testmime")
#     smtp.send_message(message)
#     print("Sent...")