
# Simple Question

# Del Keyword

# class Student:

#  def __init__(self, name):
#     self.name = name

# s1 = Student("Rehan")
# print(s1.name)
# del s1.name
# print(s1.name)





#  (OOP)

# Q1

# class Player:
#     club_name1 = "Paris-Saint-Geman"
#     club_name2 = "Real-Madrid"
#     name = "anonymous"  #class attribute

# # Default Constructors:
#     def __init__(self):
#        print("adding new database string")


#     def __init__(self, name, score):
#       self.name = name # obj attribute > class attribute
#       self.score = score
#       print("adding new database string")

# # Creation of different different methods in python
#     def welcome(self):
#          print("welcome player", self.name)

#     def get_score(self):
#         return self.score
 

# # p1 = Player("Ronaldo", 900)
# # p1.welcome()
# # print(p1.get_score())

# # print(p1.club_name1)
# #    #    OR
# # print(Player.club_name1)



# p2 = Player("Messi", 800)
# p2.welcome()
# print(p2.get_score())
# # p2.name
# # p2.score


# print(p2.club_name2)
#    #    OR
# print(Player.club_name2)







# Q2

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

# class Student:

#    def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks

   # @staticmethod
   # def hello():
   #  print("hello")

      
# method 1

#    def get_avg(self):
#       sum = 0
#       for val in self.marks:
#         sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# method 2

#    def get_avg(self):
#      ave = sum(self.marks) / 3
#      print("average of marks", ave)
    

# s1 = Student("Rehan", [78, 76, 79])
# print(s1.name)
# print(s1.marks)
# s1.get_avg()

# s2 = Student("Zeeshan", [90, 88, 91])
# print(s2.name)
# print(s2.marks)
# s2.get_avg()

# s3 = Student("Arslan", [89, 88, 86])
# print(s3.name)
# print(s3.marks)
# s3.get_avg()





# Q3

# Encapsulation Method of (OOP) 

# Create Account class with 2 attributes, balance & account no.
# Create methods for debit, credit & printing the balance

# class Account:
    
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#    #  Debit Card
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())

#    #  Credit Card
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount,"was credited")
#         print("Total Balance", self.get_balance())

#    #  Printing the balance
#     def get_balance(self):
#         return self.balance

# acc1 = Account(100000, 123456)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(13000)
# print(acc1.balance)
# print(acc1.account_no)






# Q4

# Inheritance

# Single-Level Inheritance

# class Car:
   
#     @staticmethod
#     def start():
#         print("car has started...")

#     @staticmethod
#     def stop():
#         print("car has stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car1.start())
# print(car1.stop())





# Q5

# Multi-Level Inheritance

# class Car:
   
#     @staticmethod
#     def start():
#         print("car has started...")

#     @staticmethod
#     def stop():
#         print("car has stopped...")
  
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, car_type):
#         super().__init__("Toyota")
#         self.type = car_type

# car1 = Fortuner("diesel")

# car1.start()
# print(car1.brand)
# print(car1.type)











#######################                          19 Dec 2025                          #############################
  

# Super Method

# class Car:
    
#     def __init__(self, car_type):
#         self.car_type = car_type
   
#     @staticmethod
#     def start():
#         print("car has started...")

#     @staticmethod
#     def stop():
#         print("car has stopped...")

# class ToyataCar(Car):
#     def __init__(self, name, car_type):
#         super().__init__(car_type)
#         self.name = name

# car1 = ToyataCar("grande", "electric")
# print(car1.type)
# car1.start()
# car1.stop()






# Class Methods

# class Person:
#     name = "anonymous"

# #First Way

#     # def changeName(self, name):
#     #     self.__class__.name = "Rehan Parveez"

# # Second Way

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("David Attenborough")
# print(p1.name)
# print(Person.name)







# Improving Above Solved Practice Question About Transactions: Add Transaction Limits with Abstraction

# Task:
# Modify the Account class to include a daily transaction limit of Rs. 50,000.

# If a credit or debit exceeds the limit, it should not process and should display an error message.


