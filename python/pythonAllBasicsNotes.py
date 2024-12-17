print("hello Eesha! welcome in the world of python😀 after c++ c# java-dsa css VB.NET js ts html😭")

# **************************Python variables**************************
# In Python, we can assign a value to a variable using the assignment operator (=).
# The variable name can be any valid Python identifier (a sequence of characters that starts with a letter
# or underscore and is followed by any number of letters, digits, or underscores).
# x = 5
# print(x)  # Output: 5
# x=10
# print(x)  #  Output: 10
# print(id(x))
# print(type(x))

# limitations of variables
# 1-no space in variable name
# 2- not start with any number
# 3- not start with any special character
# 4- not start with any underscore
# 5- variable name should be unique
# 6- variable name should not be a keyword in python

# standards of variables in python
# ---camel case : first alphabet of every word is small
# ---Pascal case : first alphabet of every word is capital
# ---Snake case : underscore after every word

# *********************Python data types*********************
# Python has several built-in data types, including:
# Integers (int): whole numbers, either positive, negative, or zero
# Floats (float): decimal numbers
# Strings (str): sequences of characters, such as words or sentences
# Boolean (bool): true or false values (True or false=> first alphabet is always capital) 
# Lists (list): ordered collections of items that can be of any data type, including strings,
# integers, floats, and other lists
# Tuples (tuple): ordered, immutable collections of items that can be of any data type,
# including strings, integers, floats, and other tuples
# Dictionaries (dict): unordered collections of key-value pairs
# Sets (set): unordered collections of unique items
# We can use the type() function to determine the data type of a variable
# print(type(5))  # Output: <class 'int'>
# python is not a typed variables
# python is dynamically typed

# f-string
# name = "Esha"
# age = 20
# print(f"Hello, my name is {name} and I am {age} years old.")

# multi-quotations in python => 
# the single and double quotations do not support multiple lines data but multi-quotations are used for next line coding 
# print('''
#       Hello, my name is Esha and I am 20 years old.
#       I am a student of computer science.
#       I am from Pakistan.
#       ''')


# *****************python-Arithmetic-Operators********************

# 1. Addition: a + b
# 2. Subtraction: a - b
# 3. Multiplication: a * b
# 4. Division: a / b
# 5. Floor Division: a // b
# 6. Modulus: a % b
# 7. Exponentiation: a ** b
# 8. Bitwise AND: a & b
# 9. Bitwise OR: a | b
# 10. Bitwise XOR: a ^ b
# 11. Bitwise NOT: ~a
# 12. Unpack operator: a, b = 1, 2
# 13. Augmented assignment operators: a += b, a -= b, a *= b
# 14. Multiplication-assignment operator: a *= b

# print(5 + 3)  # Output: 8
# print(5 - 3)  # Output: 2
# print(5 * 3)  # Output: 15
# print(5 / 3)  # Output: 1.666666666666666                         
# print(5 // 3)  # Output: 1 (integer division)
# print(5 % 3)  # Output: 2 (remainder)
# print(5 ** 3)  # Output: 125 (exponentiation)
# print(5 ** 0.5)  # Output: 2.236067977
# print(5 ** -3)  # Output: 0.125
# print(5 ** 0)  # Output: 1

# comparison operator:
# 1. Equal to: a == b
# 2. Not equal to: a != b
# 3. Greater then and equal to: a >= b
# 4. less then and equal to: a <= b

# x=10
# y=20
# print(x==y) # false
# print(x!=y) #true


# logical operators
# 1. and: a and b
# 2. or: a or b
# 3. not: not a
# print(5 > 3 and 3 > 1)  # Output: True
# print(5 > 3 or 3 > 1)  # Output: True
# print(not 5 > 3)  # Output: False
# print(5 > 3 and not 3 > 1)  # Output: False
# print(5 > 3 or not 3 > 1)  # Output: True


# assignment operators
# 1. =: a = b
# 2. +=: a += b
# 3. -=: a -= b
# 4. *=: a *= b
# 5. /=: a /= b
# 6. %=: a %= b
# 7. **=: a **= b
# 8. //=: a //= b
# print(x=10) # error


