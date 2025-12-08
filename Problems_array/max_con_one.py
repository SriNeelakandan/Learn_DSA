# Find Maximum consecutive ones

# Input: [1,1,0,0,1,1,1,0,1,1]
# Output: 3

def max_ones(arr,n):
    count=0
    max=0
    for i in range(0,n):
        if arr[i]==1:
            count+=1
            if count>max:
                max=count
        else:
            count=0
    
    return max

x=[1,1,0,0,1]
print(max_ones(x,len(x)))

# Time Complexity: O(N)
# Space Complexity: O(1)