# class Account:
#      def __init__(self, bal, acc):
#           self.balance = bal
#           self.account_no = acc

#      # Debit Card
#      def debit(self, amount):
#           if amount <= 50000:
#                self.balance -= amount
#                print("Transaction is valid and completed")
#           else:
#                print("Transaction is not valid nor completed")

#           print("Rs.", amount, "was debited")    
#           print("your remaining balance is", self.get_balance())

#     # Credit Card:
#      def credit(self, amount):
#       if amount <= 50000:
#            self.balance += amount
#            print("Transaction is valid and completed")
#       else:
#            print("Transaction is not valid nor completed")
     
#       print("Rs.", amount, "was credited")
#       print("your updated balance is", self.get_balance())

#      def get_balance(self):
#            return self.balance

# acc1 = Account(100000, 12345)
# print(acc1.account_no)
# print(acc1.balance)
# acc1.credit(47000)
# acc1.debit(45000)

# acc2 = Account(50000000, 23423)
# print(acc2.account_no)
# print(acc2.balance)
# acc2.debit(20000) 
# acc2.credit(30000)






# Property Decorator

# class Student:
#    def __init__(self, name, phy, che, math):
#       self.name = name
#       self.phy = phy
#       self.che = che
#       self.math = math

# ##First Way
  
#    def calPercentage(self):
#          self.percentage = str((self.phy + self.che + self.math) / 3) + "%"
#          return self.percentage

# ## Second Way

#    # We use @property decorators on any method in the class to use the method as the property

#    # @property   
#    # def calPercentage(self):
#    #    return str((self.phy + self.che + self.math) / 3) + "%"
   
# stud1 = Student('Mubashir', 85, 87, 90)
# print(stud1.calPercentage())

# stud1.phy = 79
# print(stud1.calPercentage())

# # for @property method
# # stud1 = Student('Mubashir', 85, 87, 90)
# # print(stud1.calPercentage)
   
# # stud1.phy = 79
# # print(stud1.calPercentage)





# Using Encapsultion Concept

# class Account:
#     def __init__(self, acc_no, acc_pass):
#       self.acc_no = acc_no
#       self.__acc_pass = acc_pass  

#     def reset_pass(self):
#        print(self.__acc_pass)

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass)
# print(acc1.reset_pass())


# class Account:
#    def __init__(self, acc_no, acc_pass):
#       self.acc_no = acc_no
#       self.__acc_pass = acc_pass
      
#    def reset_pass(self):
#       return self.__acc_pass
   
# acc1 = Account('12345', 'abcde')
# print(acc1.acc_no)
# print(acc1.__acc_pass)
# acc1.reset_pass()














#######################                          22 Dec 2025                          #############################
      
      
# Inheritance Based

# Qs. Define a Employee class with attributes department, organization & designation. This class is also have a showDetails()
#  method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.


# class Employee:
#    def __init__(self, department, organization, designation):
#       self.department = department
#       self.organization = organization
#       self.designation = designation
   
      
#    def showDetails(self):
#         print("Department:", self.department)
#         print("Organization :", self.organization)
#         print("Designation :", self.designation)
        
# class Engineer(Employee):
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       super().__init__('Engineer', 'LDA', 'SDO')
      
# eng1 = Engineer('M. Zeeshan', 25)
# print(eng1.name) 
# print(eng1.age)
# eng1.showDetails()
      
      
      
      

# class Complex:
#    def __init__(self, real, img):
#       self.real = real
#       self.img = img
      
#    def showNumber(self):
#       print(self.real, 'i +', self.img, 'j')
      
#    def __add__(self, num2):
#       newReal = self.real + num2.real
#       newImg = self.img + num2.img
#       return Complex(newReal, newImg)
      
#    def __sub__(self, num2):
#       newReal = self.real - num2.real
#       newImg = self.img - num2.img
#       return Complex(newReal, newImg)
      
# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(5, 4)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num4 = num1 - num2
# num4.showNumber()




