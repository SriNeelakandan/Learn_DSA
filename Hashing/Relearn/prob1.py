# Find the highest and lowest frequency element

# Bruteforce 
n=int(input())
arr=list(map(int,input().split()))

Hash_Array= [0] * (max(arr)+1)
print(Hash_Array)
# Precomputing
for i in range(n):
    Hash_Array[arr[i]]+=1
print(Hash_Array)
high=0
high_element=0
low=len(arr)
low_element=0
# Fetching
for i in arr:
    if Hash_Array[i]>high:
        high= Hash_Array[i]
        high_element=i
    if Hash_Array[i] < low:
        low=Hash_Array[i]
        low_element=i

print(high_element," ",low_element)

# Time Complexity: O(N)
# Space Complexity: O(Max_element_input_aray)