# Finding Missing Number in an array
# Input: [1,2,4,5] N=5

# Bruteforce
# def find_miss(arr,n):
#     for i in range(1,n+1):
#         flag=0
#         for j in range(0,n):
#             if arr[j]==i:
#                 flag=1
#                 break
#         if flag==0:
#             return i
# x=[1,2,5,3]
# print(find_miss(x,len(x)))

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Better Approach - hashing
# def find_miss(arr,n):
#     new_arr =[0] * (n+1)
#     for i in range(0,len(arr)):
#         new_arr[arr[i]]=1
    
#     for i in range(1,n+1):
#         if new_arr[i]==0:
#             return i

# x=[1,2,5,3]
# print(find_miss(x,5))

# Time complexity: O(N+N)
# Space Complexity: O(N)

#d- actual size of array include missing element
# def find_miss(arr,d):
#     xsum=int((d*(d+1))/2)
#     print(xsum)
#     ysum=0
#     for j in range(len(arr)): # O(N)
#         ysum+=arr[j]
#     return xsum-ysum

# x=[1,2,5,3,4]
# print(find_miss(x,5))

# Time Complexity: O(N)

# Space Complexity: O(1)


# def find_miss(arr,d):
#     xs=0
#     ys=0
#     for j in range(0,len(arr)):
#         ys^=arr[j]
#         xs^=(j+1)
#     xs^=d
    
#     return xs^ys

# x=[1,5,3,4]
# print(find_miss(x,5))

# Time Complexity: O(N)

# Space Complexity: O(1)