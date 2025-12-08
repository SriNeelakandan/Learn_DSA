# Linear Search
# Input array: [5,7,1,9,3,6,1] , value : 6
# Output: first occurence of 6

def linear_search(arr,n,x):
    for i in range(n):
        if arr[i] ==x:
            return i
    return -1

x=[4,6,2,1,7,3,2,6,3,7]
print(linear_search(x,len(x),10))

# Time Complexity: O(N)
# Space complexity: O(1)

# If they ask last occurence, iterate from last
# If tehy ask all occurence store the index value in list and return that list