# brute force 
# def reverse_arr(x,n):
#     ans =[0] *n
#     for i in range(n-1,-1,-1):
#         ans[n-i-1] = x[i]
#     return ans

# arr =[1,2,3,4,5]
# l= len(arr)
# print(reverse_arr(arr,l))

# Time Complexity: O(N) - loop operates for N times 
# Space Complexity: O(N) - same length list is used for storing result 

# Optimal approach
# def reverse(x,n):
#     p1=0
#     p2=n-1
#     while p1 <p2:
#         x[p1],x[p2] = x[p2],x[p1]
#         p1+=1
#         p2-=1
#     return x

# arr =[3,6,2,7,8,9]
# l= len(arr)
# print(reverse(arr,l))
# Time Complexity: O(N) - loop operates for N times 
# Space Complexity: O(1) - No extra space is used, only constant variables are used 

# Using Recursion
# def reverse(x,p1,p2):
#     if p1<p2:
#         x[p1],x[p2] = x[p2],x[p1]
#         return reverse(x,p1+1,p2-1)
#     return x
    
# arr= [1,3,5,7,9]
# l=len(arr)
# print(reverse(arr,0,l-1))

# Time Complexity: O(N) - loop operates for N times 
# Space Complexity: O(1) - No extra space is used, only constant variables are used 

# using inbuilt func
def rev(x):
    x.reverse()
    return x
x=[1,2,3,4,5]
print(rev(x))

# Time Complexity: O(n)
# Space Complexity: O(1)