# def numType(num):
#    if num % 2 == 0:
#       print("num is even")
#    else:
#       print("num is odd")
#    print([1, 2, 3] + [4, 5, 6]) # concatenating

# numType(4)





# Program TO Convert USD TO INR

# def convert(usd_val):
#     pkr_val = usd_val * 280
#     print(usd_val, "USD =", pkr_val, "PKR")
    
# convert(50)





# Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area) method of the class which calculates the area of the circle.
#  Define a Perimeter method of the class which allows you to calculate the perimeter of the circle.


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
 
#     def area(self):
#         return (22/7) * (self.radius ** 2)
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())





# WAF TO PRINT THE ELEMENT OF A LIST IN SINGLE LINE


# Names = ['rehan', 'zeeshan', 'arslan']
# Profession = ["Developer", "Engineer", "Doctor"]

# print(Names[0], end=" ")
# print(Names[1], end=" ")
# print(Names[2], end=" ")

# def list_length(list):
#     print(len(list))

# list_length(Names)
# list_length(Profession)





# Given a list of 6 elements, swap the second and second-last elements.

# orig_list = [10, 20, 30, 40, 50, 60]
# print("Before Swapping orig_list[1], orig_list[-2]:", orig_list[1], orig_list[-2])
# orig_list[1], orig_list[-2] = orig_list[-2], orig_list[1]
# print("After Swapping orig_list[1], orig_list[-2]:", orig_list[1], orig_list[-2])




# # Extract and print the second and fourth elements using indexing (not slicing).

# original_list = [10, 20, 30, 40, 50]

# # Extracting elements at specific indices
# indices_to_extract = [1, 3]
# extract_elements = [original_list[i] for i in indices_to_extract]
# print(f"Extracted Elements: {extract_elements}")


# # Extracting elements based on a condition
# filtered_elements = [x for x in original_list if x > 25]
# print(f"Filtered_elemnts: {filtered_elements}")




      
# Code to Replace the middle element of a list with 0 of any list items length (Even or Odd)

# list1 = [100, 200, 300, 400, 500, 600, 700, 800]

# length = len(list1)
# mid = length // 2

# if length % 2 == 0:
#     print("Before Middle Elements:", list1[mid-1], list1[mid])
    
#     list1[mid - 1] = 0
#     list1[mid] = 0
    
#     print("After Middle Elements:", list1[mid-1], list1[mid])

# else:
#     print("Before Middle Element:", list1[mid])
    
#     list1[mid] = 0
    
#     print("After Middle Element:", list1[mid])



















#######################                          23 Dec 2025                          #############################


# Nested if Statement with else Condition

# Example

# num = 12
# print("num:", num)

# if num % 2 == 0 and num % 3 == 0:
#     print("Divisible by num 2 and 3")

# elif num % 2 == 0:
#   print("Divisible by num 2 not by 3")

# elif num % 3 == 0:
#     print("Divisible by num 3 not by 2")

# else:
#    print("Not Divisible by num 2 and 3")





#  Problem check If a Name Exists in the List:

# You are given a list of names (strings) and a target name.
# Search the list and tell if the target name exists in the list or not.


# def list_names(arr, target):
#     for i in range(len(arr)):
#         if(arr[i] == target):
#             return True
#     else:
#         return False
    
# names = ["Naseem", "Sajid", "Arslan", "Zeeshan", "Rehan"]
# target = "Sajid"
# index = list_names(names, target)
# print("Found at Index:" if index == True else "Not Found", index)




#example usage of zip and dict combine

# a = [2, 3, 5]
# b = ['arslan', 'zeeshan', 'rehan']
# print(a,b)
# pracice = list(zip(a,b))
# print(pracice)
# print(dict(pracice))





# Q handling prime numbers and simple multiplication of numbers which aren't prime numbers

# for num in range(10, 20):
#     for i in range(2, num):
#         if num%i == 0:
#             j = num/i
#             print("%d equals %d * %d" % (num,i,j))
#             break
#         else:
#             print(num, "is a prime number")
#             break




