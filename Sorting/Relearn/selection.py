# Selection sort:
# -  we select minimum
arr=list(map(int,input().split()))
n=len(arr)

for i in range(n-2):
    for j in range(i+1,n):
        if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)
# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Recursion:
# def selection_sort(i,j,n,arr):
#     if i>= n-2:
#         print(arr)
#         return
#     if j>=n:
#         selection_sort(i+1,i+2,n,arr)
#     if arr[j]<arr[i]:
#         arr[i],arr[j]=arr[j],arr[i]
#     selection_sort(i,j+1,n,arr)

# arr=list(map(int,input().split()))
# n=len(arr)
# print(selection_sort(0,1,n,arr))