# membership operators
# 1. in: a in b
# 2. not in: a not in b
# print(5 in [1, 2, 3, 4, 5])   # Output: True
# print(5 not in [1, 2, 3, 4, 5]) # Output: False
# me = "esha"
# z=10
# # print(z in me) #error




# # ************************functions-in-python************************
# # function definition
# # def function_name(parameters):
# #     # function body
# #  return value
# # function calling
# # function_name(parameters)

# def hide():
#     print("hello Esha! welcome to the world of python")
    
# hide()    


# def addition(a,b):
#     return a+b

# result = addition(10,20)
# print(result)


# def sum(a,b):
#     return a+b

# print(sum(2,sum(10,10)))

# myName= "esha"

# def myInfo():
#     # print(f"My name is {myName} and my age is 20")
#     return myName
    
    
# me = myInfo()    
# print(me)



# global scope variables vs local scope variables in python:
# local scope variables are not accessible globally 
# global scope variables are accessible from any part of the program

# types of function arguments:
# 1. positional arguments
# 2. keyword arguments
# 3. default arguments=> defines in the function definition
# 3. Positional-only arguments
# 3. Keyword-only arguments
# 3. Arbitrary or variable-length arguments


# *****Built in functions in python*******
# 1. abs() => returns absolute value of a number
# 2. input()

# print(input("enter your name: "))


# def calculate(a,b):
#     return a*b

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))

# result = calculate(num1,num2)
# print(result)


# *****************Conditions-in-python****************

# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if-else statement
# isGreater = 11 < 50

# if isGreater:
#     print("11 is less than 50")

# if True:
#     print("this will print")

    
# num1 = int(input("enter the number: "))
# if num1 % 2 == 0:
#     print(f"The number {num1} is even")
#     if num1 < 50:
#         print(f"Number {num1}is not greater then 50")
#     else:
#         print("The number is less then 50")
# else:
#     print(f"The number {num1} is odd")
    
    
# if-elif-else statement    

# num = 10

# if num%2==0:
#     print("number is even")
# elif num==0:
#     print("number is zero")
# else:
#     print("number is odd")

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))

# if  num1 > num2 and num1 > num3:
#     print(f"{num1} is greater then {num2} and {num3}")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is greater then {num1} and {num3}")
# else:
#     print(f"{num3} is greater then {num1} and {num2}")
    
    
# ***************Match-case-conditions-in-python********************

# match-case statement is used to handle multiple cases in a single statement.
# It is used to replace the if-elif-else statement.
# It is used to handle multiple cases in a single statement.
# n = int(input("Enter the day number of week: "))

# match n:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3: 
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5: 
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Enter number from 1 to 7")    
            
            
# *********************Python-list-in-depth*********************            
# studentsName = ["zain","umer", "esha", "hamna", "zani"]
# print(studentsName[0])
# #nested list : 
# nestedStudentsName = ["umer",["esha","hamna"],["zani","ali"]]
# print(nestedStudentsName)

# output01 = ['Esha😻'] * 9
# print(output01) # ['Esha😻', 'Esha😻', 'Esha😻', 'Esha😻', 'Esha😻', 'Esha😻', 'Esha😻', 'Esha😻', 'Esha😻']

#builtIn-functions used for list
#pop()
#insert()
#append()
#extend()
#remove(value) 
#index(value)
#count()
#sort()
#reverse()
#clear()
#copy()
#len()
#slicing=> slicing = studentsName[2:4] # take the values from index 2 to 4 but value at index 4 is not included
# print(slicing)
# in => membership operator 