#  Problem find the Last Occurrence of a Target Number:

# You are given a list of integers and a target number.
# Find the last index at which the target occurs in the list.
# If it doesn’t occur, return -1.

# def list_num(arr, target):
#     last_index = -1
#     for i in range(len(arr)):
#         if(arr[i] == target):
#             last_index = i
#     return last_index

# num = [2, 3, 4, 5, 7, 5]

# target = 5
# index = list_num(num, target)
# print("Founda at index:" if index != -1 else "Not Found", index)





# What if the same num exists at two indexes then write logic to count both the indexes

# def list_num(arr, target):
#    last_index = -1
#    indexs = []
#    for i in range(len(arr)):
#       if(arr[i] == target):
#          last_index = i
#          indexs.append(i)
#    return last_index, indexs

# num = [2, 3, 4, 5, 6, 7, 5]
# target = 5
# last_index, indexs = list_num(num, target)

# if last_index != -1:
#    print("found at index:", indexs)
#    print("full count:", len(indexs))
#    print('last_position:', last_index)





# Question

# You are given words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
      
# words = ['apple', 'banana', 'apple', 'banana', 'banana', 'mango']

# unique = []
# count = []

# for w in words:
#     if w not in unique:
#         unique.append(w)
#         count.append(1)
#     else:
#         index = unique.index(w)
#         count[index] += 1

# print(unique, count)





# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

# def reverse_words(string):
#     result = ""
#     word = ""

#     for ch in string:
#         if ch != " ":
#             word += ch
#         else:
#             result += word[::-1] + " "
#             word = ""

#     result += word[::-1]   # last word
#     return result
 
# # took help of chatgpt in this mainly for like how to reverse each word instead of whole string, means keeping the correct
# # order of the entered strings while just reversing words
 
# print(reverse_words("Abdus Salam was the first Pakistani who won nobel prize in Physics")) 



 
      
      
      
      
      
      
      
      
      
#######################                          24 Dec 2025                          #############################
      
      
      
      
# Practicing File Handling in Python

# Example 1

# file = open("example.txt", "w")
# file = open("example.txt", "r")
# file = open("example.txt", "a")
# file = open("example.txt", "rb")



# Example 2

# fo = open("foo.txt", "wb")
# print("enter a name", fo.name)
# print("closed or not", fo.closed)
# print("opening mode", fo.mode)
# fo.close()




# Reading a File in Python

# Example: Using read() method

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)



# Example: Using readline() method

# with open("example.txt", "r") as file:
#     line = file.readline()
# while line:
#     print("line", end='')
#     line = file.readline()




# Example: Using readlines() method

# with open("example.txt", "r")as file:
#     line = file.readline()
# for lines in line:
#     print("line", end='')





# Writing to a File in Python

# Example: Using the write() method

# with open("foo.txt", "w") as file:
#   line = file.write("Hello World")
#   print(line)
#   print("Content added Successfully")




# Example: Using the writelines() method

# with open("example.txt", "w")as file:
#  file.writelines(["Hello\n", "World\n", "Python\n"])

# with open("example.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line, end='')





# PYTHON FILE HANDLING LEARNING CSV USE:


# import csv

# name = input("Enter your Name")
# age = input("Enter your age")
# roll_no = input("Enter your roll no")


# with open('data.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([name, age, roll_no])

# with open('data.csv', 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)




# How to read a CSV file into a Dictionary in Python


# import csv

# name = input("Enter your name")
# age = input("Enter your age")
# roll_no = input("Enter your roll no")

# with open("data1.csv", "a", newline="") as file:
#     print(f"\n{name},{age},{roll_no}")

# with open("data1.csv", "r") as file:
#     reader = csv.DictReader(file, fieldnames = ['Name', 'Age', 'roll_no'])
#     for line in reader:
#         print(line)





# Writing CSV file using csv module

# import csv

# data = ["month", "1959", "1960", "1961"]

