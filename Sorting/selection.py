# Input: x=[9,3,1,7,10,6]
# Selection sort : Find minimum and swap it

# Without function definition:
x=[9,3,1,7,10,6]
for i in range(0,len(x)-1):
    mini=i
    for j in range(i,len(x)):
        if x[j]<x[mini]:
            mini=j
    print(f"{i} : {x[mini]}")
    x[i],x[mini]=x[mini],x[i]
    print(x)

"""
0 : 1
[1, 3, 9, 7, 10, 6]
1 : 3
[1, 3, 9, 7, 10, 6]
2 : 6
[1, 3, 6, 7, 10, 9]
3 : 7
[1, 3, 6, 7, 10, 9]
4 : 9
[1, 3, 6, 7, 9, 10]
"""

# Defining Function

# def selection_sort(x):
#     for i in range(0,len(x)-1):
#         mini=i
#         for j in range(i,len(x)):
#             if x[j]<x[mini]:
#                 mini=j
#         x[i],x[mini]=x[mini],x[i]
    
#     return x

# print(selection_sort([9,3,1,7,10,6]))

# Time Complexity: O(N*N)
# Space Complexity: O(1)