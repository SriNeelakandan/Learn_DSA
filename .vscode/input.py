#-------------------------------------------------------------------------------------#
# get single input:
# n=input() # type of n - string by default
# n=int(input()) # casting - converts string to integer

#-------------------------------------------------------------------------------------#

# get multiple inputs in a single line - both treated as strings
# n,m=input("Enter a number:").split()
# print(type(n),n)
# print(type(m),m)

#-------------------------------------------------------------------------------------#

# get multiple inputs in a single line - for make them integers
# use map

# n,m=map(int,input("Enter a number:").split())
# print(type(n),n)
# print(type(m),m)

#-------------------------------------------------------------------------------------#

# get list elements using map 

"""
map() is a built-in function that applies a given function to each item of an iterable (like a list, tuple, or string) and returns an iterator (a map object) containing the results. It provides a concise way to perform element-wise transformations without explicit loops. 

How it works:
- map() takes the function and applies it to the first item of the iterable.
- It then applies the function to the second item, and so on, for all items in the iterable.
- It returns a map object, which is an iterator. To view the results as a list, tuple, or other collection, you need to convert the map object (e.g., using list(), tuple()).
"""
# lst=map(int,input().split())
# print(list(lst))
#-------------------------------------------------------------------------------------#
# get list elements one by one and append
# 1-D array / list init by zero
# a=[0 for i in range(4)]
# print(a) # [0,0,0,0]
# a= list(map(int, input().split()))
# print(a)
#-------------------------------------------------------------------------------------#
# 2-D array / list init by zero

# t = [ [0]*4 for i in range(4)]
# print(t)

#-------------------------------------------------------------------------------------#
# 2-D array / list init by zero

# rows = int(input("Enter number of rows: "))
# matrix = [list(map(int, input().split())) for _ in range(rows)]
# print("2D List:", matrix)

#-------------------------------------------------------------------------------------#
