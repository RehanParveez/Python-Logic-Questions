
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

# class Student():

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
#         self.type = car_type
   
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
# car1.start()
# print(car1.type)







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
# p1.changeName("Rehan Parveez")
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
#                print("Transaction is Valid")
#           else:
#                print("Error, Transaction is not Valid")

#           print("Rs.", amount, "was debited")    
#           print("Total balance is =", self.get_balance())

#     # Credit Card:
#      def credit(self, amount):
#       if amount <= 50000:
#            self.balance += amount
#            print("Transaction is valid")
#       else:
#            print("Transaction is not Valid")
     
#       print("Rs.", amount, "was credited")
#       print("Total balance is =", self.get_balance())


#      def get_balance(self):
#            return self.balance

# acc1 = Account(100000, 12345)
# acc1.debit(45000)
# acc1.credit(47000)
# acc1.debit(3500)
# acc1.credit(4700)
# acc1.debit(55000)






# Property Decorator

# class Student:
#    def __init__(self, phy, che, math):
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
   
# stud1 = Student(85, 87, 90)
# print(stud1.calPercentage())

# stud1.phy = 79
# print(stud1.calPercentage())





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



