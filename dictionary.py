# Dictionary Python ka ek bahut hi important aur widely used data type hai. 
# Ye data ko Key-Value pairs ke roop me store karta hai.
# Dictionary mutable hoti hai (isme changes kiye ja sakte hain) aur Python 3.7+ se ye ordered bhi hoti hai.

# Basic Syntax & Creation
# Dictionary ko curly braces {} se banaya jata hai, jisme key: value ka pair hota hai.


# Dictionary Create Karna
student = {
    "name": "Rahul",
    "age": 22,
    "course": "B.Tech",
    "skills": ["Python", "SQL"]
}

print(student)
# Bracket Notation
print(student["name"])  # Output: Rahul

# .get() Method (Recommended: Key na hone par error nahi deta)
print(student.get("age"))     # Output: 22
print(student.get("city"))    # Output: None (Error nahi aayega)


# Adding / Updating Elements


# Nayi key-value add karna
student["city"] = "Delhi"

# Purani value update karna
student["age"] = 23

print(student)


# 3. Removing Elements


# .pop() - Key ke zariye delete karna aur value return karna
removed_val = student.pop("course")

# del keyword
del student["city"]

# .clear() - Puri dictionary khali kar dena
# student.clear()



# Important Dictionary Methods
# -------------------------------------------------------------------------------------------
# Method   |   Description                                 |    Example
# --------------------------------------------------------------------------------------------
# .keys()   |  Sabhi keys ki list jaisa object deta hai    |    student.keys()
# --------------------------------------------------------------------------------------------
# .values() |  Sabhi values ki list jaisa object deta hai  |    student.values()
# --------------------------------------------------------------------------------------------
# .items()  |  Keys aur values ke tuples ka pair deta hai  |    student.items()
# -------------------------------------------------------------------------------------------
# .update() |  Doosri dictionary se merge karta hai        |    student.update({"gpa": 8.5})



# Looping through a Dictionary

# Keys aur Values dono par loop chalana
for key, value in student.items():
    print(f"{key} : {value}")