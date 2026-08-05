# *********************************************
# Loop in Python
# Python mein 2 types ke loops hote hain:
#1- for loop
#2- while loop
# ***********************************************

# for i in range(0, 6):
#     print(i)



# Table print
# num = 5

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# Even Number
# range(start,stop,increment/decrement)
# for i in range(2, 21, 2):
#     print(i)

# Odd Number
# for i in range(1, 21, 2):
#     print(i)

# Second Methond for print odd Number
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)



# While uses
i = 1

# while i <= 5:
#     print(i)
#     i += 1


num = 5
i = 1

# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1



# Reverse a number.
# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reverse Number =", reverse)


# Find the factorial of a number
# 5!= 5 * 4 *  3 * 2 * 1 * 0!

# num=int(input("Enter a Number : "))

# fact=1
# while num>0:
#     fact=num*fact    
#     num=num-1

# print(fact)



# Count the digits in a number

num=int(input('Enter a Number : '))

count = 0

while num > 0:
    count += 1
    num = num // 10

print("Total Digits =", count)