#-------------------------------------------------------------------------------------#
"""
An array is a linear data structure in which we store data and perform any operation, we can randomly access data in an array (With the help of its index values). 

In other words, an array is a collection of similar types of elements (Homogeneous elements) that have contiguous memory locations i.e One after another.

Arrays store the related information in adjacent memory blocks.

If you need to access one or more than one element, the process of finding or performing operations on that element becomes very fast because your computer very well knows where the value is located in the memory.
"""
#-------------------------------------------------------------------------------------#

"""
Why are Arrays ‘0’ indexed?
- Counting arrays from the index value 0 simplifies the computation for the memory. Though it simplifies the computation. But it adds an extra step of an unnecessary subtraction of 1 i.e (n-1) for each access.
- The array of length n can be indexed by the integers from 0 to n-1.
- Most programming languages have been designed in this way only, so indexing from 0 is pretty much inherent to the language.
"""
#-------------------------------------------------------------------------------------#
"""
Defining an array:
As we already specified, the array contains homogeneous data so the above one is an integer array as it contains integer data.

Arrays can store numbers, strings, boolean values, characters, objects, etc. But once you define the type of values that your array will store, all its elements must be of that same type. You cannot “insert” different types of data in a single array.

Arrays cannot store heterogeneous data, Now what it means.
"""
#-------------------------------------------------------------------------------------#
"""
Summary of the Arrays:
- Memory is allocated instantly: After the array is created the memory is allocated instantly and the array is empty until you assign the values.
- Elements are located in contiguous manner: So the elements can be accessed very efficiently (direct access, O(1) = constant time) using it’s index values.
- Arrays are powerful data structures: The type of elements and the size of the array are fixed and defined when you create it. Arrays store elements of the same type (homogeneous).
- Inserting elements: Reach to the end of the array and insert the element. The insertion at the end of the array. Insertion takes constant time O(1). We can also insert the elements in the middle or the start of the array but it's a bit of a complex process.
Removing elements: Reach to the index and remove the element. The removal operation takes constant time O(1).

"""
#-------------------------------------------------------------------------------------#
# Arrays in Pyton 
# - There is no built in support for arrays but python lists can be used

# arr =[2,5,4,2]
# print(arr.append("Neels"))
# print(arr)
# arr.append("Neels") returns None
# arr.pop() returns last element
# arr.pop(2) returns that element
# arr.remove(2) returns None
# arr.sort() returns None
# print(sorted(arr)) # returns the sorted array but does not actually sort the original array
# print(arr)
# 2 5 4 2 Neels
# 0 1 2 3 4
# arr.pop() - returns last element and delete that element from the list
# arr.pop(2) - returns element at index position 2 and delete that element from the list

# print(arr.pop()) #Neels
# print(arr)

# print(arr.pop(2)) #4
# print(arr)

# print(arr.remove(2)) # returns None
# arr.sort()
# print(sorted(arr)) # returns the sorted array but does not actually sort the original array
# print(arr) # [5,4,2,'Neels']
# from array import array
# numbers = array('i', [10, 20, 30, 40])
# print(numbers)
# for x in numbers:
#     print(x)

# numbers.append("Hello") # not possible in this
# print(numbers)

#-------------------------------------------------------------------------------------#

# Strings:

"""
A string is a sequence of characters enclosed within quotes — either single (' '), double (" "), or triple quotes (''' ''' / """ """).
Strings are immutable → Once created, they cannot be changed.
"""
# name= 'srineelakandan'
# # print(type(name))
# # print(name[0])
# # print(len(name)) # {0...13} - total 14
# # print(name[len(name)]) # name[14] - index out of range
# # # name[13] - returns n

# name[0]='R' # TypeError: 'str' object does not support item assignment
# # which means immutable
# print(name)

# triple quotes - multi line string

# text = """I'm learning Python"""
# # print(text)
# print(len(text)) #19

# Indexing
# print(text[4]) # l
# print(text[8]) # n

#slicing
# print(text[3:5])
# print(text[::-1]) # reverse a string
# print(reversed(text))

# text.upper()
# text.lower()
# text.title()
# text.capitalize()
# text= text.replace("le","xx")
# print(text.replace("le","xx")) # returns the modified output
# f= text.split()
# print(f)
# isalpha()
# isdigit()
# isalnum()
# # isspace()
# print(sorted(text)) # [' ', ' ', "'", 'I', 'P', 'a', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'n', 'n', 'o', 'r', 't', 'y']
# s = "Python"
# lst = list(s)
# print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# List → String
# joined = ''.join(lst)
# print(joined)  # Python

# from collections import Counter
# s = "banana"
# print(Counter(s))

# Passing Strings to Functions

# def greet(name):
#     print("Hello,", name)

# greet("Neels")

# Assignment creates a new reference to the same string object (since strings are immutable).

# s1 = "Python"
# s2 = s1
# print(id(s1), id(s2))  # Same memory address

# Modify Inside Function

# def change_name(s):
#     s = "Python"
#     print("Inside function:", s)

# name = "Neels"
# change_name(name)
# print("Outside function:", name)

# output:
# Inside function: Python
# Outside function: Neels
"""
Strings Are Passed by Object Reference

Python uses a model called “pass-by-object-reference” (sometimes called “pass-by-assignment”).

So when you pass a string to a function:
        - You pass a reference to the string object.
        - But since strings are immutable, the function can’t modify it in place.
        
"""
# def modify(s):
#     s += " Rocks!"
#     return s
# msg = "Python"
# print(f"{msg}")
# msg= modify(msg)
# print(f"--{msg}")
# output:
"""
Inside function: Python Rocks!
Outside function: Python

Explanation:

Inside the function → new string "Python Rocks!" created.

Outside → original "Python" unchanged.
"""

# a, b, c = "AI", "ML", "DL"
# print(a, b, c)
# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.replace("H", "J"))
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# 
x=1
x &= 3	
print(x)