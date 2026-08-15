# Module 21: Python Data Structures & Algorithms
# Data Structures
# Array
# Stack
# Queue
# Linked List
# Hash Table
# Tree
# Graph
# Algorithms
# Searching
# Linear Search
# Binary Search
# Sorting
# Bubble Sort
# Selection Sort
# Insertion Sort
# Merge Sort
# Quick Sort
# Recursion



# List/Array
# toys = ["Lego", "Puzzle", "Video Game"]
# print(toys[0])

# Dictionaries
# Key-Value जोड़े
toy_chest = {"bottom_drawer": "Legos", "top_shelf": "Action Figure"}
print(toy_chest["top_shelf"])  # Output: Action Figure


# Stacks => LIFO (Last In, First Out)
stack = []
stack.append("Page 1")  # सबसे नीचे जोड़ी
stack.append("Page 2")  # सबसे ऊपर जोड़ी

last_visited = stack.pop()  # सबसे ऊपर वाली चीज़ को बाहर निकाला
print(last_visited)         # Output: Page 2


# Queues => FIFO (First In, First Out)

from collections import deque

queue = deque(["Person 1", "Person 2"])
queue.append("Person 3")  # लाइन के आखिर में जुड़ा

first_served = queue.popleft()  # लाइन के आगे वाले को सर्विस मिली
print(first_served)             # Output: Person 1

# first_served = queue.popright()  # popright() Python mein valid method nahi hai.




# Linear Search vs. Binary Search (किताब में पन्ना ढूंढना)
# Python में Binary Search (इसके लिए लिस्ट का क्रमबद्ध/Sorted होना ज़रूरी है)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Mil gaya index {mid} par!"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return "Nahi mila"

numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 50))  # Output: Mil gaya index 4 par!



# Bubble Sort (खिलौनों को साइज के हिसाब से जमाना)
# कल्पना कीजिए कि आप अपने खिलौनों को छोटे से बड़े क्रम में लगा रहे हैं। 
# आप बगल वाले दो खिलौनों की तुलना करते हैं। अगर बाएं वाला खिलौना दाएं वाले से बड़ा है, 
# तो उनकी जगह आपस में बदल (swap) देते हैं! यह प्रक्रिया तब तक दोहराई जाती है 
# जब तक सारे खिलौने सही क्रम में न आ जाएं।
n=int(input('Enter Array Limit Element : '))
myArr=[]
for i in range(n):
    num = int(input(f"Insert {i+1} Element: "))
    myArr.append(num)

print("Array List : ",myArr)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # जगहों की अदला-बदली (Swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# unsorted_list = [5, 2, 8, 1, 3]
unsorted_list=myArr
print("Sorted List : ",bubble_sort(unsorted_list))  # Output: [1, 2, 3, 5, 8]