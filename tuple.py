# List = Changeable
# Tuple = Fixed


# Tuple = multiple values ko ek single variable mein store karne ka collection.

# Tuple ko () parentheses se banate hain:




# fruits=("Apple","Banana","Grapes")
# print(fruits)




# Note: tuple me element append nhi kar sakte hai..

# Agar aapko tuple me koi element add karna hai, toh aap in do tareeqon (workarounds) ka use kar sakte hain:

# 1. List me convert karke (Recommended)
# Tuple ko pehle List me convert karein, usme append() karein, aur phir wapas Tuple bana dein.


my_tuple=(10,20,30,40)
temp_tuple=list(my_tuple)
temp_tuple.append(50)

# Wapas Tuple banaya
my_tuple=tuple(temp_tuple)
print(my_tuple)


# 2. Concatenation (+ operator) se
# Aap do tuples ko jod kar ek naya tuple bana sakte hain. (Dhyan rahe: Naye element ke sath comma , lagana zaroori hai).


my_tuple1=("Viru","Sheelu","Peudi")
my_tuple2=("Friends",)
my_tuple1+=(my_tuple2)
print(my_tuple1)


# Tuple mein bhi index 0 se start hota hai.
print("Index of FIrst Element : ",my_tuple[0])

# List ki tarah Tuple mein bhi negative indexing hoti hai.
# like, Negative Index is right-to-left

print(my_tuple1[-1])
print(my_tuple1[-2])
print(my_tuple1[-3])



# Tuple ka bhi ek part nikal sakte hain.
# Basic Slicing (start : stop)

numbers = (10, 20, 30, 40, 50, 60)

# Index 1 se lekar Index 3 tak (Index 4 include nahi hoga)
sub_tuple = numbers[1:4]
print(sub_tuple)  # Output: (20, 30, 40)



# Tuple mein different types ka data store kar sakte hain:

data = ("Viru", 25, 85.5, True)

print(data)

# Slicing with Negative Indexing
letters = ('a', 'b', 'c', 'd', 'e', 'f')

# Last ke 3 elements nikalna
print(letters[-3:])  # Output: ('d', 'e', 'f')

# Pehle element se lekar second-last element tak
print(letters[:-2])  # Output: ('a', 'b', 'c', 'd')


# Single Item Tuple
x=(10)  # ye tuple nhi hai
print(x)
print(type(x))

x=(10,)         # Single item tuple define me comma(,) zaroor lagate hai.
print(x)
print(type(x))


# Tuple Packing
# Multiple values ko automatically Tuple mein pack kar sakte hain:

student = "Rahul", 25, 85
print(student)
print(type(student))



# Tuple Unpacking
# Tuple Unpacking ka matlab hai ek tuple ke sabhi elements ko alag-alag variables me ek sath assign (nikalna) karna.
# Tuple ke values ko alag-alag variables mein nikal sakte hain.



student = ("Rahul", 25, 85)

name, age, marks = student

print(name)
print(age)
print(marks)



# Tuple mein Search

# in operator use kar sakte hain

fruits = ("Apple", "Mango", "Banana")

print("Mango" in fruits)


# Tuple par Loop
for fruit in fruits:
    print(fruit)


# Nested Tuple
students = (
    ("Rahul", 80),
    ("Amit", 75),
    ("Neha", 90)
)
print(students[0])   #output ("Rahul", 80)
print(students[0][0])  # output: Rahul
print(students[0][1])   # output: 80


# Tuple Repetition
numbers = (1, 2)

print(numbers * 3)

# list=["Apple","Banana","Grapes"]
# print(list[0])