# studentsName.append("Tehzeeb") # one value from the end of list is added
# studentsName.insert(3,"tayyab") # add value at any index
# print(studentsName)
# studentsName.pop() # one value from the end of list is removed
# # studentsName.pop(2) # delete the value on the index
# print(studentsName)
# listOfNumbers = [2,5,6,7,8,9,1,3]
# # studentsName.extend(listOfNumbers) # extend the list by adding another list 
# print(studentsName)
# studentsName.remove("umer")
# print(studentsName)
# output = studentsName.count("umer") # count how many times a particular item is present in a list
# print(output)
# studentsName.sort()  # sort the values in ascending order
# print(studentsName) 
# studentsName.reverse() # reverse the list
# print(studentsName)
# studentsName.clear()
# print(studentsName) # empty the whole list  
# output  = studentsName.copy() # copy the list
# print(len(output)) # copy the list
# res = "tayyab" in studentsName
# print(res) # check if a value is present in the list or not return True / False
# slicing = studentsName[2:4] # take the values from index 2 to 4 but value at index 4 is not included
# print(slicing)

# *****************python-loops-in-depth********************

# -while loop => used to deals with variables 
# -for in => Mostly used to deal with lists
# -for in range loop => mostly used to create a list 
# map() loop
# filter() loop
#reduce()  loop


# i = 1
# while i<6:
#     print("Hello world")
#     i += 1
    
# f = 1
# while f<=10:
#     print(f"2 * {f} = {2*f}")    
#     f+=1
    
# lis = [10,20,30,40,50]    
# i = 0
# while i<len(lis):
#     print(lis[i]*2)
#     i+=1
# for item in lis:
#     print(item*2)  # for in loop is used to iterate over the list and print
    
    
# for item in range(1,11,1):
#     print(item)  # for in range loop is used to create a list from 1 to 10

   
   

# built-in functions used for for loop
# enumerate() => returns both the index and value of each item in the list
# zip() => returns an iterator of tuples where the first item in each passed iterator is paired together
# filter() => returns an iterator that filters elements from the iterable returning a boolean value
# map(function,no-of-iterations(list)) => applies a given function to each item of an iterable (such as a list or
# tuple) and returns a map object , takes two arguments 
# reduce() => applies a rolling computation to sequential pairs of values in a list
# lambda functions are the functions that have no function name and no need  to write return 

# for i, item in enumerate(lis):
#     print("loop running", item, i)
    
# userNames = ["Esha","hamna","zani","tehzeeb","umer","Ayyan","Tayyab","momi"] 

# for i ,item in enumerate(userNames):
#         newNames.append("hello "+item)
# print(newNames)


#  map():
# def changeUserNames(userName):
#     return f"hello {userName}"

# newNames = list(map(changeUserNames,userNames))  
# print(newNames)


# nums = [10,11,30,5,50,60,77,80]
# way-1
# def changeNums(items):
#     if items%2 == 0:
#        return 2*items 
#     else:
#         return items

# newNums = list(map(changeNums,nums))
# print(newNums) #updated new list is created 

# # way-2
# newList = list(map(lambda x: x*2, nums))
# print(newList) #updated new list is created


#filter(function, list): is used to reduce the list but the list don't changes only reduces we have to use map update the items of list 

# def multi(items):
#     if items%2==0:
#         # print(items) # when we don't return any thing then new list gives empty string
#         return items # Now new list contains only even numbers
        
# newLists = list(filter(multi,nums))
# print(newLists)


# *****************Dictionaries-in-python-deep-dive***********************
# 1. dictionary is mutable 
# 2. dictionary is unordered collection of key-value pairs
# 3. key is unique and immutable
# 4. key can be string, integer, float, tuple but not list or dictionary

# car = {
#     "color": "red",
#     "model": "BMW",
#     "numberOfDoors": 4,
#     "isElectric": False,
#     "company": "honda",
#     "price": 50000.0,
#     "info":{
#        "address" : "P-834567",
#        "phone": "123456789"
#     }
# }


# # dictionary data read:
# carP = car["price"]
# print(carP)
# color = car.get("color",{}) # if the value not found it returns empty strings {}
# print(color)

# # dictionary data update
# car["price"] = 60000.0
# print(car)

# # dictionary data add
# car["engineCC"] = "1200cc"
# print(car)

# dictionary data add
# del car["engineCC"]
# car.pop("color")
# car.popitem() # del the key-value from last
# print(car)


