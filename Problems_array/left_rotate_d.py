# Rotate an array left by D places

# Brute force
def rotate(arr,d,n):
    d=d%n
    # take elements
    new_arr=[]
    for i in range(d):
        new_arr.append(arr[i])

    # shift others
    for i in range(d,n):
        arr[i-d]=arr[i]

    # put back the elements
    for i in range(n-d,n):
        arr[i]=new_arr[i-(n-d)]

x=[1,2,3,4,5,6,7]
print(x)
rotate(x,5,len(x))
print(x)

# Time Complexity:
# O(d) + O(n-d) + O(d) - O(n+d)

# Space Complexity:
# O(d)

# Optimal approach:

def reverse(x,start,end):
    end=end-1
    while start <end:
        x[start],x[end] = x[end],x[start]
        start+=1
        end-=1


def rotate(arr,n,d):
    d=d%n
    reverse(arr,0,d)
    reverse(arr,d,n)
    reverse(arr,0,n)

x=[1,2,3,4,5,6,7]
print(x)
rotate(x,len(x),2)
print(x)

# Time Complexity : O(D) + O(N-D) + O(N) = O(2N)
# Space Complexity: O(1)