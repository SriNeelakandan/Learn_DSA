# Find the number that appears only once
# Input: [1,1,2,3,3,4,4]
# Output: 2

# Bruteforce
# def once(arr,n):
#     for i in range(0,n):
#         count=0
#         for j in range(0,n):
#             if arr[i]==arr[j]:
#                 count+=1
#         if count==1:
#             return arr[i]

# x=[1,1,2,3,3,4,4]
# print(once(x,len(x)))

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# better
def once(arr,n):
    freq={i:0 for i in arr} # O(N)
    for i in arr:
        freq[i]+=1
    print(freq)
    for x,y in freq.items():
        if y==1:
            return x
    return -1
    

# x=[1,1,2,2,3,3,4,4]
x=[3,1,2,4,3,2,1]
print(once(x,len(x)))

# Time Complexity: O(N)
# Space Complexity: O(N)


# Optimal 

# def once(arr,n):
#     res=0
#     for i in range(0,n):
#         res^=arr[i]
#     return res

# x=[1,1,2,3,3,4,4]
# print(once(x,len(x)))

# Time Complexity: O(N)
# Space Complexity: O(1)