# **************Student-app-in-core-python**************
# studentsList = [
#     {
#         "id": 1,
#         "name": "John",
#         "email": "student1@gmail.com",
#         "rolNo": 10,
#         "class": "WMA" 
#     },
#     {
#         "id": 2,
#         "name": "Ali",
#         "email": "student2@gmail.com",
#         "rolNo": 11,
#         "class": "Python development"  
#     },
#     {
#         "id": 3,
#         "name": "Eesha",
#         "email": "student3@gmail.com",
#         "rolNo": 13,
#         "class": "AI development"  
#     },
#     {
#         "id": 4,
#         "name": "Hamna",
#         "email": "student4@gmail.com",
#         "rolNo": 14,
#         "class": "Word-press development"  
#     },
#     {
#         "id": 5,
#         "name": "Zainab",
#         "email": "student5@gmail.com",
#         "rolNo": 15,
#         "class": "Web development"  
#     },
# ]

# # Add new student
# print("Welcome to your college! Thanks for your admission. Please fulfill our requirements:")

# name = input("Enter your name: ")
# email = input("Enter your email: ")
# course = input("In which course do you want to take admission? ")

# newStudent = {
#     "id": len(studentsList) + 1,
#     "name": name,  # Use the inputted name instead of static "Zain"
#     "email": email,
#     "rolNo": 16,  # You might want to handle roll numbers differently in real applications
#     "class": course
# }

# studentsList.append(newStudent)
# print("Congratulations, your admission is done 💖")
# print(studentsList)

# # Update email of a given student by ID
# updateID = int(input("Enter the student ID to update the email: "))
# updateEmail = input("Enter the new email for the student: ")

# def updateStudent(student):
#     if student["id"] == updateID:
#         return {
#             "id": student["id"],
#             "name": student["name"],
#             "email": updateEmail,  # Update with the new email
#             "rolNo": student["rolNo"],
#             "class": student["class"]              
#         }
#     return student  # Return the student as is if ID doesn't match

# studentsList = list(map(updateStudent, studentsList))
# print("Updated Student List:")
# print(studentsList)

# # Delete student by ID
# deleteID = int(input("Enter the student ID to delete: "))
# studentsList = list(filter(lambda student: student["id"] != deleteID, studentsList))
# print("After Deletion:")
# print(studentsList)

# # Show all students' emails and IDs
# print("List of Students:")
# for student in studentsList:
#     print("Student Email: " + student["email"] + ", ID: " + str(student["id"]))  # Convert ID to string



# Note: 
# to add => append()
# to del => filter()
# to update => map()
# to show list => for in loop



# *********************python-tupples*******************
# Tuples are similar to lists but are immutable(don't del,update,add list). They are defined by enclosing values in parentheses instead
# of square brackets.
# Tuples are faster, more memory efficient,more suitable for use as function return values than lists and more more suitable for use as dictionary keys because they are immutable.
# we can only read the tupples in many ways 
# names = ("Tayyab" , "Esha")
# print(names[1])

# for username in names:
#     print(username)

# print(len(names))

# halfList = names[0:1]
# print(halfList)
                                      
# ****************python-Sets-Data-Structure*******************
# Sets are unordered collections of unique elements. They are defined by enclosing values in curly brackets.
# Sets are used to store a collection of unique elements. They are mutable and can be modified after
# they are created. Sets are faster and more memory efficient than lists because they don't store duplicate 
# sets methods are:
# add() - add an element to the set
# discard() - remove an element from the set if it is a member
# update() - update an element takes two arguments =>1st is current element and  2nd is the updated element 

# studentsEmailsSet = {"test1@gmail.com","test2@gmail.com","test3@gmail.com","test4@gmail.com"}
# print(studentsEmailsSet)
# studentsEmailsSet.add("test5@gmail.com")
# print(studentsEmailsSet)
# studentsEmailsSet.discard("test3@gmail.com")
# print(studentsEmailsSet)
# studentsEmailsSet.update("test5@gmail.com", "test9@gmail.com")
# print(studentsEmailsSet)

# we can also convert the existing list into sets so that the duplications in list is automatically removed

# listNums = [12,3,4,3,5,6,3,6,8,6,8,58,8,8,7,1,54,65,4]
# uniqueList = list(set(listNums))
# print(uniqueList)