# x = [
# ["Jan", "358", "359", "360"],
# ["Feb", "458", "459", "460"],
# ["Mar", "558", "559", "560"],
# ["Apr", "658", "659", "660"],
# ["May", "758", "759", "760"],
# ["June", "858", "859", "860"],
# ["July", "958", "959", "960"],
# ["Aug", "1058", "1059", "1060"],
# ["Sep", "1158", "1159", "1160"]
# ]

# y = "file.csv"
# with open(y, "w") as work:
#  z = csv.writer(work)
#  z.writerow(data)
#  z.writerows(x)






# import csv

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open("new_names.csv", "w", newline="") as new_file:
#         fieldNames = ['first_names', 'last_names']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerow(line)



# Q

# import csv

# # Asking user for new header names

# first_name = input("Enter header for first name")
# last_name = input("Enter header for last name")
# parents = input("Enter header for email")

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open("new_names.csv", "w", newline="") as new_file:
#         fieldnames = [first_name, last_name, parents]
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow({
#                 first_name: line['first_names'],
#                 last_name: line['last_names'],
#                 parents: line['email']
#             })



















#######################                          25 Dec 2025                          #############################


# simple to do list 

# tasks = []

# while True:
#     print("\n--- To-do List---")
#     print("1. Add Task")
#     print("2. View task")
#     print("3. Remove task")
#     print("4. Exit")

#     choice = input("enter your choice number(1-4)")

#     if choice == '1':
#         task = input("enter your task")
#         tasks.append(task)
#         print("task added successfully")
    
#     elif choice == '2':
#         print("\nYour Tasks")
#         if len(tasks) == 0:
#             print("no task found")
#         else:
#             for i, t in enumerate(tasks):
#                 print(f"{i+1} {t}")
#         input("\nclick enter to return to menu")

#     elif choice == '3':
#         print("Remove our task")
#         for i, t in enumerate(tasks):
#             print(f"{i+1}{t}")
            
#         if len(tasks) > 0:
#             try:
#                 task_num = int(input("enter your task"))
#                 if 1 <= task_num <= len(tasks):
#                   removed = tasks.pop(task_num - 1)
#                   print(f"remove task: {removed}")
#                 else:
#                     print("wrong task number")
#             except ValueError:
#                 print("your task number is not correct")

#         else:
#             print("enter task again")
#     elif choice == '4':
#         print("Exit! no task to peroform")
#         break
    
#     else:
#         print("wrong choice, enter task again")










# Student Class

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def show_info(self):
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_number)
#         print("Marks:", self.marks)

#         # Manually calculate average
#         total = 0
#         for mark in self.marks:
#             total = total + mark

#         subjects = len(self.marks)
#         if subjects != 0:
#             average = total / subjects
#         else:
#             average = 0

#         print("Average Marks:", average)

#         # Check if passed in all subjects
#         passed = True
#         for mark in self.marks:
#             if mark < 40:
#                 passed = False

#         if passed == True:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")

#         print("------------------------")

        
#  # ClassRoom Class
 
# class ClassRoom:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def show_all_students(self):
#         if len(self.students) == 0:
#             print("No students in the class")
#         else:
#             for student in self.students:
#                 student.show_info()


# # Main Program

# classroom = ClassRoom()

# while True:
#     print("---- MENU -----")
#     print("1. Add New Student")
#     print("2. Show All Students")
#     print("3. Exit")
#     print("--------------")

#     choice = input("Enter your choice (1, 2 or 3):")

#     if choice == "1":
#         name = input("enter student name:")
#         roll = input("enter roll number:")

#         sub_count = input("how many subjects?")
#         sub_count = int(sub_count)

#         marks = []
#         for i in range(sub_count):
#             mark = input("enter marks for subject " + str(i+1) + ": ")
#             mark = int(mark)
#             marks.append(mark)

#         student = Student(name, roll, marks)
#         classroom.add_student(student)

#     elif choice == "2":
#         classroom.show_all_students()
#         input('click enter to go to main menu')

#     elif choice == "3":
#         print("exiting program")
#         break

#     else:
#         print("wrong choice, Please enter 1, 2 or 3")





