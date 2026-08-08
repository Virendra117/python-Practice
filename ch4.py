from array import array

# Array in Python

# Summary Table
# Function	Work
# append(x)	End mein element add karta hai
# insert(i, x)	Index par element add karta hai
# remove(x)	Value delete karta hai
# pop(i)	Index se element delete karta hai
# index(x)	Element ka index batata hai
# count(x)	Value kitni baar hai
# reverse()	Array ko reverse karta hai
# extend(arr)	Do arrays ko jodta hai
# buffer_info()	Memory information deta hai
# typecode	Data type batata hai
# len(arr)	Total elements batata hai
# Important Type Codes
# Type Code	Data Type
# 'i'	Integer
# 'f'	Float
# 'd'	Double
# 'u'	Unicode Character





# Decleration of Array

arr=[1,2,3,4,5,6,7,8,9] 
print('Array : ',arr)
print('Array[0] = ',arr[0])

# or

arrnew={1,2,3,4,5,6,7,8,9}  # it is dictionary
print('Dictionary',arrnew)

# Array with string
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])


for item in fruits:
    print(item)



# append(x)	End mein element add karta hai

students=["Virendra","Ritesh","Karan","Prakash"]

# students.append("Anuj")
# print(students)


# insert(index, Value)	Index par element add karta hai

# students.insert(2,'Mahek')  
# print(students)



# remove(x)	Value delete karta hai
# students.remove('Mahek')
# print(students)


# pop(i)	Index se element delete karta hai
# students.pop(2)
# print(students)



# index(x)	Element ka index batata hai
index=students.index("Ritesh")
print(index)


# count(x)	Value kitni baar hai
number=[10,20,30,30,40,43,54,20]
print(number.count(30))



# reverse()	Array ko reverse karta hai
students.reverse()
print(students)



# extend(arr)	Do arrays ko jodta hai
arr1=[10,20,30,40,50]
arr2=['virendra','Ritesh','Prakash']
arr1.extend(arr2)
print(arr1)



# buffer_info()	Memory information deta hai
# from array import array      Krana hoga, upar laga hai..

number = array('i', [10, 20, 30, 30, 40, 43, 54, 20])

print(number.buffer_info())

address, size = number.buffer_info()

print("Memory Address:", address)
print("Total Elements:", size)


# typecode	Data type batata hai

# Important Type Codes

# Type Code	Data Type
#   'i'	        Integer
#   'f'	        Float
#   'd'	        Double
#   'u'	        Unicode Character

arr = array('i', [10, 20, 30])

print(arr.typecode)


# len(arr)	Total elements batata hai

print(len(students))


# 'u'	Unicode Character
letters = array('u', ['A', 'B', 'C', 'D'])

print(letters)   # output : array('u', 'ABCD')


marks = array('i', [78, 85, 92, 67, 88])

print("Student Marks:")

for mark in marks:
    print(mark)



total=sum(marks)
print(total)




# ****************************************************
original = [10, 20, 30, 40]

n = len(original)

total = n * (n + 1) // 2

print("Total subarrays:", total)

# Print all subarray

for i in range(n):
    for j in range(i, n):
        print(original[i:j+1])



# Sum of Each Subarray

for i in range(n):
    for j in range(i, n):
        subarray = original[i:j+1]
        print(subarray, "=", sum(subarray))
