# Input: x=[4,9,2,10,5,12,8]
# output: 10

# Brute force

# def second_largest(arr):
#     arr.sort()
#     flar = arr[len(arr)-1]
#     for i in range(len(arr)-2,-1,-1):
#         if arr[i]!=flar:
#             return arr[i]
#     return -1


# # x=[4,12,12,10,10,12,12,8]
# x=[7,7,7,7,7]
# print(second_largest(x))

# Time complexity: O(NlogN)+ O(N)
# Space Complexity: O(1)


# def second_smallest(arr):
#     arr.sort()
#     flar = arr[0]
#     for i in range(1,len(arr)):
#         if arr[i]!=flar:
#             return arr[i]


# x=[4,12,12,10,10,12,12,8,8,8,4,6]
# print(second_smallest(x))

# Better Approach

# def second_largest(arr):
#     fmax=arr[0]
#     for i in range(0,len(arr)):
#         if arr[i]>fmax:
#             fmax=arr[i]
#     smax=-1
#     for i in range(0,len(arr)):
#         if arr[i] > smax and arr[i]!=fmax:
#             smax=arr[i]
#     return smax
    

# # x=[4,9,2,10,5,12,8]
# x=[7,7,7,7,7]
# print(second_largest(x))

# Time complexity: O(N+N)- O(2N)

# Optimal Approach
def second_largest(arr):
    flar=arr[0]
    slar=-1
    for i in range(1,len(arr)):
        if arr[i]>flar:
            slar,flar=flar,arr[i]
        elif arr[i] < flar and arr[i]>slar:
            slar=arr[i]
        
    return slar

# x=[4,9,2,10,5,12,8]
x=[7,7,7,7,7]
print(second_largest(x))

# Time Complexity: O(N)
# Space Complexity: O(1)