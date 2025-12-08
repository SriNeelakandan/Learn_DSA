# Quick Sort
# Idea: Pick the pivot element and Place that in its correct place in sorted array
# ascending order
# Time complexity: O(nlogn)
# Space complexity: O(1)

# steps:
#pick the pivot element and place it in its correct places
#pick the element
    #place it in right of the pivot element if picked element is greater than pivot element
    #place it in left of the pivot element if picked element is less than pivot element

# x=[4,6,2,5,7,9,1,3]
# x=[2,4,0,1,5]
# low=0
# high = len(x)-1
# pivot = 0
# for i in range(low,len(x),1):
#     if x[i]>x[pivot]:
#         for j in range(high,-1,-1):
#             if x[j]<x[pivot]:
#                 if j<=i:
#                     x[j],x[pivot]=x[pivot],x[j]
#                     pa_in=j
#                     break
#                 x[i],x[j]=x[j],x[i]
#                 break         
# print(x)
# print(pa_in)


def fn(arr,low,high):
    pivot = low
    i=low
    j=high
    while(i<j):
        while (arr[i]<=arr[pivot] and i<high):
            i+=1
        while (arr[j]>arr[pivot] and j >low):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def qs(arr,low,high):
    if low<high:
        pa_index = fn(arr,low,high)
        qs(arr,low,pa_index-1)
        qs(arr,pa_index+1,high)

x=[4, 6, 2, 5, 7, 9, 1, 3]
print(f"Input: {x}")
qs(x,0,len(x)-1)
print(f"Output: {x}")