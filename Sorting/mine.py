# Selection sort
# def select_sort(arr,n):
#     for i in range(0,n-1): #no of elements -1 # 8 elements - 8 times run{0 - 7},we need 7 times run
#         print(f"Outer Loop runs at {i}")
#         mini=i    
#         for j in range(i,n):
#             print(f"Inner Loop runs at {i} -{j}")
#             if arr[j]<arr[mini]:
#                 mini=j
#         arr[i],arr[mini]=arr[mini],arr[i]


# # x=[10,3,6]
# x=[0,1,2,3]
# select_sort(x,len(x))
# print(x)

# Time Complexity:
# Outer loop runs for N-1 times{7 times if no of element is 8}
# for each inner loop, it runs for 
# N,N-1,N-2,N-3 ...2,1 = sum of N natural numbers
# N(N-1)/2  -~=N^2 

# so it leads to O(N^2)

# Space complexity: O(1)

# # Bubble sort
# def bubble_sort(arr,n):
#     for i in range(0,n-1): # run for 4 times,but length of an array is 5
#         for j in range(0,n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j]=arr[j],arr[j+1]
#         print(arr)
    
# x=[20,9,3,5,12]
# print(x)
# bubble_sort(x,len(x))
# print(x)


# Time Complexity:
# Outer loop runs for N-1 times{4 times, no of element is 5 }
# Inner loop runs for each as
# N-1,N-2,N-3.....2,1 = sum of N numbers
# N(N-1)/2 ~=N^2

# Hence time complexity is O(N^2)

# space complexity: O(1)

# Optimised approach for best case scenario

# def bubble_sort(arr,n):
#     for i in range(0,n-1): # run for 4 times,but length of an array is 5
#         print(f"Printed {arr} at {i} - outer")
#         didswapped = False
#         for j in range(0,n-1-i):
#             print(f"Printed {arr} at {i} - {j}")
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j]=arr[j],arr[j+1]
#                 didswapped= True
#         if not didswapped:
#             print(f"Returned at {i} - {j}")
#             return
    
# x=[20,9,7,5,1] # worstcase - reverse sorted array - sorted after 4 iteration
# x=[12,5,3,4,8] # average case - sorted after 3 outer iteration
# x=[1,2,3,4,5] # best case - already sorted array - sorted after single iteration
# bubble_sort(x,len(x))

# Time complexity: O(N^2) - average case,worst case
# O(N) - best  case

# Space Complexity: O(1)

# Another approach like selection sort
# find max and swap to the last
# In selection sort, find min and swap to the first

# def bubble_sort(x):
#     for i in range(0,len(x)-1):
#         maxi=0
#         for j in range(0,len(x)-1-i):
#             if x[j]>x[maxi]:
#                 maxi=j
#         x[len(x)-1-i],x[maxi]=x[maxi],x[len(x)-1-i]
#         print(x)

# x=[12,5,3,4,8]
# bubble_sort(x)
# print(x)

# recursive approach

# def bubble_sort(arr,n):
#     if n==1:
#         return
#     didswapped = False
#     for i in range(0,n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             didswapped = True
#     # print(f"{arr} - outside didswapped")
#     if not didswapped:
#         # print(f"{arr}- inside not swapped")
#         return
#     bubble_sort(arr,n-1)
        

# # x=[5,4,3,2]
# x=[1,2,3,4,5]
# bubble_sort(x,len(x))
# print(x)

# Time Complexity:Same O(N^2) - worst case,average case
#O(N) - Best case

# Space Complexity: O(N) - N- auxiliary stack space.

# Insertion sort:
# def insertion_sort(arr,n):
#     for i in range(1,n):
#         didswapped= False
#         for j in range(i,0,-1):
#             if arr[j]<arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
#                 didswapped= True
#         if not didswapped:
#             return

# # x=[12,4,9,6,2]
# x=[5,4,3,2,1]
# # x=[1,2,3,4,5]
# insertion_sort(x,len(x))
# print(x)

# Time Complexity: 
# Outer loop runs for N-1 times{4 times when no of elements is 5}
# Inner loop runs for each
# 1-> 1 times
# 2 runs for 2 times
# 3 runs for 3 times
# similarly - so overall O(N^2)


# Space Complexity: O(1)


# recursive approach

def insertion_sort(arr,n,i):
    if i ==n:
        return 
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
    insertion_sort(arr,n,i+1)

# x=[12,9,8,11,6,2]
x=[1,2,4,3,2,1]
insertion_sort(x,len(x),1)
print(x)

# Time complexity: O(N^2) - average ,worst case
# space complexity: O(N) - auxiliary stack space.