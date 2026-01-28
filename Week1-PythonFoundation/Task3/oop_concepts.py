# OOP Concepts
# Classes & Objects
# Encapsulation


class Student:
    name = "majid"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


class Car:
    color = "blue"
    brand = "Honda"

car1 = Car()
print(car1.color)
print(car1.brand)



# Consructor: all classes have _init_() function, which is executed when object is initiated.

# attributes = variables.
class Student:   
    def __init__(self, name, marks):
        print("adding new student")
        self.name = name
        self.marks = marks

s1 = Student("majid",20)
print(s1.name)
print(s1.marks)

s2 = Student("ali",50)
print(s2.name)
print(s2.marks)



# class and instance attributes

class Student: 
    college_name = "comsats" 
    def __init__(self, name, marks):
        print("adding new student")
        self.name = name
        self.marks = marks

s1 = Student("majid",20)
print(s1.name)
print(s1.marks)
print(s1.college_name)
print(Student.college_name)


# methods, functions that belong to objects

class Student: 
    college_name = "comsats" 
    def __init__(self, name, marks):      #constructor
        self.name = name
        self.marks = marks
    def welcome(self):
        print("welocome", self.name)
    def get_marks(self):
        return self.marks


s1 = Student("majid",20)
print(s1.name)
print(s1.marks)
print(s1.college_name)
s1.welcome()
print(s1.get_marks())



# static method

class Student: 
  
    @staticmethod        #decorator
    def welcome():
        print("welocome")


s1 = Student
s1.welcome()



# abstraction: hiding unnecessry details of a class
# encapsulation: wraing data and functions into sigle unit



class Account:
    def __init__(self, acc_no,bal):
        self.acc = acc_no
        self.bal = bal
    def balance(self):
        return self.bal
    def credit(self,cr):
        self.bal += cr
    def debit(self,dr):
        self.bal -= dr


c1 = Account(1223,1000)
print(c1.balance())
c1.credit(100)
print(c1.bal)
c1.debit(100)
print(c1.balance())


