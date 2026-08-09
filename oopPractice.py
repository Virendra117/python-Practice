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

         