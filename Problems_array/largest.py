# Largest Element in an array:
# Input: arr[] = {2,5,1,3,0};
# Output: 5


# Brute force Approach:
# def large(arr):
#     arr.sort()
#     return arr[len(arr)-1]

# x=[5,9,1,8,0,3]
# print(large(x))

# Time Complexity: O(NlogN)
# Space Complexity: O(N)

# Optimal Approach

def large(arr):
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi

x=[2,5,1,5,3,0]
print(large(x))

# Time Complexity: O(N)
# Space Complexity: O(1)
