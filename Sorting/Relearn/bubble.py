# Bubble sort
# select the maximum and move it to the end
# arr=list(map(int,input().split()))
# n=len(arr)

# for i in range(n-1,1,-1):
#     for j in range(i):
#         if arr[j]>arr[i]:
#             arr[i],arr[j]=arr[j],arr[i]
#     print(arr)
    
#Time Complexity: O(N^2)
# Space Complexity: O(1)

# Recursion:

def bubble_sort(i,j,n,arr):
    if i<=1:
        print(arr)
        return
    if j==i:
        print(arr)
        bubble_sort(i-1,0,n,arr)
    if arr[j]>arr[i]:
        arr[i],arr[j]=arr[j],arr[i]
    bubble_sort(i,j+1,n,arr)

arr=list(map(int,input().split()))
n=len(arr)
print(bubble_sort(n-1,0,n,arr))