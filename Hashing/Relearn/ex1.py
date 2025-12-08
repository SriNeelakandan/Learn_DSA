# Hashing
# Input array: [1,3,2,1,4]

# Inputs given:
# size of ip array
# array elements
# no of query
# query elements

n=int(input())
arr=list(map(int,input().split()))
q=int(input())

# Precomputing:
# Hash Array
HashArray = [0] * 13
for i in range(n):
    HashArray[arr[i]]+=1


# Fetching
for i in range(q):
    x=int(input())
    print(HashArray[x])

# Time Complexity: O(N) * O(1) = O(N)
# Space Complexity: O(Max-element-array)