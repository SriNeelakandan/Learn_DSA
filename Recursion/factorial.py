# Simple way
# def fact(n):
#     res=1
#     while n!=0:
#         res*=n
#         n-=1
#     return res

# n=int(input("Enter a number: "))
# print(fact(n))
# Time Complexity: The operation of finding factorial done for n times (Given n number times)
# say 5, loop starts from 5,4,3,2,1 -  5 times O(N)

# Space Complexity: res variable is used and kept changing its value 
# O(1)

# Using Recursion:

def fact(x):
    if x<=1:
        return 1
    return x * fact(x-1)

n=int(input("Enter a number: "))
print(fact(n))

# Time Complexity: O(n)
# Space Complexity: O(n)