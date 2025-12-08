# Insertion sort
# Idea: Takes an element and places it in its correct order

# Bruteforce

# def insertion(arr,n):
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if arr[j]<arr[j-1]:
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 print(f"swapped: {arr}")
#             print(f"Last checked at {j} -inner")            
            
#         print(f"Last checked {i} -outer")
#     return arr

# # x=[9,3,1,7,10,6] # Worstcase,Average Case
# x=[2,3,5,7,9,10] # Best case
# print(f"Input: {x}")
# print("Insertion Sort \n ----------------------------------------")
# print(insertion(x,len(x)))
# print("Completed\n ----------------------------------------")
# # Time Complexity:
# Outer loop runs for 1 to 6, 5 times, N-1 times
# Inner loop runs - 1 -> 1 ,2 -> 2,1,3 -> 3,2,1 similarly
# so inner loop runs for i times
# so overall - it leads to n*(n+1)/2 
# O(N^2) - worst case, average case
# O(N) - best case, achieved by optimising the code

# Space Complexity: O(1) - Only swapping happens

# Optimised


# def insertion_opt(arr,n):
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             print(f"Last checked at {j}")
#             if arr[j]<arr[j-1]:
#                 arr[j],arr[j-1] = arr[j-1],arr[j]
#                 print(f"swapped: {arr}")
#             break
            
            
#         print(f"Last checked {i} -outer")
#     return arr


# # x=[9,3,1,7,10,6] # Worstcase,Average Case
# x=[2,3,5,7,9,10] # Best case
# print(f"Input: {x}")
# print("Insertion Sort Optimised \n ----------------------------------------")
# print(insertion_opt(x,len(x)))
# print("Completed\n ----------------------------------------")

# Time Complexity: O(N) - only runs for N-1 times and since at each iteration, elements at the end are  checked once to ensure if they are already in its position

def insertion_opt(arr,n,i):
    if i==n:
        return
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        
    insertion_opt(arr,n,i+1)


x=[9,3,1,7,10,6] # Worstcase,Average Case
# x=[2,3,5,7,9,10] # Best case
print(f"Input: {x}")
insertion_opt(x,len(x),1)
print(x)

# Time Complexity: O(N2), (where N = size of the array), for the worst, and average cases.

# Reason: If we carefully observe, we can notice that the recursion call will occur for n times, and for each i, inside the recursive function, the loop j runs from i to 1 i.e. i times. For, i = 1, the loop runs 1 time, for i = 2, the loop runs 2 times, and so on. So, the total steps will be approximately the following: 1 + 2 + 3 +……+ (n-2) + (n-1). The summation is approximately the sum of the first n natural numbers i.e. (n*(n+1))/2. The precise time complexity will be O(n2/2 + n/2). Previously, we have learned that we can ignore the lower values as well as the constant coefficients. So, the time complexity is O(n2). Here the value of n is N i.e. the size of the array.

# Space Complexity: O(N) auxiliary stack space.