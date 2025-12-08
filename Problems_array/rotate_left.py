# Left rotate an array by one place

# Input: [1,2,3,4,5]
# Output: 2,3,4,5,1

# Optimal

def rotate(arr):
    temp= arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    
x=[1,2,3,4,5]
print(x)
rotate(x)
print(x)

# Time Complexity: O(N)
# Space Complexity: O(1)