# ****************string-handling-in-python**************

# Strings are sequences of characters. They are defined by enclosing values in quotes.
# Strings are immutable, meaning that once a string is created, it cannot be changed.
# Strings are sequences of characters. They are defined by enclosing values in quotes.


#built-in-functions for strings in python are: 
# 1. len() - returns the length of the string
# 2. lower() - returns the string in lowercase
# 3. upper() - returns the string in uppercase
# 2. str() - convert any datatype into string
# 3. print() - print the string on the screen
# 4. split() - split the string into a list where each word is a list item
# 5. join() - join the list into a string where each word is a string item
# 6. replace() - replace the old string with the new string in the given string
# 7. strip() - remove the leading and trailing spaces from the string
# 8. find() - find the index of the first occurrence of the given string in the
# given string
# 9. rfind() - find the index of the last occurrence of the given string in
# the given string
# 10. count() - count the number of occurrences of the given string in the
# given string
# 11. startswith() - check if the given string starts with the given string
# 12. endswith() - check if the given string ends with the given string
# 13. isalnum() - check if the given string contains alphanumeric characters
# 14. isalpha() - check if the given string contains alphabetic characters
# 15. isdigit() - check if the given string contains digits
# * => print the string no. of  times given 
# name = " esha niaz"
# repeatName = name * 3
# print(repeatName) #esha esha esha 
# print(name[2]) # indexing
# print(name[0:3]) #slicing 
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.strip()) # remove extra spaces 
# print(name.index('s')) # returns index number
# print(name.count('a')) # count numbers of a present 
# print(name.find('a')) # returns index number
# print(name.replace("esha","eman"))
# print(name.split()) # convert the string into list with help of white spaces
# # print("-".join(listName)) # convert the list into string 
# print(name.startswith("e")) # check if the string starts with e returns True or False
# print(name.endswith("z")) # check if the string ends with z returns True or False
# print(name.isalpha()) # check if the variables contains all string 
# print(name.isdigit()) # check if the variables contains all digit
# print(name.isspace()) 
# print(name.isalnum()) # check if the variables contains all alphanumeric
# num = 1
# print(len(str(num)))


# ***********************Exploring-python-modules**********************

#how to use modules: => every file becomes modules 
#from file_name import variableName/functionDefinition
# from generateText import userName 
# print(userName)

# as => is used to use any name in place of module real name or name of any function/variable in file
#example
# from generateText import userName as myName
# from generateText as textfile
# OR:
# from generateText #Here we import the complete module/file
    

# python-built-in modules/files
# 1. math - contains mathematical functions like sin, cos, tan, sqrt, log etc
# 2. random - contains random number generation functions like randint, uniform, choice etc
# 3. statistics - contains statistical functions like mean, median, mode etc
# 4. datetime - contains date and time functions like today, now, strftime etc
# 5. time - contains time functions like sleep, time, ctime etc
# 6. os - contains operating system functions like mkdir, rmdir, rename etc
# 7. sys - contains system functions like exit, argv etc
# 8. re - contains regular expression functions like search, findall, sub etc
# 9. itertools - contains functions for working with iterators like chain, cycle, groupby etc
# 10. collections - contains functions for working with collections like Counter, defaultdict etc
# 11. heapq - contains functions for working with heaps like heappush, heappop
# 12. bisect - contains functions for working with bisect like bisect_left, bis
# 13. copy - contains functions for working with copying like deepcopy, copy
# 14. operator - contains functions for working with operators like add, sub, mul etc
# 15. functools - contains functions for working with functions like reduce, partial etc
# 16. pickle - contains functions for working with pickling like dumps, loads etc
# 17. json - contains functions for working with json like dumps, loads etc
# 18. csv - contains functions for working with csv like reader, writer etc
# 19. urllib - contains functions for working with urls like urlretrieve, urlopen etc
# 20. requests - contains functions for working with http requests like get, post, put etc
# 21. socket - contains functions for working with sockets like socket, connect etc
# 22. select - contains functions for working with select like select, poll etc
# 23. threading - contains functions for working with threads like Thread, Lock etc
# 24. queue - contains functions for working with queues like Queue, LifoQueue etc
# 25. multiprocessing - contains functions for working with processes like Process, Pool etc
# 26. concurrent.futures - contains functions for working with concurrent futures like ThreadPoolExecutor, Process
# 27. contextlib - contains functions for working with context managers like contextmanager, ExitStack
# 28. logging - contains functions for working with logging like getLogger, basicConfig etc
# 29. traceback - contains functions for working with traceback like print_exc, format_exc etc


