print('hello V3i Technology')
print('***********************************')

# define varaible

# a=10 # integer varaible define
# b='V3i Technology' # string varaible define

# print(a,b)

# is_active=True
# is_finished=False

# **************************************************

# p=10
# q=21
# is_greater=p>q
# print(is_greater) # False

# ****************************************************

# use if in condition structure
# if condition:
    # statement

# ****************************************************

# 1. Check Positive, Negative, or Zero
# 2. Check Even or Odd Number
# 3. Check Voting Eligibility
# 4. Find Greater of Two Numbers
# 5. Find Smaller of Two Numbers
# 6. Find Largest of Three Numbers
# 7. Check Leap Year
# 8. Check Pass or Fail
# 9. Grade Calculator
# 10. Check Divisible by 5
# 11. Check Divisible by 2 and 5
# 12. Check Multiple of 3 and 7
# 13. Check Vowel or Consonant
# 14. Check Uppercase or Lowercase Letter
# 15. Check Alphabet, Digit, or Special Character
# 16. Check Driving License Eligibility
# 17. Check Senior Citizen Eligibility
# 18. Check Number is Three-Digit or Not
# 19. Login Validation (Username & Password)
# 20. Electricity Bill Category (Low/High Bill)


# ***************************************************
# age = 13

# if age >= 18:
#     print("You are an adult.")
# else:
#     print('You are not adult.')

# ****************************************************

# largest number of three numbers
# n1=12
# n2=9
# n3=16
# if n1>n2 and n1>n3:
#     print(f"First Number {n1} is greatest")
# elif n2>n3 and n2>n1:
#     print(f"Second Number {n2} is greatest")
# elif n3>n1 and n3>n2:
#     print(f"Third Number {n3} is greatest")

# ****************************************************

# num=23
# print(f'Number is {num}')

# ****************************************************

# name=input('Enter name :')
# print('Hello',name)

# ****************************************************

# Check Positive, Negative, or Zero
# number=int(input("Enter any number: "))

# if number>0:
#     print(f'Number {number} is positive')
# elif number==0:
#     print(f'Number {number} is Zero.')
# else:
#     print(f'Number {number} is Nigative.') 

# ****************************************************
# Check Even or Odd Number

# if number%2==0:
#     print(f'Number {number} is Even.')
# else:
#     print(f'Number {number} is Odd.')

# ****************************************************
# Check Leap Year

# if (number % 400 == 0) or (number % 4 == 0 and number % 100 != 0):
#     print(f'Year {number} is leap year.')
# else:
#     print(f'Year {number} is not leap Year')


# Check Pass or Fail
# Check Vowel or Consonant

str =input('Enter any charactor :')

# if str=='a' or str=='e' or str=='i' or str=='o' or str=='u':
#     print(f'\nCharactor {str} is Vowels')
# else:
#     print(f'\nCharactor {str} is Consonant')



# ****************************************************
#  uppercase and lowercase
# print(str.upper())
# print(str.lower())



# ****************************************************
# Check Alphabet , digit and Special Charactor
# if str.isalpha():
#     print('It is a Alphabets')
# elif str.isdigit():
#     print('It is a Digit')
# else:
#     print('it is Special Charactor')


# *******************************************

# 16. Check Driving License Eligibility

# if str.isdigit():
#     age=int(str)
#     if age>=18:
#         print('Eligible for Licencse')
#     else:
#         print('Not Eligible for License.')
# else:
#     print('Not Valid number.')

# *******************************************************
# 17. Check Senior Citizen Eligibility

# if str.isdigit():
#     age=int(str)
#     if age>=60:        
#         print('Your Senior Citizen')
#     else:
#         print("Not a Senior Citizen.")
# else:
#     print('In Valid Number.')   


# **********************************************************
# 18. Check Number is Three-Digit or Not 

# if 100 <= abs(int(str)) <= 999:
#     print("It is a three-digit number.")
# else:
#     print("It is not a three-digit number.")

# *********************************************************
# 19. Login Validation (Username & Password)
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")




    