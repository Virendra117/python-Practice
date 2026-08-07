# OOPs (Object-Oriented Programming System) in Python

# 1. Class
# 2. Object    
# 3. Constructor (init)
# 4. Methods
# 5. Attributes
# 6. Four Pillars of OOPs
# (A) Encapsulation
# (B) Abstraction
# (C) Inheritance
# (D) Polymorphism



# Class and object

# Syntax

# class Student:
#     pass


# class Student:
#     name = "Rahul"

# print(Student.name)    


# Object 
# Object, Class का Instance होता है।

# class Student:
#     name = "Rahul"

# s1 = Student()

# print(s1.name)

# class Student:
#     name="Virendra"             # Properties

# # Creating object from class
# s2= Student()
# print(s2.name)



# 3. Constructor (init)
# __init__() constructor method

# class Student:

#     def __init__(self):
#         print("Constructor Called")

# s1 = Student()


# Constructor with Parameters

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Rahul", 20)

# print(s1.name)
# print(s1.age)





# self Keyword
# self वर्तमान Object को Refer करता है।

# class Student:

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Virendra")

# print(s1.name)



# 4. Methods
# Method वह Function है जो Class के अंदर बनाया जाता है।

# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name =", self.name)

# s1 = Student("Rahul")
# s1.display()




# 5. Attributes
# Instance Attribute

# हर Object का अलग-अलग Data होता है।

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Virendra")    # first data value
s2 = Student("V3i Technnology")    # second data value

print(s1.name)
print(s2.name)