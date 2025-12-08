# Number hashing -
# problem: If the max element present in given 
# array is large, the size of hash array is also larger which affects the efficiency of code

# Map concept in C++: used for solving this
# How?
#- By storing only necassary elements in hasharray
# Implemented using dictionary in python
# Map in C++ stores keys in sorted order
# But dictionary is not

# Inputs:
n=int(input())# size of input
arr=list(map(int,input().split()))
q=int(input())

# Precomputing - using dictionary
map_dict={}
# Assigning frequencies
for i in range(n):
    map_dict[arr[i]]=map_dict.get(arr[i],0)+1
# print(map_dict)
# for key in sorted(map_dict):
#     print(f"{key}->{map_dict[key]}")
# Fetching
for i in range(q):
    x=int(input())
    print(map_dict.get(x,0))

# Time Complexity: O(N)(precomputing) + O(N)(fetching) = O(2N)= O(N)

# Space Complexity: O(N)