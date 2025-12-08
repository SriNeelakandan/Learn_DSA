# Second Largest
# Input: [2,12,5,1,8,9,10,3,11,9,12]

# Brute force
# def f_sl(arr):
#     arr.sort()
#     f_l = arr[len(arr)-1]
#     for i in range(len(arr)-1,-1,-1):
#         if arr[i] !=f_l:
#             return arr[i]
#     return -1
# # x=[2,12,5,1,8,9,10,3,11,9]
# # x= [2,12,5,1,8,9,10,3,11,9,12]
# # x=[7,7,7,7]
# print(f_sl(x))
# Time complexity: O(NlogN)
# Space Complexity: O(1)

# Better Approach:
# def f_sl(arr):
#     f_l = 0
#     for i in range(0,len(arr)):
#         if arr[i]>arr[f_l]:
#             f_l=i
#     s_l=-1
#     for i in range(0,len(arr)):
#         if i!=f_l and arr[i]!=arr[f_l] and arr[i]>s_l:
#             s_l=arr[i]
#     return s_l

# x=[2,12,5,1,8,9,10,3,11,9]
# print(f_sl(x))
# x= [2,12,5,1,8,9,10,3,11,9,12]
# print(f_sl(x))
# x=[7,7,7,7]
# print(f_sl(x))

# Time Complexity: O(N+N)
# Space Complexity: O(1)

# Optimal Approach
# def f_sl(arr):
#     f_l = arr[0]
#     s_l=-1
#     for i in range(1,len(arr)):
#         if arr[i]>f_l:
#             s_l=f_l
#             f_l=arr[i]
#         elif arr[i]<f_l and arr[i]>s_l:
#             s_l=arr[i]
#     return s_l

# x=[2,12,5,1,8,9,10,3,11,9]
# print(f_sl(x))
# x= [2,12,5,1,8,9,10,3,11,9,12]
# print(f_sl(x))
# x=[7,7,7,7]
# print(f_sl(x))

# Time Complexity: O(N)
# Space Complexity: O(1)

# Second Smallest
#  Brute force
# def f_ss(arr):
#     arr.sort()
#     f_s = arr[0]
#     for i in range(0,len(arr)):
#         if arr[i] !=f_s:
#             return arr[i]
#     return -1
# x=[2,2,12,5,1,8,9,10,3,11,9]
# print(f_ss(x))
# x= [2,12,5,1,8,9,10,3,11,9,12]
# print(f_ss(x))
# x=[7,7,7,7]
# print(f_ss(x))
# Time complexity: O(NlogN)
# Space Complexity: O(1)
# import sys
# Better Approach:
# def f_ss(arr):
#     f_s = arr[0]
#     for i in range(0,len(arr)):
#         if arr[i]<f_s:
#             f_s=arr[i]
#     s_s=max(arr)
#     for i in range(0,len(arr)):
#         if arr[i]!=f_s and arr[i]<s_s:
#             s_s=arr[i]
#     return s_s

# x=[2,1,12,5,1,8,9,10,3,11,9]
# print(f_ss(x))
# x= [2,12,5,1,8,9,10,3,11,9,12]
# print(f_ss(x))
# x=[7,7,7,7]
# print(f_ss(x))

# Time Complexity: O(N+N)
# Space Complexity: O(1)

# Optimal Approach
# def f_ss(arr):
#     f_s = arr[0]
#     s_s=max(arr)
#     for i in range(1,len(arr)):
#         if arr[i]<f_s:
#             s_s=f_s
#             f_s=arr[i]
#         elif arr[i]>f_s and arr[i]<s_s:
#             s_s=arr[i]
#     return s_s

# x=[2,2,12,5,1,8,9,10,3,11,9]
# print(f_ss(x))
# x= [2,12,5,1,8,9,10,3,11,9,12]
# print(f_ss(x))
# x=[7,7,7,7]
# print(f_ss(x))

# Time Complexity: O(N)
# Space Complexity: O(1)

# Check array is sorted

# def check_ar(arr):
#     sor= False
#     for i in range(1,len(arr)):
#         if arr[i]>=arr[i-1]:
#             sor = True
#         else:
#             sor= False
#             break
#     return sor

# x=[1,1,2,2,3,3,2,1,3]
# print(check_ar(x))
# x=[1,2,3,3,4,5]
# print(check_ar(x))
# x=[1,1,1,2,2,0]
# print(check_ar(x))

# Time Complexity: O(N)
# Space Complexity: O(1)

# Remove duplicates from sorted array in place

# Brute force

# def rm_dup(arr):
#     unique= list(set(arr))
#     for i in range(len(unique)):
#         arr[i]=unique[i]
#     return arr
# x=[1,1,1,2,2,3,3,4,5,6,1]
# print(rm_dup(x))

# Time Complexity: 
# Convert to set - takes NlogN - times
# Modifying the list elements - N times
# So, it is O(NlogN) + O(N)
# Space Complexity: O(N)  - If all are unique elements

# Better approach

# def rm_dup(arr):
#     unique= []
#     for i in arr:
#         if i not in unique:
#             unique.append(i)
#     for i in range(0,len(unique)):
#         arr[i]=unique[i]
    
#     return arr


# x=[1,1,1,2,2,3,3,4,5,6,1]
# print(rm_dup(x))
# x=[1,1,1]
# print(rm_dup(x))
# x=[1,2,6,5,1]
# print(rm_dup(x))

# Time Complexity: 
# O(N+N)
# Space Complexity:
# O(N)

# Optimal Approach

# def rm_dup(arr):
#     first = 0
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[first]:
#             first+=1
#             arr[first]=arr[i]
#     return arr,first+1

# # x=[1,1,1,2,2,3,3,4,5,6,1]
# x=[1,1,2,2,2,3,3,3,4]
# print(rm_dup(x))
# x=[1,1,1]
# print(rm_dup(x))
# x=[1,2,5,5,6,6,6]
# print(rm_dup(x))

# Time Complexity: O(N)
# Space Complexity: O(1)