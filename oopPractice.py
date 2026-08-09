# ---------------------------------------------------------------
# 1. Student Class

# Student नाम की class बनाइए।

# Properties:

# name
# age
# course

# Method:

# display()

# ----------------------------------------------------------------
class Student:   
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    
    def Display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)

s=Student("Virendra",32,"Data Analyst")
s.Display()

# --------------------------------------------------------------------
print("**********************************************************")

class Employee:
    def __init__(self,name, salary=0):
        self.name=name
        self.salary=salary

    def SalaryDisplay(self):
        print("Employee Name :", self.name)
        print("Salary : ", self.salary)


emp1=Employee("Virendra", 25000)    
emp1.SalaryDisplay()   

emp2=Employee("Surendra", 85000)    
emp2.SalaryDisplay()   


# --------------------------------------------------------
# 3. Rectangle Class

# Rectangle class बनाइए।

# Properties:

# length
# width

# Methods:

# area()
# perimeter()

# Formula:

# Area = length × width
# Perimeter = 2 × (length + width)

# Solution
print("*******************************************************")
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def Area(self):
          area=self.width*self.height
          return area      


    def Parameter(self):
        parameter=2*(self.width+self.height)
        return parameter


area1=Rectangle(20,12)

print("Area of Rectangle : ",area1.Area())
print("Parameter of Rectangle : ",area1.Parameter())




# Calculator class बनाइए।

# Methods:

# add()
# subtract()
# multiply()
# divide()
print("***************************************************************")

class Calculator:
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Add two numbers : ",(self.num1+self.num2))        
    def subtract(self):
        print("Substract two numbers : ",(self.num1-self.num2))        
    def multiply(self):
        print("Multiply two numbers : ",(self.num1*self.num2))        
    def divide(self):
        print("Divide two numbers : ",(self.num1/self.num2))        



calc=Calculator(12,20)
calc.add()
calc.subtract()
calc.multiply()
calc.divide()


# ******************************************************
# 5. Circle Class

# Circle class बनाइए।

# Property:

# radius

# Methods:

# area()
# circumference()

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("Area of Circle :",(3.14*self.radius*self.radius))

    def circumference(self):
        print("Circumfrence of Circle : ",(2*3.14*self.radius))



ac=Circle(10)
ac.area()
ac.circumference()


# *************************************************************************
# 6. Bank Account

# BankAccount class बनाइए।

# Properties:

# account_holder
# balance

# Methods:

# deposit()
# withdraw()
# check_balance()


class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount  
        print("Balance : ",amount)      



dpst=BankAccount("Virendra",1000)
dpst.deposit(500)