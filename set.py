# Set = aisa collection jisme duplicate values nahi hoti.

# Set {} curly brackets se banta hai:
numbers = {10, 20, 30, 40}

print(numbers)

fruits = {"Apple", "Mango", "Banana"}
print(fruits)


# Duplicate values automatically remove

numbers = {10, 20, 30, 40,20,30,50}

print(numbers)


# Set Ordered nahi hota
# Set mein indexing nahi hoti.
students = {"Rahul", "Amit", "Neha"}

# print(students[0])      # index not allow
print(students)     


# Set mein item add karna — add()

students.add("Ribu")
print(students)

# Multiple items add — update()
fruits = {"Apple", "Mango"}

fruits.update(["Banana", "Orange", "Grapes"])

print(fruits)

# remove() — Item delete
# discard() — Safe delete
# pop() - Set se ek random/arbitrary element remove karta hai.
# clear() - Pura set empty kar deta hai
# len() - Set mein kitne unique elements hain?
# in Operator - Check karna hai ki item Set mein hai ya nahi:

# Set Union - Do Sets ko combine karna.
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))        # Basic format
print(A | B)            # Shortcut


# Intersection
# Dono Sets mein jo common hai.

print(A.intersection(B))
print(A & B)                # Shortcut



# Difference
# A mein hain lekin B mein nahi.
A = {1, 2, 3}
B = {2, 3, 4}

print(A.difference(B))
print(A - B)            # Shortcut



# Symmetric Difference
# Jo values sirf A ya sirf B mein hain, common values nahi.
A = {1, 2, 3}
B = {2, 3, 4}
print(A.symmetric_difference(B))
print(A^B)                  # Shortcut