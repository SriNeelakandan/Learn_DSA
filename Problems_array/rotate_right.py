# Rotate an array right by one place

# Input : [1,2,3,4,5]
# Output: [5,1,2,3,4]

def rotate(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
x=[1,2,3,4,5]
print(x)
rotate(x)
print(x)