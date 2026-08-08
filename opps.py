
from abc import ABC, abstractmethod
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

# class Student:

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Virendra")    # first data value
# s2 = Student("V3i Technnology")    # second data value

# print(s1.name)
# print(s2.name)


# 6. Four Pillars of OOPs

# (A) Inheritance

# एक Class दूसरी Class की Properties और Methods का उपयोग करती है।

# Parent Class

# class Animal:

#     def sound(self):
#         print("Animal Sound")


# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()


# Types of Inheritance

# 1. Single Inheritance
class A:
    pass

class B(A):
    pass


# Method Overriding

# Parent Class (Super Class)
# class Animal:

#     def make_sound(self):
#         print("Animal makes a sound")


# # Child Class (Sub Class)
# class Dog(Animal):
#     # Parent class के method को यहाँ override किया गया है
#     def make_sound(self):
#         print("Dog barks")


# # Objects बनाना
# my_animal = Animal()
# my_dog = Dog()

# my_animal.make_sound()  # Output: Animal makes a sound
# my_dog.make_sound()  # Output: Dog barks





# (B) Encapsulation

# Data और Methods को एक Class के अंदर रखना।

# class Bank:

#     def __init__(self):
#         self.balance = 5000

# b = Bank()

# print(b.balance)


# __str__() Method
# __str__() method allows us to define a custom string representation of an object. By default, 
# when we print an object or convert it to a string using str(), 
# Python uses the default implementation, 
# which returns a string like <__main__.ClassName object at 0x00000123>.

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# print(dog1)  
# print(dog2)



# def __init__():
#     return "Viru"


# sss=__init__()
# print(sss)


# (C) Abstraction

# ज़रूरी जानकारी दिखाना और Internal Details छिपाना।

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):

#     def sound(self):
#         print("Bark")

# d=Dog()
# d.sound()



        
