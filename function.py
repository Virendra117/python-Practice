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