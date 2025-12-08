# Merge sort
# Idea: Divide and Merge in sorted manner

# [4,6,2,3,9,1,5,4,2] - 9 elements - divided into 5+4
# 0 - 4           5-8
# 0-2,3-4         5-6,7-8
# 0-1,2  3  4     5    6   7   8
# 0  1  2  3  4   5    6   7   8


#merge_sort - divides an array logically and sort it


def merge(arr,low,mid,high):
    res=[]
    left = low
    right = mid+1
    while left<=mid and right <=high:
        if arr[left]<arr[right]:
            res.append(arr[left])
            left+=1
        else:
            res.append(arr[right])
            right+=1
    while right<=high:
        res.append(arr[right])
        right+=1
    while left<=mid:
        res.append(arr[left])
        left+=1
    for i in range(low,high+1):
        arr[i]=res[i-low]

def merge_sort(arr,low,high):
    if low == high:     
        return
    mid= int((low+high)/2)
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr

x= [6,2,9,1,10]
print(f"Input: {x}")
print(f"Output: {merge_sort(x,0,len(x)-1)}")

# Time Complexity:
# O(N) * O(log2 N) -  O(NlogN)

# Space Complexity: O(N)