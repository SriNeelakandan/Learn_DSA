# Find the highest and lowest frequency element

# Optimal Approach 
# Map - dictionary in python

n=int(input())
arr=list(map(int,input().split()))

# Map
map_dict={}
for i in range(n):
    map_dict[arr[i]]=map_dict.get(arr[i],0)+1

high=0
high_element=0
low=len(arr)
low_element=0
# fetching
for key,value in map_dict.items():
    if value>high:
        high= value
        high_element=key
    if value < low:
        low= value
        low_element= key
print(high_element," ",low_element)

# Time Complexity: O(N)
# Space Complexity: O(N)