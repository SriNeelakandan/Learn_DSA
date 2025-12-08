# Character hashing using map

# Inputs:
arr=input()
n=len(arr)
q=int(input())

# Precomputing - using dictionary
map_dict={}
# Assigning frequencies
for i in range(n):
    map_dict[arr[i]]=map_dict.get(arr[i],0)+1
print(map_dict)
# for key in sorted(map_dict):
#     print(f"{key}->{map_dict[key]}")
# Fetching
for i in range(q):
    x=input()
    print(map_dict.get(x,0))

# Time Complexity: O(N)(precomputing) + O(N)(fetching) = O(2N)= O(N)

# Space Complexity: O(N)