# import time 
# currentTime = time.time() # gives us the current time 
# time.sleep(4) # here the execution stops for 4 sec
# print(currentTime)


# import datetime 
# currentTime = datetime.date.today()
# print(currentTime)

# duration = datetime.timedelta(days=1,hours=6)
# total_second = duration.total_seconds()
# print(total_second)

# import random
# randoM = random.random()
# print(int(randoM * 500))
# # This gives random numbers between 1 and 100
# randomNumber = random.randint(a=1,b=100)
# print(randomNumber)
# import math 
# print(math.sqrt(5))
# print(math.factorial(3))

# by using os we can del with files or folders in over os and much more things ,we can also open or close any application or our window , os have all the control of our system 
# import os 
# # cwd()=> current working directory
# currentDir = os.getcwd()
# print(currentDir) # tell the name of current folder open 
# getFiles = os.listdir(currentDir) 
# print(getFiles) # return all the files present in current directory




# **********************Python-OOP-Class-Concept************************

# Every class contains attributes and function/methods

# in the function of class , the first parameter is always self
#self => list of attributes , we make every attribute using self 



# class Car: 
    # initialize function: => it automatically calls and we mostly create our all the attributes in init function
# the function defined with name __init__ is used to decide the attributes in a class    
    # def __init__(self,brand,price):
    #     # here we define the name and value of attributes 
    #     self.brand = brand
    #     self.price = price   
    #     self.doors = 4
    #     # drive function 
    # def drive(self,driver):
    #     myBrand = self.brand
    #     return driver + " start driving " + myBrand
    # def start(self):
    #     return self.brand + "started"
    
  
# # here car1 is like the dictionary / obj that contains class Car()
# car1 = Car("Lamborghini ", 234567)
# # __init__ is called automatically
# print(car1.brand,car1.price,car1.doors)
# # we have to call the function drive:
# output = car1.drive("Eesha")
# out = car1.start()
# print(out)
# print(output)

# car2 = Car("BMW", 123456 )
# print(car2.brand, car2.price)
# output2 = car2.drive("Tayyab")
# print(output2)


# class Teacher:
#     def __init__(self, name, email,education,salary,experience):
#         self.name = name 
#         self.email = email 
#         self.education = education 
#         self.salary = salary 
#         self.experience = experience
#     def details(self):
#         return self.name,self.email,self.education,self.salary,self.experience
    
# teacherDetails = Teacher("esha","eshaniaz5@gmail.com","AI_Developer",12345,"3-years")    
# print(teacherDetails)
# myOut = teacherDetails.details()
# print(myOut)

# # inheritance: 

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         def eat(self):
#             return self.name + " is eating"
#         def sleep(self):
#             return self.name + " is sleeping"
        

# now inherit this class in another class 

# class Cats(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#         def meow(self):
#             return self.name + " is meowing"
#         def eat(self):
#             return self.name + " is eating"
        
        
# *******************Four-pillars-of-oop***************      
# 1-inheritance => class with-in class
# 2-polymorphism => If two child classes inherit the same parent class like 1 parent class and two or more child classes
# 3-encapsulation => class variables will not call outside the class=> private variable : like  __name is not callable outside the class but can be get and use through the function 
# 4-abstraction => Where we only make the functions in class but don't define the the logic, the logic is defined in the child

# Example of abstraction:  => The logic in not defined in the parent class
# class Person:
#     def __init__(self):
#         pass
#     def getProperties(self):
#         pass
    
# class Student(Person):
#     def __init__(self,name , age):
#         super().__init__()
#         self.name = name 
#         self.age = age
#     def showProperties(self):
#         print("Name: ", self.name)
 
 
  
