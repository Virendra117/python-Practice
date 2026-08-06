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

students.append("Anuj")
print(students)


# insert(index, Value)	Index par element add karta hai

students.insert(2,'Mahek')  
print(students)



# remove(x)	Value delete karta hai
students.remove('Mahek')
print(students)


# pop(i)	Index se element delete karta hai
students.pop()
