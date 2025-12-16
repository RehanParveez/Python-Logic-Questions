
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

# class ToyatoCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyatoCar("fortuner")
# car2 = ToyatoCar("prius")

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

# class ToyataCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyataCar):
#     def __init__(self, type):
#         super().__init__("Toyota")
#         self.type = type

# car1 = Fortuner("diesel")

# car1.start()
# print(car1.brand)
# print(car1.type)

