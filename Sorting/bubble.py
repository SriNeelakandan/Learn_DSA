# Input: x=[9,3,1,7,10,6]
# Bubble sort : Push the maximum to last by adjacent swapping of elements
# x=[9,3,1,7,10,6]
# print(x)
# for j in range(0,len(x)-1):
#     for i in range(0,len(x)-1-j):# for 0, {0,1,2,3,4}
#         if x[i]>x[i+1]:
#             x[i],x[i+1]=x[i+1],x[i]
#     print(f"last checked {j}")
# print(x)

# Time Complexity: O(N^2) - worst complexity,average complexity
# Checks for each iteration even if an array gets sorted by its previous iterations
# For best case, it can be O(N) - by optimizing the code
# Space Complexity: O(1) - Only swap happens


# Optimized
# It can be optimizied by a condition 
# if the array is not swapped entirely at any step , then it means array is already sorted

# x=[2,3,5,7,9]
# x=[9,3,1,7,10,6]
# # Input:
# print(x)
# for j in range(0,len(x)-1):
#     swapped = False
#     for i in range(0,len(x)-1-j):# for 0, {0,1,2,3,4}
#         if x[i]>x[i+1]:
#             x[i],x[i+1]=x[i+1],x[i]
#             swapped= True
#     print(f"last checked {j}")  
#     if swapped == False:
#         print(f"breaked at {j} step ")
#         break       
# print(x)

# Time Complexity: O(N) - only for best case - N-length of an array

# Recursive Approach:
def bubble(x,n):
        if n==1:
             return
        swapped= False
        for i in range(0,n-1):# for 0, {0,1,2,3,4}
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                swapped = True
        if swapped == False:
             return
        bubble(x,n-1)

x=[9,3,1,7,10,6]
# Input:
print(x)
bubble(x,6)
print(x)

#Time Complexity: O(N2) for the worst and average cases and O(N) for the best case. Here, N = size of the array.

# Space Complexity: O(N) auxiliary stack space.