# class Person:
#     def __init__(self, name, age):
#         # Using a single underscore for protected variable
#         self._name = name
#         self.age = age
    
#     def printProperties(self, Username, UserAge):
#         self._name = Username  # Updating the name
#         self.age = UserAge  # Updating the age
#         return f"My name is {self._name} and my age is {self.age}"
    
#     def getProperties(self):
#         return self._name   

# class Student(Person):
#     def __init__(self, name, age, rollNo):
#         # Now include name and age parameters
#         super().__init__(name, age)
#         self.rollNo = rollNo
    
#     def getRollNumber(self):
#         return self.rollNo

# Create an object of Student with all required parameters
# obj = Student("John", 18, 12)

# # Print age
# print(obj.age)   

# # Retrieve and print properties
# print(obj.getProperties()) 

# # Print the updated properties
# print(obj.printProperties("Esha", 20))

    
    
           
        
# #  creating the instance of class        
# obj = Person("Eesha",20)        
# # now the private variable __name is not callable outside the class => This is called encapsulation
# # print(obj.__name)  error 
# # now we access the private name through function
# outs = obj.getProperties()
# print(outs)
# print(obj.age)
# myself = obj.printProperties("Tayyab",27)
# print(myself)
      
# Creating the instance of class student



# ******************Error-handling-in-python**********************
# Types of errors
# syntax error  => complier  can detect
# Exceptional or runtime error => Error because of space etc means that occur at the run time
# logical error => Error that is only detected  by developer nor system
# semantic error


# Exceptional Error:
# 1. ZeroDivisionError: This error occurs when we try to divide a number by zero
# 2. TypeError: This error occurs when we try to perform an operation on a wrong data
# 3. ValueError: This error occurs when a function receives an argument with an incorrect value
# 4. IndexError: This error occurs when we try to access an index that does not exist
# 5. KeyError: This error occurs when we try to access a key that does not exist
# 6. ImportError: This error occurs when we try to import a module that does not exist
# 7. AttributeError: This error occurs when we try to access an attribute that does not exist



# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")
# except Exception as e:
#     print(f"An error occurred: {e}")

# try:
#     x = 5 / 0
#     loader = True
# except ZeroDivisionError:
#     loader = False
#     print("Error: Division by zero is not allowed")
# except Exception as e:
#     loader = False
#     print(f"An error occurred: {e}")
# except ValueError as e:
#     print(f"An Value error occurred: {e}")
# else:
#     print("error")    
# finally:
#     loader = False
#     print("This will run regardless of whether an exception occurred or not")
    


# *****************File-handling-in-python******************
# File handling in Python is a way to interact with files using Python programs. It allows you to
# read and write data to files, which can be useful for storing and retrieving data.
# There are several types of file handling in Python, including:
# 1. Reading a file: This involves opening a file and reading its contents.
# 2. Writing to a file: This involves opening a file and writing data to it.
# 3. Appending to a file: This involves opening a file and adding data to the
# end of the file.
# 4. Deleting a file: This involves deleting a file from the file system.
# 5. Renaming a file: This involves renaming a file from the file system.
# 6. Copying a file: This involves copying a file from one location to another.
# 7. Moving a file: This involves moving a file from one location to another.
# 8. Checking if a file exists: This involves checking if a file exists in the file
# system.
# 9. Getting the size of a file: This involves getting the size of a file in
# bytes.
# 10. Getting the last modified date of a file: This involves getting the last
# modified date of a file.


# modes 
# r=> read
#  w => write
#  a => append
#  r+ => read and write
#  w+ => read and write
#  a+ => read and write
#  x => create
#  b => binary mode
 
# file = open("./example.txt","r+") # r=> mood
# content = file.read()
# # content = file.readlines()
# file.writelines("Ohhhh python is such a crazy thing! I can write and write in any file ")
# # file.close()

# print(content)

#with=> it is a good practice to use with so that we don't need to close the file manually

# with open("./example.txt","r+") as file:
#     print(file.readlines())

print("successfully 9th language done! but no benefits cuz I'm  a software engineer student. 🙂")