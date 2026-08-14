# Functions
# -------------------------------
# Defining functions
# Calling functions
# Parameters
# Arguments
# Default arguments
# Keyword arguments
# Positional arguments
# *args
# **kwargs
# Return statement
# Multiple return values
# Scope
# Local/global variables
# Lambda functions
# Recursive functions
# -----------------------------------------------------------

# Defining functions

def functionName():
    print("Hello V3i Technology")

functionName()

# Default Arguments: Set default values for parameters if none are provided.
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9 (uses default exponent 2)
print(power(3, 3))  # 27


# Keyword Arguments: Pass arguments by parameter name regardless of position.
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Whiskers", animal_type="cat")



# Arbitrary Arguments (*args & **kwargs):
# *args passes a variable number of positional arguments as a tuple.
# **kwargs passes a variable number of keyword arguments as a dictionary.

def summarize(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

summarize(1, 2, 3, status="active", role="admin")



def add_numbers(*args):
    # 'args' is treated as a tuple inside the function
    return sum(args)

print(add_numbers(1, 2))          # Output: 3
print(add_numbers(10, 20, 30, 40)) # Output: 100



# **kwargs (Keyword Arguments)
# The ** operator unpacks incoming named/keyword arguments into a dictionary.
# Use case: When you want to accept flexible, named parameters (like configuration settings or metadata).


def print_user_profile(**kwargs):
    # 'kwargs' is treated as a dictionary inside the function
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_profile(name="Alex", role="Developer", status="Active")
# Output:
# name: Alex
# role: Developer
# status: Active


# Combining args and kwargsYou can use both in the same function definition. 
# When combining parameter types, 
# Python requires a strict order:
# Standard Parameters $\rightarrow$ *args $\rightarrow$ Default Parameters $\rightarrow$ **kwargs

def log_event(event_type, *args, level="INFO", **kwargs):
    print(f"[{level}] Event: {event_type}")
    print("Positional details:", args)
    print("Metadata:", kwargs)

log_event("USER_LOGIN", "User_123", "IP_192.168.1.1", level="DEBUG", status="Success")



# Return statement

def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val  # Returns a tuple: (sum, diff)

# Unpacking multiple return values
s, d = calculate(10, 4)
print(f"Sum: {s}, Difference: {d}")  # Sum: 14, Difference: 6



# Lambda Functions (Anonymous Functions)
# A Lambda function is a small, single-expression inline function without a formal def name.

# Syntax: lambda arguments : expression

# Standard function
def add_five(x):
    return x + 5

# Equivalent Lambda function
add_five_lambda = lambda x: x + 5

print(add_five_lambda(10))  # Output: 15

# Commonly used with functions like map(), filter(), or sorted()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]



# Recursive Functions

# A recursive function is a function that calls itself to solve a problem by breaking it into smaller instances.

# Every recursive function requires:

# 1)Base Case: A stopping condition that prevents an infinite loop.

# 2)Recursive Case: The logic where the function calls itself with modified input.


# Example: Calculating Factorial (5! = 5 * 4 * 3 * 2 * 1)
def factorial(n):
    # Base Case
    if n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Example:
# 1-Countdown to Zero
# A simple visual example of how recursion replaces standard loops.

def countdown(n):
    if n<=0:
        print("Blastoff!")
        return 0
    print(n)
    countdown(n - 1)
countdown(5)
    


# 2. Sum of Numbers (1 to N)Adds all numbers from 1 up to N.

def sumUpto():
    if 

