# Find union of two sorted arrays:

# Input: 
# arr1 =[1,1,3,4,5,5,5,6,6]
# arr2 = [0,0,2,3,6,6,7]

# Union= Union the elements of both arrays such that element should not be repeated

# Bruteforce
# def union(arr1,arr2):
#     x=set() # O(N1+N2)- space
#     x.update(arr1) # O(N1logN1)
#     x.update(arr2) # O(N2logN2)
#     x=list(x) # O(N1+N2) - time , O(N1+N2) - space
#     return x

# arr1 =[1,1,3,4,5,5,5,6,6]
# arr2 = [0,0,2,3,6,6,7]
# print(union(arr1,arr2))

# # Time Complexity: O(N1logN1) + O(N2logN2) + O(N1+N2)
# # Space Complexity:O(N1+N2) + O(N1+N2)

# Better
def union(arr1,arr2):
    arr=[]
    for i in arr1:
        if i not in arr:
            arr.append(i)
    for j in arr2:
        if j not in arr:
            arr.append(j)
    print(arr)

arr1 =[1,1,3,4,5,5,5,6,6]
arr2 = [0,0,2,3,6,6,7]
union(arr1,arr2)

# time complexity: O(N1) + O(N2)
# Space Complexity: O(N1+N2)

# Optimal Approach using two pointer

# arr1 =[1,1,3,4,6]
# arr2 = [0,3,6,7,9]

# def union(x,y):
#     res=[]
#     i=0
#     j=0
#     while i<len(x) and j<len(y):
#         if (x[i]<y[j]):
#             if x[i] not in res:
#                 res.append(x[i])
#             i+=1
#         else:
#             if y[j] not in res:
#                 res.append(y[j])
#             j+=1
    
#     while j<len(y):
#         if y[j] not in res:
#             res.append(y[j])
#         j+=1
    
#     while i<len(x):
#         if x[i] not in res:
#             res.append(x[i])
#         i+=1
    
#     return res
# arr1 =[1,1,3,4,6]
# arr2 = [0,3,6,7,9]
# print(union(arr1,arr2))

# Time Complexity: O(N1+N2)
# Space Complexity: O(N1+N2)